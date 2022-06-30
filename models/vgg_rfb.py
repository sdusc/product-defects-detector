
import torch
from torchvision import models
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import transforms, datasets
from fl import BatchFocalLoss
from rfb import BasicRFB
import numpy as np

transforms = transforms.Compose([
    # resize to 224*224 to feed in VGG network
    transforms.Resize(224),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406],
                         [0.229, 0.224, 0.225])
])

vgg16 = models.vgg16(pretrained=True)

# not using vgg dense layer
vgg = vgg16.features

# freeze vgg parameters
for param in vgg.parameters():
    param.requires_grad_(False)


class MyVggModel(nn.Module):
    def __init__(self):
        super(MyVggModel, self).__init__()
        
        self.vgg = vgg
        # reception field block, using dilated conv operator for 3 forward pathway
        self.rfb = BasicRFB(512, 16)


        self.classifier = nn.Sequential(
            nn.Linear(7*7*16, 64),
            nn.ReLU(),
            nn.Linear(64, 2),

        )

    def forward(self, x):
        x = self.vgg(x)
        # 512*7*7

        x = self.rfb(x)

        # flatten output
        x = x.view(x.size(0), -1)
        output = self.classifier(x)
        return output


model = MyVggModel()

model.classifier.load_state_dict(torch.load('./clf.pth', map_location='cpu'))
model.rfb.load_state_dict(torch.load('./rfb.pth', map_location='cpu'))
device = 'cpu'

criterion = BatchFocalLoss().to(device)

train_path = './data_masked/test'

data_train = datasets.ImageFolder(train_path, transform=transforms)

data_loader = DataLoader(data_train, batch_size=8, shuffle=True)

test_path = './data_masked/train'
data_test = datasets.ImageFolder(test_path, transform=transforms)
test_dloader = DataLoader(data_test, 1, False)



correct = 0
total = 0
confusion_mat = np.zeros([2,2])
with torch.no_grad():
    for data in test_dloader:
        image, label = data
        image, label = image.to(device), label.to(device)
        out = model(image)
        pred = torch.argmax(out)
                  
        if pred == label:
            correct += 1
        total += 1
        confusion_mat[label.item(), pred.item()] += 1

        print("test accuracy:{},correct {} out of {}".format(
                correct/total, correct, total))
        print(confusion_mat)
