# -----------------------------------------------------------------
# 모듈로딩 
# -----------------------------------------------------------------
from torch import tensor
from torchmetrics.classification import F1Score
from torchmetrics.classification import BinaryF1Score, BinaryAccuracy, BinaryRecall, BinaryPrecision
from torchmetrics.classification import BinaryConfusionMatrix 

# -----------------------------------------------------------------
#  임시데이터 
# -----------------------------------------------------------------
preds = tensor([[0.3745],
                [0.3752],
                [0.3712],
                [0.3807],
                [0.3959],
                [0.4800],
                [0.3781]])
target = tensor([[0.],
                 [0.],
                 [0.],
                 [0.],
                 [1.],
                 [0.],
                 [0.],
                 [0.]])

# 데이터 출력
print(f'preds => {preds}')
print(f'target => {target}')


# -----------------------------------------------------------------
# torchmetrics 패키지 활용 
# -----------------------------------------------------------------
cf = BinaryConfusionMatrix()
print("BinaryConfusionMatrix", cf(preds, target), sep='\n' )

accuray = BinaryAccuracy(zero_division=1.0)
print("BinaryAccuracy  :", accuray(preds, target) )

recall = BinaryRecall(zero_division=1.0)
print("BinaryRecall    :", recall(preds, target) )

precision = BinaryPrecision(zero_division=1.0)
print("BinaryPrecision :", precision(preds, target))

f1Score = BinaryF1Score(zero_division=1.0)
print("BinaryF1Score   :", f1Score(preds, target) )

print('-'*50)


# -----------------------------------------------------------------
# Scikit-learn 패키지 활용 
# -----------------------------------------------------------------
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score, accuracy_score, precision_score, recall_score

print('[sklearn]------------------------')

# scikit-learn은 정수 타입 지원 
preds2= (preds>0.5).int()
print(f'preds2 => {preds2}')
print(f'target => {target}')

sk_cm = confusion_matrix(target, preds2)
print("confusion_matrix", sk_cm, sep='\n' )

sk_accuray = accuracy_score(target, preds2)
print("sk_accuray  :", sk_accuray )

sk_recall = recall_score(target, preds2)
print("sk_recall    :", sk_recall )

sk_precision = precision_score(target, preds2)
print("sk_precision :", sk_precision)

sk_f1Score = f1_score(target, preds2)
print("sk_f1Score   :", sk_f1Score )
