# ---------------------------------------------------------------------
# Version.1
# file_name : DL_func.py
# Date : 2024-09-19
# 설명 : DL 모델링용 함수 모음
# ---------------------------------------------------------------------
# 모듈 로딩
# --------------------------------------------------------------------- 

import torch
import os
from torch.nn.utils.rnn import pad_sequence

# ---------------------------------------------------------------------
# 함수 이름 : save_model()
# 함수 역할 : 모델 저장 함수
# 매개 변수 : 
# ---------------------------------------------------------------------

def save_model(model, SAVE_FILE):
    ### 학습된 모델 파라미터 값 확인
    print(model.state_dict())

    # 모델 저장
    torch.save(model.state_dict(), SAVE_FILE)

    # 모델 즉, 가중치와 절편 로딩
    # [1] 가중치와 절편 객체로 로딩
    # [2] 모델의 state_dict 속성에 저장

    # 읽기
    wbTS = torch.load(SAVE_FILE)

    # 모델 인스턴스에 저장
    model.load_state_dict(wbTS)


# ---------------------------------------------------------------------
# 함수 이름 : load_model()
# 함수 역할 : 모델 호출 함수
# 매개 변수 : 
# ---------------------------------------------------------------------

def load_model(model, SAVE_MODEL):
    model = torch.load(SAVE_MODEL, weights_only=False)

# ---------------------------------------------------------------------
# 함수 이름 : predice_model()
# 함수 역할 : 모델 예측 함수
# 매개 변수 : model, data
# ---------------------------------------------------------------------

def predict_model(model, data):
    dataTS = torch.FloatTensor(data).reshape(1,-1)

    # 검증 모드로 모델 설정
    model.eval()
    with torch.no_grad():

        # 추론/평가
        pre_val=model(dataTS)
        
    return pre_val
# ---------------------------------------------------------------------
# 함수 이름 : training
# 함수 역할 : 배치 크기 만큼 데이터 로딩해서 학습 진행
# 매개 변수 : score_func
# ---------------------------------------------------------------------

def training(model, trainDL, loss_func, score_func, optimizer):
    # 학습 모드로 모델 설정
    model.train()
    # 배치 크기 만큼 데이터 로딩해서 학습 진행
    loss_total, score_total=0,0
    for featureTS, targetTS in trainDL:

        # 학습 진행
        pre_y=model(featureTS)

        # 손실 계산
        loss=loss_func(pre_y, targetTS)
        loss_total+=loss.item()
        
        # 성능평가 계산
        score=score_func(pre_y, targetTS)
        score_total+=score.item()

        # 최적화 진행
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    return loss_total, score_total

# ---------------------------------------------------------------------
# 함수 이름 : validate
# 함수 역할 : 배치 크기 만큼 데이터 로딩해서 검증 진행
# 매개 변수 : loss_func, score_func
# ---------------------------------------------------------------------

def validate(model, loss_func, score_func, valDS):
    # 검증 모드로 모델 설정
    model.eval()
    with torch.no_grad():
        # 검증 데이터셋
        val_featureTS=torch.FloatTensor(valDS.featureDF.values)
        val_targetTS=torch.FloatTensor(valDS.targetDF.values)
        
        # 평가
        pre_val=model(val_featureTS)

        # 손실
        loss_val=loss_func(pre_val, val_targetTS)

        # 성능평가
        score_val=score_func(pre_val, val_targetTS)
    return loss_val, score_val

# ---------------------------------------------------------------------
# 함수 이름 : collate_fn
# 함수 역할 : 각 배치에서 텐서의 길이를 맞추기 위해 패딩을 적용
# 매개 변수 : batch
# ---------------------------------------------------------------------

def collate_fn(batch):
    features, targets = zip(*batch)
    
    # 피쳐와 타겟에 패딩 적용
    padded_features = pad_sequence([torch.tensor(f) for f in features], batch_first=True)
    padded_targets = pad_sequence([torch.tensor(t) for t in targets], batch_first=True)
    
    return padded_features, padded_targets