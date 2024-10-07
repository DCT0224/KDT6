import pandas as pd
import random as rad

def yut():
    stick=[]
    for _ in range(4):
        x=rad.randint(0,1)
        stick.append(x)
        stick.sort(reverse=True)
    return stick
## 윷 던져서 나오는 배열 값 만듬.

def score(x):
    yut_name=[]
    yut_score=0
    if x == [1,1,1,0]:
        yut_score = 1
        yut_name = '도'
    elif x == [1,1,0,0]:
        yut_score = 2
        yut_name = '개'
    elif x == [1,0,0,0]:
        yut_score = 3
        yut_name = '걸'
    elif x == [0,0,0,0]:
        yut_score = 4
        yut_name = '윷'
    elif x == [1,1,1,1]:
        yut_score = 5
        yut_name = '모' 
    return yut_score, yut_name

# print(score(yut())) 
## 윷 던져서 점수 나오는거 만듬

########### player turn #############
player_turn = rad.randint(0,1) # 흥부가 먼저일지 놀부가 먼저일지 정하는거 # 흥부 = 0, 놀부 = 1
# player_turn = 1 - player_turn # 플레이어 턴 바꾸기

########### player score 저장 변수 ############
h_score = 0
n_score = 0

# 윷놀이 시작!
while True:
    if h_score >=20:
        print('*'*35)
        print(f'흥부 승리 => 흥부: {h_score}, 놀부: {n_score}')
        print('*'*35)
        break
    if n_score >=20:
        print('*'*35)
        print(f'놀부 승리 => 흥부: {h_score}, 놀부: {n_score}')
        print('*'*35)
        break
    while True:

        if player_turn == 0:
            yut_result = yut()
            if  yut_result == [0,0,0,0] or yut_result == [1,1,1,1]:
                score_yut= score(yut_result)
                h_score += score_yut[0]
                print(f'흥부 {yut_result}: {score_yut[1]} ({score_yut[0]}점)/(총 {h_score}점) -->')
            else : 
                score_yut= score(yut_result)
                h_score += score_yut[0]
                print(f'흥부 {yut_result}: {score_yut[1]} ({score_yut[0]}점)/(총 {h_score}점) -->')
                player_turn = 1 - player_turn
                break
        if  player_turn == 1:
            yut_result = yut()
            if  yut_result == [0,0,0,0] or yut_result == [1,1,1,1]:
                score_yut= score(yut_result)
                n_score += score_yut[0]
                print(f'                                     <-- 놀부 {yut_result}: {score_yut[1]} ({score_yut[0]}점)/(총 {n_score}점)')
            else:
                score_yut= score(yut_result)
                n_score += score(yut_result)[0]
                print(f'                                     <-- 놀부 {yut_result}: {score_yut[1]} ({score_yut[0]}점)/(총 {n_score}점)')
                player_turn = 1 - player_turn
                break



