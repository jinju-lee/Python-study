instr="   파  이  썬   "
outstr=''
print(instr)

for i in range(0, len(instr)):
    if instr[i]!=' ':
        print(instr[i], end='')
    else:
        print('-', end='')
