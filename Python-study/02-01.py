instr='<<<파<<이>>썬>>>'
outstr=''

for i  in range(0,len(instr)):
    if (instr[i] != '<')&(instr[i]!='>'):
        outstr+=instr[i]

print("원 문자열==>"+'['+instr+']')
print("공백 제거==>"+'['+outstr+']')
        
