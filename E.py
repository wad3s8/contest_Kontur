n,m,q = map(int, input().split())

arr = []
for i in range(n):
    arr.append(input())

for i in range(q):
    y1, x1 = map(int, input().split())
    y = y1 - 1
    x = x1 - 1
    if arr[y][x] == '.':
        print("MISS")
    else:
        stack = [[y,x]]
        flag = True
        where_we_was = []
        while len(stack) != 0:
            point = stack.pop()
            flag_i = True
            for i in range (-1, 2):
                if flag_i:
                    for j in range(-1, 2):
                        if point[1] + j < 0 or point[1] + j >= len(arr[0]) or point[0] + i < 0 or point[0] + i >= len(arr):
                            continue
                        if (i == 0 and j ==0 or i**2 == j**2):
                            continue
                        if [point[0]+i, point[1]+j] in where_we_was:
                            continue
                        if arr[point[0] + i][point[1] + j] == '.':
                            continue
                        if arr[point[0] + i][point[1] + j] == 'X':
                            print("HIT")
                            arr[y] = arr[y][:x] + '0' + arr[y][x + 1:]
                            flag = False
                            flag_i = False
                            break


                        else:
                            stack.append([point[0]+i, point[1]+j])
                            where_we_was.append([point[0], point[1]])
        if flag:
            print("DESTROY")





