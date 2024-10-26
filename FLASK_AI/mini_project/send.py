# 문장 분류하는 모델
class SentenceClassifier(nn.Module):
    def __init__(self, n_vocab, hidden_dim, embedding_dim, n_layers, n_classes ,dropout=0.5, bidirectional=True, model_type="lstm"):
        super().__init__()  # 부모클래스 상속

        self.embedding = nn.Embedding(num_embeddings=n_vocab, embedding_dim=embedding_dim, padding_idx=0)

        # rnn모델 일 경우
        if model_type == 'rnn':
            self.model = nn.RNN(
                input_size=embedding_dim, hidden_size=hidden_dim, num_layers=n_layers, bidirectional=bidirectional, dropout=dropout, batch_first=True
            )
        # lstm모델 일 경우
        elif model_type == 'lstm':
            self.model = nn.LSTM(
                input_size=embedding_dim, hidden_size=hidden_dim, num_layers=n_layers, bidirectional=bidirectional, dropout=dropout, batch_first=True
            )

        # bidirectional은 양방향성을 의미하는 파라미터
        if bidirectional:
            self.classifier = nn.Linear(hidden_dim * 2, n_classes)   # 양방향일때 타임스탭에서 양방향의 정보(순방향,역방향)의 출력들을 결합하여 분류기에 전달
        else:
            self.classifier = nn.Linear(hidden_dim, n_classes)
        self.dropout = nn.Dropout(dropout)

    def forward(self, inputs):
        embeddings = self.embedding(inputs)
        output, _ = self.model(embeddings) 
        last_output = output[:, -1, :]
        last_output = self.dropout(last_output)
        logits = self.classifier(last_output)
        return logits
    
## 손실 함수와 최적화 함수 정의
from torch import optim
LR = 0.001
n_vocab = len(token_to_id)   # 단어사전의 크기
hidden_dim = 128     # 은닉 사태의 크기
embedding_dim = 128   #임베딩 벡터의 차원 128차원으로 사용
n_layers = 7     # 2층
n_classes = 1 # 2진 분류라 1

classifier = SentenceClassifier(n_vocab=n_vocab, hidden_dim=hidden_dim, embedding_dim=embedding_dim, n_layers=n_layers, n_classes=n_classes,model_type='rnn')

def re_text(text):
    text = re.sub(r'[^ㄱ-ㅎ가-힣 ]+', ' ', text)
    text = text.replace('\xa0','')
    
    return text.strip()

def pad_sequences(sequences, max_length, pad_value):  
    result = list()
    for sequence in sequences:
        sequence = sequence[:max_length] 
        pad_length = max_length - len(sequence)
        padded_sequence = sequence + [pad_value] * pad_length   
        result.append(padded_sequence)
    return np.asarray(result)   

token_to_id = {token: idx for idx, token in enumerate(vocab)} 
new_reviews = [re_text(review) for review in new_reviews]
new_tokens = [[token for token in tokenizer.morphs(review) if token not in stopwords] for review in new_reviews]
new_ids = [[token_to_id.get(token, unk_id) for token in tokens] for tokens in new_tokens]
new_ids_padded = pad_sequences(new_ids, max_length, pad_id)
new_ids_tensor = torch.tensor(new_ids_padded)




## 예측
model.eval()
with torch.no_grad():
    outputs = model(new_ids_tensor)
    predictions = torch.sigmoid(outputs)

# 9. 예측 결과 출력 (0.5 이상이면 긍정, 미만이면 부정)
for i, review in enumerate(new_reviews):
    prediction = 1 if predictions[i] >= 0.5 else 0
    print(f"리뷰: {review}")
    print(f"예측된 결과: {'나이 제한 필요' if prediction == 1 else '전체 이용가'}")