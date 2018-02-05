number= input('세 개의 양의 정수를 입력하세요. (구분/): ')
number_split=number.split('/')
number_int=list(map(int, number_split))

if number_int[0]>number_int[1] and number_int[0]>number_int[2]:
    print('가장 큰 수는?: %s' %number_int[0])
elif number_int[1]>number_int[0] and number_int[1]>number_int[2]:
    print('가장 큰 수는?: %s' %number_int[1])
elif number_int[2]>number_int[0] and number_int[2]>number_int[1]:
    print('가장 큰 수는?: %s ' %number_int[2])
