import os
from django.conf import settings

from skimage.io import imread
from skimage.transform import resize
import torch
import torch.nn as nn
from torch.nn import Linear, Sequential, Conv2d, Module, Dropout
import numpy as np
import torchvision.models as models

# Model Weight paths
weights_dir = os.path.join(os.path.dirname(
    settings.BASE_DIR), 'chest-x-ray-covid-19-detection', 'research', 'weights')
our_model_weights = os.path.join(weights_dir, 'our_model_weight_part222.pth')
vgg_weights = os.path.join(weights_dir, 'vgg_weights_part2.pth')


def conv_block(ni, nf, size=3, stride=1):
    def for_pad(s):
        return s if s > 2 else 3
    return nn.Sequential(
        nn.Conv2d(ni, nf, kernel_size=size, stride=stride,
                  padding=(for_pad(size) - 1)//2, bias=False),
        nn.BatchNorm2d(nf),
        nn.LeakyReLU(negative_slope=0.1, inplace=True)
    )


def triple_conv(ni, nf):
    return nn.Sequential(
        conv_block(ni, nf),
        conv_block(nf, ni, size=1),
        conv_block(ni, nf)
    )


def maxpooling():
    return nn.MaxPool2d(3, stride=2)


class Net(Module):
    def __init__(self):
        super(Net, self).__init__()

        self.cnn_layers = Sequential(
            # Defining a 2D convolution layer
            conv_block(7, 8),
            Dropout(0.3),
            maxpooling(),
            conv_block(8, 16),
            Dropout(0.3),
            maxpooling(),
            triple_conv(16, 32),
            Dropout(0.3),
            maxpooling(),
            triple_conv(32, 64),
            Dropout(0.3),
            maxpooling(),
            triple_conv(64, 128),
            Dropout(0.3),
            maxpooling(),
            triple_conv(128, 256),
            Dropout(0.3),
            maxpooling(),
            conv_block(256, 128, size=1),
            Dropout(0.3),
            conv_block(128, 256),
            Dropout(0.3),
            Conv2d(256, 2, 3),
        )

        self.linear_layers = Sequential(
            Linear(16, 2)
        )

    # Defining the forward pass
    def forward(self, x):
        x = self.cnn_layers(x)
        x = x.view(x.size(0), -1)
        x = self.linear_layers(x)
        return x


# Below function takes uploaded image path and return 0 or 1
# 0 - for covid -ve , 1 - for covid +ve
def chest_xray_predict(obj):
    img_path = os.path.join(os.path.dirname(
        settings.BASE_DIR), 'chest-x-ray-covid-19-detection', 'media', str(obj.image))
    print(" path is ", weights_dir)
    print("image url is ", img_path)
    img = imread(img_path)
    img = img/255
    img = resize(img, output_shape=(224, 224, 3),
                 mode='constant', anti_aliasing='True')
    img = img.astype('float32')
    img_reshape = img.reshape(1, 3, 224, 224)
    img = torch.from_numpy(img_reshape)
    vgg_model = models.vgg16_bn()
    vgg_model.classifier[6] = Sequential(Linear(4096, 2))
    vgg_model.load_state_dict(torch.load(
        vgg_weights, map_location=torch.device('cpu')))
    vgg_model.cpu()
    x = vgg_model.features(img)
    x = x.reshape(1, 7, 7, 512)
    our_model = Net()
    our_model.load_state_dict(torch.load(
        our_model_weights, map_location=torch.device('cpu')), strict=False)
    output = our_model(x)
    softmax = torch.exp(output).cpu()
    prob = list(softmax.detach().numpy())
    prediction = np.argmax(prob, axis=1)
    print("prediction ", prediction, " proba ", prob)
    return prediction
