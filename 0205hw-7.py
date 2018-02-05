i=0

for i in range(0,9,1):
    if i<=4:
        print(' '*(4-i), end=' ')
        print('*'*((2*i)+1), end=' ')
        print(' '*(4-i), end='\n')

    if i>4:
        print(' '*(i-4), end=' ')
        print('*'*(8-(2*(i-5)+1)), end=' ')
        print(' '*(i-4), end='\n')

