way=input('입금 수단은 무엇입니까?')
kind=input('통화 종류는 무엇입니까?')

if way=='통장' or way=='카드':
    if kind=='현금':
        print('\n귀하의 입금 처리는 가능합니다.')
    else:
        print('\n%s의 입금은 불가합니다.' %kind)
