# ---------------------------------------------------------------------
# Version.1
# file_name : ML_preprocessing.py
# Date : 2024-09-16
# 설명 : 머신러닝 데이터전처리 - 인코딩
# ---------------------------------------------------------------------
# 데이터 관련 모듈 로딩
# ---------------------------------------------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------
# 데이터 전처리 관련 모듈 로딩
# ---------------------------------------------------------------------

# 인코딩 관련 모듈
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.preprocessing import OrdinalEncoder

# 스케일링 관련 모듈
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# ---------------------------------------------------------------------
# 함수이름 : convert_label()
# 함수목적 : 라벨 인코딩 진행
# 매개변수 : items
# ---------------------------------------------------------------------

def convert_label(items):
    lencoder = LabelEncoder()
    lencoder.fit(items)
    return lencoder.transform(items)

# ---------------------------------------------------------------------
# 함수이름 : convert_onehot()
# 함수목적 : 원-핫 인코딩 진행
# 매개변수 : items
# ---------------------------------------------------------------------

def convert_onehot(items):
    # 2차원 ndarray로 변환.
    items = np.array(items).reshape(-1, 1)
    ohencoder = OneHotEncoder()
    ohencoder.fit(items)
    return ohencoder.transform(items)

# ---------------------------------------------------------------------
# 함수이름 : sScale()
# 함수목적 : StandardScaling 진행
# 매개변수 : dataset
# ---------------------------------------------------------------------

def sScale(dataset):
    # StandardScaler 객체 생성
    sScaler = StandardScaler()
    # StandardScaler로 데이터 세트 변환
    sScaler.fit(dataset)
    return sScaler.transform(dataset)

# ---------------------------------------------------------------------
# 함수이름 : mmScale()
# 함수목적 : MinMaxScaling 진행
# 매개변수 : dataset
# ---------------------------------------------------------------------

def mmScale(dataset):
    # MinMaxScaler 객체 생성
    mmScaler = MinMaxScaler()
    # MinMaxScaler로 데이터 세트 변환
    mmScaler.fit(dataset)
    return mmScaler.transform(dataset)

