import torch
import torch.nn as nn
import torch.functional as F
import torchvision.transforms as transforms
from torchvision import datasets
from torch.utils.data import DataLoader
from torch.optm import Adam 
import matplotlib.pyplot as plt



# %% defining Vision transfomer Model
class VisionTransformer(nn.modules):
    def __init__(self, num_classes =10, d_model = 768, num_heads=12, num_layers=12, 
                 dim_feedforward=2048):
        super(VisionTransformer, self).__init__()
        self.patch_size = 16
        self.num_patches = (32 //self.patch_size)
        self.embedding = nn.Linear(3*self.patch_size **2, d_model)
        self.transformer_encoder = nn.TransformerEncoder(nn.TransformerEncoderLayer)