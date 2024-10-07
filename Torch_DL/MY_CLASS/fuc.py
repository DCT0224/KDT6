# # 모듈 로딩
# # - Model관련
# import torch              
# import torch.nn as nn              
# import torch.nn.functional as F 
# from torch.utils.data import Dataset, DataLoader 
# import torch.optim as optim    
# from torchmetrics.classification import MulticlassF1Score
# from torchinfo import summary 

# #- Data 및 시각화 관련
# import pandas as pd 
# import matplotlib.pyplot as plt              
# from sklearn.preprocessing import * 
# from sklearn.model_selection import train_test_split

# class My_Dataset(Dataset):
#     def __init__(self, featureDF, targetDF):
#         self.featureDF=featureDF 
#         self.targetDF=targetDF
#         self.n_rows=featureDF.shape[0]
#         self.n_features=featureDF.shape[1]
    
#     def __len__(self):
#         return self.n_rows
    
#     def __getitem__(self, index):
#         # 텐서화
#         featureTS=torch.FloatTensor(self.featureDF.iloc[index].values)
#         targetTS=torch.FloatTensor(self.targetDF.iloc[index].values) 
        
#         # 피쳐와 타겟 반환
#         return featureTS, targetTS