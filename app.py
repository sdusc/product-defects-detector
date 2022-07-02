import io
import torch
from torchvision import models, transforms
from PIL import Image
from flask import Flask, jsonify, request, render_template, app
from utils.constants import INPUT_IMG_SIZE, NEG_CLASS
from utils.helper import predict_localize
import os
from utils.dataloader import get_train_test_loaders, get_cv_train_test_loaders

checkpoint_path = '/Users/xu/Desktop/PDD/weights/dataplus_model.h5'
model = torch.load(checkpoint_path)

class_name = ["Good", "Anomaly"] if NEG_CLASS == 1 else ["Anomaly", "Good"]
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
heatmap_thres = 0.7

def transform_image(image_bytes):
    img_transforms = transforms.Compose([
        transforms.Resize(INPUT_IMG_SIZE), transforms.ToTensor(),
    ])

    image = Image.open('/Users/xu/Desktop/PDD/data/dataset/dataplus/test/anomaly/126-fliph.JPG')
    return img_transforms(image).unsqueeze(0)


def get_prediction(image_bytes):
    tensor = transform_image(image_bytes=image_bytes)
    outputs = model.forward(tensor)
    _, prediction = torch.max(outputs, 1)
    return class_name[prediction]


img = Image.open('/Users/xu/Desktop/PDD/data/dataset/dataplus/test/anomaly/126-fliph.JPG')
print(get_prediction(img))

data_folder = "/Users/xu/Desktop/PDD/data/dataset"
subset_name = "dataplus"
data_folder = os.path.join(data_folder, subset_name)

train_loader, test_loader = get_train_test_loaders(
    root=data_folder, batch_size=10, test_size=0.2, random_state=42,
)

''' Visualization '''
predict_localize(
    model, test_loader, device, thres=heatmap_thres, n_samples=15, show_heatmap=False
)
