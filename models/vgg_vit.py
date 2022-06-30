import torch
import torch.nn as nn
from vit_pytorch import ViT
from torch.utils.data import DataLoader
from torchvision import transforms, datasets
from fl import BatchFocalLoss


v = ViT(
    image_size=256,
    patch_size=32,
    num_classes=1000,
    dim=1024,
    depth=6,
    heads=16,
    mlp_dim=2048,
    dropout=0.1,
    emb_dropout=0.1
)

net = nn.Sequential(
    nn.Linear(1000, 256),
    nn.ReLU(),
    nn.Linear(256, 2)
)
device = 'cpu'
criterion = BatchFocalLoss().to(device)
transforms = transforms.Compose([
    transforms.Resize(224),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406],
                         [0.229, 0.224, 0.225])
])


optimizer = torch.optim.Adam(
    net.parameters(), 2e-4, (.9, .999), eps=1e-08, weight_decay=0)


train_path = './dataplus/train'

data_train = datasets.ImageFolder(train_path, transform=transforms)

data_loader = DataLoader(data_train, batch_size=16, shuffle=True)

test_path = './dataplus/test'
data_test = datasets.ImageFolder(test_path, transform=transforms)
test_dloader = DataLoader(data_test, 1, False)

epochs = 20

for epoch in range(epochs):
    total_loss = 0
    count = 0
    for i, data in enumerate(data_loader):
        images, labels = data
        images, labels = images.to(device), labels.to(device)
        feature = v(images)
        pred = net(feature)
        loss = criterion(pred, labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
        count += 1

    print("train epoch:{},avg loss:{}".format(epoch, total_loss/count))
    correct = 0
    total = 0
    with torch.no_grad():
        for data in test_dloader:
            image, label = data
            image, label = image.to(device), label.to(device)
            feature = v(images)
            out = net(feature)
            pred = torch.argmax(out)
            if pred == label:
                correct += 1
            total += 1
    print("validation accuracy:{},correct {} out of {}".format(
        correct/total, correct, total))
