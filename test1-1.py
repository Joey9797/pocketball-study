import math

'''
Stage 1
Data Received: 64/64/250/122/-1/-1/-1/-1/-1/-1/-1/-1/
Data Sent: 72.681062/97.416631/
           각도/속도/
Stage 2
Data Received: 64/64/120/8/-1/-1/-1/-1/-1/-1/-1/-1/
Data Sent: 135.000000/39.597980/

Stage 3
Data Received: 64/64/5/5/-1/-1/-1/-1/-1/-1/-1/-1/
Data Sent: 225.000000/41.719300/

Stage 4
처음 상황
Data Received: 64/64/250/120/-1/-1/10/120/-1/-1/-1/-1/
Data Sent: 73.244251/97.123633/
첫번째 공 넣은 후 상황
Data Received: 192.79/102.77/-1/-1/-1/-1/10/120/-1/-1/-1/-1/

Stage 5
Data Received: 64/64/190/64/-1/-1/198/78/-1/-1/198.5/63.5/

Stage 6
Data Received: 64/64/190/64/198/51/198/78/215/64/198/64/

'''

WIDTH = 254
HEIGHT = 127
r = 5.73 / 2 # 공의 반지름

HOLES = [[0 ,0], [127,0], [254, 0], [0, 127], [127, 127], [254, 127]]
h1 = [0, 127]
h3 = [254, 127]
# [x, y]
NUMBER_OF_BALLS = 6
balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]
server_str = "64/64/250/122/-1/-1/-1/-1/-1/-1/-1/-1/" 
data = server_str[:len(server_str)-1].split('/')
data = [float(n) for n in data]

wx, wy = data[0], data[1]
for i in range(2, len(data), 2):
    if data[i] > 0:
        tx, ty = data[i], data[i+1]
        break

ta = ty - wy     # 타겟과 흰공의 밑변
tb = tx - wx     # 타겟과 흰공의 높이
tc = math.sqrt(ta**2 + tb**2)      # 타겟과 흰공사이의 거리
# radian = math.atan2(b, a)
# result = math.degrees(radian)
# if result < 0:
#     result += 360 
# print(result)

# 빗겨치기------------------------------------------------------------
ha = h3[1] - wy     # 구멍과 흰공의 밑변
hb = h3[0] - wx     # 구멍과 흰공의 높이
ang_h = math.degrees(math.atan2(hb, ha))    # 구멍과 흰공 사이의 각도

a = math.sqrt(ha**2 + hb**2)   # 흰공과 구멍 사이의 거리
b = math.sqrt((h3[1] - ty)**2 + (h3[0] - tx)**2)   # 타겟과 구멍 사이의 거리
cos_c = (a**2 + b**2 - tc**2) / 2*a*b   # cc(나머지 한 변)를 구하기 위해 필요한 값 cos_c
bb = b + 2*r
c = math.sqrt(a**2 + bb**2 - 2*a*bb * cos_c)   # 흰공이 타겟과 접하기 위해 굴러가야 하는 거리
ang_t = math.degrees(math.acos((a**2 + c**2 - bb**2) / 2*a*c))  # 흰공이 타겟과 접했을 때의 각도
result = ang_h + ang_t      # 최종 각도(degree)

'''
1. 흰공-구멍(6개)의 각도를 각각 전부 구한다.
2. 흰공-타겟 각도를 구한다.
3. 만약 흰공-구멍 각도와, 흰공-타겟 각도의 차이(절댓값)가 5? 이하를 만족하는 구멍이 있는지 찾는다.
4. 있다면 스트레이트샷을 날린다.
5. 없다면 흰공-구멍 각도와 흰공-타겟 각도의 차이(절댓값)가 45? 이하인 경우를 찾아 빗겨치기를 한다. (세게 날린다)
'''