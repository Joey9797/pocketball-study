import math


def up_right(wx, wy, x, y):  # 목적구가 오른쪽 위에 있을 때
    a = y - wy
    b = x - wx
    r = math.sqrt(a**2 + b**2)

    radian = math.atan(b / a)
    result = math.degrees(radian)
    return result


def down_right(wx, wy, x, y):  # 목적구가 오른쪽 아래에 있을 때
    a = wy - y
    b = x - wx
    r = math.sqrt(a**2 + b**2)

    radian = math.atan(b / a)
    result = math.degrees(radian)
    return 180 - result


def up_left(wx, wy, x, y):  # 목적구가 왼쪽 위에 있을 때
    a = y - wy
    b = wx - x
    r = math.sqrt(a**2 + b**2)

    radian = math.atan(b / a)
    result = math.degrees(radian)
    return 360 - result


def down_left(wx, wy, x, y):  # 목적구가 왼쪽 아래에 있을 때
    a = wy - y
    b = wx - x
    r = math.sqrt(a**2 + b**2)

    radian = math.atan(b / a)
    result = math.degrees(radian)
    return 180 + result


HOLES = [[0 ,0], [127,0], [254, 0], [0, 127], [127, 127], [254, 127]]
ball_data = [float(x) for x in input().split('/') if x]
wx, wy = ball_data[0], ball_data[1]
for i in range(2, len(ball_data), 2):
    if ball_data[i] > 0:
        x, y = ball_data[i], ball_data[i+1]
        break

# hole 확인하기


# 스트레이트샷
if y > wy and x > wx:  # 목적구가 오른쪽 위에 있을 때
    print(up_right(wx, wy, x, y))

elif wy > y and x > wx:  # 목적구가 오른쪽 아래에 있을 때
    print(down_right(wx, wy, x, y))

elif y > wy and wx > x:  # 목적구가 왼쪽 위에 있을 때
    print(up_left(wx, wy, x, y))

elif wy > y and wx > x:  # 목적구가 왼쪽 아래에 있을 때
    print(down_left(wx, wy, x, y))

# 빗겨치기
