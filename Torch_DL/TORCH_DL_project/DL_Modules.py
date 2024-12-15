# ---------------------------------------------------------------------
# Version.1
# file_name : DL_Modules.py
# Date : 2024-09-18
# 설명 : DL 모델링용 모듈
# ---------------------------------------------------------------------
# 모델링 관련 모듈 로딩
# ---------------------------------------------------------------------
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
import torch.optim as optim
from torchinfo import summary

from torchmetrics.regression import R2Score, MeanSquaredError
from torchmetrics.classification import F1Score, BinaryF1Score
from torchmetrics.classification import MulticlassF1Score
from torchmetrics.classification import BinaryConfusionMatrix
from torchmetrics.classification import MulticlassConfusionMatrix

# ---------------------------------------------------------------------
# 데이터 분석 관련 모듈 로딩
# ---------------------------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import koreanize_matplotlib

from sklearn.preprocessing import *
from sklearn.model_selection import train_test_split

# 활용 패키지 버전 체크
print(f'torch Ver.:{torch.__version__}')
print(f'pandas Ver.:{pd.__version__}')
print(f'numpy Ver.:{np.__version__}')