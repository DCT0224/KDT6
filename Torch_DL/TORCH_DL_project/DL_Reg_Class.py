# ---------------------------------------------------------------------
# Version.1
# file_name : DL_Reg_Class.py
# Date : 2024-09-18
# 설명 : 모델링 통합본 (Regression_nn, BinaryCF_nn, MultiCF_nn)
# ---------------------------------------------------------------------
# 모델링 관련 모듈 로딩 (DL_Modules.py)
# ---------------------------------------------------------------------
from DL_Modules import *
import time

# ---------------------------------------------------------------------
# 모델 이름 : MyDataset
# 부모클래스 : Dataset 
# 매개 변수 : 
# ---------------------------------------------------------------------
class MyDataset(Dataset):

    def __init__(self, featureDF, targetDF):
        self.featureDF=featureDF
        self.targetDF=targetDF
        self.n_rows=featureDF.shape[0]
        self.n_features=featureDF.shape[1]

    def __len__(self):
        return self.n_rows

    def __getitem__(self, index):
        # 텐서화
        featureTS = torch.FloatTensor(self.featureDF.iloc[index].values) if isinstance(self.featureDF, pd.DataFrame) else torch.FloatTensor(self.featureDF[index])
        targetTS = torch.FloatTensor(self.targetDF.iloc[index].values) if isinstance(self.targetDF, pd.DataFrame) else torch.FloatTensor(self.targetDF[index])

        # 피쳐와 타겟 반환
        return featureTS, targetTS

# ---------------------------------------------------------------------
# 모델 이름 : MyRegModel
# 부모클래스 : nn.Module 
# 매개 변수 : 
# ---------------------------------------------------------------------
class MyRegModel(nn.Module):

    # 모델 구조 구성 및 인스턴스 생성 메서드
    def __init__(self, in_in):
        super().__init__()
        
        self.in_layer=nn.Linear(in_in, 1000)
        self.hidden_layer=nn.Linear(1000, 500)
        self.out_layer=nn.Linear(500, 1)

    # 순방향 학습 진행 메서드
    def forward(self, x):
        # - 입력층
        y = self.in_layer(x)     # y = f1w1 + f2w2 + f3w3 + b ... -> 10개
        y = F.relu(y)            # relu -> y 값의 범위 0 <= y
        
        # - 은닉층 : 10개의 숫자 값(>=0)
        y = self.hidden_layer(y) # y = f21w21 + ... + f210w210 , ... -> 30개
        y = F.relu(y)            # relu -> y 값의 범위 0 <= y

        # - 출력층 : 1개의 숫자 값(>=0)
        return self.out_layer(y) # f31w31 + ... f330w330 + b -> 1개
    
# ---------------------------------------------------------------------
# 모델 이름 : MyBCFModel
# 부모클래스 : nn.Module 
# 매개 변수 : 
# ---------------------------------------------------------------------
class MyBCFModel(nn.Module):

    # 모델 구조 구성 및 인스턴스 생성 메서드
    def __init__(self):
        super().__init__()

        self.in_layer=nn.Linear(4, 10) # 4: iris in 값
        self.hidden_layer=nn.Linear(10, 5)
        self.out_layer=nn.Linear(5, 1)

    # 순방향 학습 진행 메서드
    def forward(self, x):
        # - 입력층
        y = self.in_layer(x)
        y = F.relu(y)

        # - 은닉층 :
        y = self.hidden_layer(y)
        y = F.relu(y)

        # - 출력층
        return F.sigmoid(self.out_layer(y))

# ---------------------------------------------------------------------
# 모델 이름 : MyMCFModel
# 부모클래스 : nn.Module 
# 매개 변수 : 
# ---------------------------------------------------------------------
class MyMCFModel(nn.Module):

    # 모델 구조 구성 및 인스턴스 생성 메서드 
    def __init__(self):
        super().__init__()

        self.in_layer=nn.Linear(4, 10)
        self.hidden_layer=nn.Linear(10, 5)
        self.out_layer=nn.Linear(5, 3)

    # 순방향 학습 진행 메서드
    def forward(self, x):
        # - 입력층
        y = self.in_layer(x)
        y = F.relu(y)

        # - 은닉층
        y = self.hidden_layer(y)
        y = F.relu(y)

        # - 출력층
        return self.out_layer(y)
    
# ---------------------------------------------------------------------
# 모델 이름 : KeyDynamicModel
# 부모클래스 : nn.Module 
# 매개 변수 : in_in, in_out, out_out, *hidden
# ---------------------------------------------------------------------
class KeyDynamicModel(nn.Module):

    # 모델 구조 설계 함수 즉, 생성자 메서드
    def __init__(self, in_in, in_out, out_out, *hidden):
        super().__init__()
        
        self.in_layer=nn.Linear(in_in, hidden[0] if len(hidden) else in_out)
        self.h_layers=nn.ModuleList()
        for idx in range(len(hidden)-1):
            self.h_layers.append( nn.Linear(hidden[idx], hidden[idx+1]) )

        self.out_layer=nn.Linear(hidden[-1] if len(hidden) else in_out, out_out)

    # 학습 진행 콜백 메서드
    def forward(self,x):
        # 입력층
        # y=self.in_layer(x) # y=x1w1+x2w2+x3w3+b1
        # y=F.relu(y)      # 0<=y
        y=F.relu(self.in_layer(x))
        # 은닉층
        for h_layer in self.h_layers:
            y=F.leaky_relu(h_layer(y))
        # 출력층
        return self.out_layer(y)
    
# ---------------------------------------------------------------------