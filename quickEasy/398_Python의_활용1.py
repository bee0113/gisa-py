x = input('입력 :')
a = ['abc123', 'def456', 'ghi789']
a.append(x)
a.remove('def456')
# sep =',' : 분리문자로 쉼표를 지정. 출력할 값들을 쉼표로 구분하여 출력
print(a)
print(a[1][-3:], a[2][:-3], sep=',')
for i in range(3, 6):		# 3부터 5(6-1)까지의 연속적인 숫자를 생성
    print(i, end=' ') 	# i의 값을 출력하고 종료문자로 공백 한 칸이 출력된다
