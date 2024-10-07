# 모듈 로딩
# - Model관련
import torch              
import torch.nn as nn              
import torch.nn.functional as F 
from torch.utils.data import Dataset, DataLoader 
import torch.optim as optim    
from torchmetrics.classification import MulticlassF1Score
from torchinfo import summary 

#- Data 및 시각화 관련
import pandas as pd 
import matplotlib.pyplot as plt              
from sklearn.preprocessing import * 
from sklearn.model_selection import train_test_split


def draw_BCF(SCORE_HISTORY,LOSS_HISTORY):

    TH = len(SCORE_HISTORY[1])

    fg, axes=plt.subplots(1,2, figsize=(10,5), sharex=True)
    fg.suptitle('IRIS Loss & R2')

    axes[0].plot(range(1, TH+1), LOSS_HISTORY[0][:TH], label='Train')
    axes[0].plot(range(1, TH+1), LOSS_HISTORY[1][:TH], label='Val')
    axes[0].grid()
    axes[0].legend()
    axes[0].set_xlabel("Epoch")
    axes[0].set_ylabel("Loss")
    axes[0].set_title("LOSS")

    axes[1].plot(range(1, TH+1), SCORE_HISTORY[0][:TH], label='Train')
    axes[1].plot(range(1, TH+1), SCORE_HISTORY[1][:TH], label='Val')
    axes[1].grid()
    axes[1].legend()
    axes[1].set_xlabel("Epoch")
    axes[1].set_ylabel("R2")
    axes[1].set_title("R2")

    plt.tight_layout()
    plt.show()
