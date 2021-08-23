makephone = ['apple', 'samsung', 'oppo', 'amazone', 'lg']

print(makephone)
print('휴대폰 제조사의 개수는 ' + str(len(makephone)) + '개 입니다.')
print('제조사 리스트의 3번째 제조사는' + str(makephone[3]))

print('makephone 리스트에서 제거')
print(makephone.remove('lg'))
print(makephone)