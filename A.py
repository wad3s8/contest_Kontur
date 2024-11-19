n = int(input())

unique = 0
count = 0
touth = ''
for i in range(n):

    input_string = input()
    inputt = set(input_string)
    if len(inputt) > unique:
        unique = len(inputt)
        count += 1
        touth = input_string

print(unique, touth)