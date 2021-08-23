i = int(input('첫번째로 더할 수를 입력하세요 : '))
n = int(input('두번째로 더할 수를 입력하세요 : '))

if i < 0:
    print('값는 양수여야 합니다.')
elif n < 0:
    print('값은 양수여야 합니다.')
elif i > 0:
    print(i + n)
elif n > 0:
    print(i + n)