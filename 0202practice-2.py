semester=int(input('이수 학기 = '))
grade=int(input('이수 학점 = '))

if semester>=6 and grade>=150:
    print('귀하는 정상 졸업자 입니다.')
else:
    print('귀하는 졸업 대상자가 아닙니다.')
    
