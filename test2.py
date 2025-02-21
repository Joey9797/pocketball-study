import math

# 스트레이트샷
def straight(wx, wy, x, y):
    a = y - wy
    b = x - wx
    r = math.sqrt(a**2 + b**2)

    radian = math.atan2(b, a)
    result = math.degrees(radian)
    if result < 0:
        result += 360
    return result


# hole 확인하기

# 빗겨치기


HOLES = [[0 ,0], [127,0], [254, 0], [0, 127], [127, 127], [254, 127]]
ball_data = [float(x) for x in input().split('/') if x]
wx, wy = ball_data[0], ball_data[1]
for i in range(2, len(ball_data), 2):
    if ball_data[i] > 0:
        x, y = ball_data[i], ball_data[i+1]
        break

print(straight(wx, wy, x, y))


