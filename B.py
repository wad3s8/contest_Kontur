n = int(input())

for i in range(n):
    if i == 0:
        rightmost_top = list(map(int, input().split()))
    else:
        now_point = list(map(int, input().split()))
        if now_point[0] > rightmost_top[0]:
            rightmost_top = now_point
        elif now_point[0] == rightmost_top[0]:
            if now_point[1] > rightmost_top[1]:
                rightmost_top = now_point

first = rightmost_top

for i in range(n):
    if i == 0:
        rightmost_top = list(map(int, input().split()))
    else:
        now_point = list(map(int, input().split()))
        if now_point[0] > rightmost_top[0]:
            rightmost_top = now_point
        elif now_point[0] == rightmost_top[0]:
            if now_point[1] > rightmost_top[1]:
                rightmost_top = now_point

second = rightmost_top

print(second[0] - first[0], second[1] - first[1])


