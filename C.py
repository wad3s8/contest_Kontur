n, k, q = list(map(int, input().split()))
value = list(map(int, input().split()))

#скользящее окно
changes = q
left = 0
right = 0
max_val = 0
while right < n:
    if value[right] >= k:
        if changes != 0:
            changes -= 1
            right += 1
        else:
            while value[left] < k:
                left += 1
            changes += 1
            left += 1
    else:
        right += 1
    max_val = max(max_val, right-left)

print(max_val)



