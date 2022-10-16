a, b = 1, 1
y = a+b
n = int(input('숫자 입력:'))
for k in range(3, n+1):
    c = a+b
    y = c
    a = b
    b = c
    print(y)
print(y)
