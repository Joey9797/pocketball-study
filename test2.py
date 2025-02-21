WIDTH = 254
HEIGHT = 127
RADIUS = 5.73 / 2  # 공의 반지름

HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]
# [x, y]
NUMBER_OF_BALLS = 6
is_first = True  # 내가 선플레이어
balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]
server_str = "64/64/250/122/-1/-1/-1/-1/-1/-1/-1/-1/"
data = server_str[: len(server_str) - 1].split("/")
data = [int(n) for n in data]
print(data)
idx = 0
for i in range(NUMBER_OF_BALLS):
    for j in range(2):
        balls[i][j] = data[idx]
        idx += 1
print(balls)

if is_first:
    # 1, 3, 5 처리
    pass
else:
    # 2, 4, 5 처리
    pass
