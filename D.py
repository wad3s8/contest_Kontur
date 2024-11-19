

def bin_search(arr, value):
    left = 0
    right = len(arr) - 1
    while (right - left) != 1:
        mid = (right + left) // 2
        if arr[mid] > value:
            right = mid
        else:
            left = mid
    return arr[right]


n, m = map(int, input().split())
u, v = map(int, input().split())
x_reg = list(map(int, input().split()))
y_reg = list(map(int, input().split()))
x_reg.append(n)
x_reg.append(0)
x_reg.sort()
y_reg.append(m)
y_reg.append(0)
y_reg.sort()

q = int(input())
for i in range(q):
    x1, y1, x2, y2 = map(int, input().split())
    if bin_search(x_reg, x1) == bin_search(x_reg, x2) and bin_search(y_reg, y1) == bin_search(y_reg, y2):
        print("YES")
    else:
        print("NO")



