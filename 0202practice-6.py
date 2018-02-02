sum=0

grade=input('세 과목의 점수를 입력하세요.(입력구분은 /) : ')
grade_split=grade.split('/')
grade_int=list(map(int, grade_split))

if grade_int[0]>60 and grade_int[1]>60 and grade_int[2]>60:
    print('귀하는 합격 입니다.')
else:
    for i in range(0,3):
        sum+=grade_int[i]
    aver=sum/3
    if aver>70:
        print('\n귀하는 합격 입니다.')
    else:
        print('\n귀하는 불합격 입니다.')
    
