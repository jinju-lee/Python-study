singer={}

singer[' 이름 ']='아이오아이'
singer['구성원수']=11
singer['데뷔']='픽미픽미픽미업'
singer['대표곡']='프로듀스 IOI'

for k in singer.keys():
    print('%s --> %s' %(k,singer[k]))

c=set(singer)
print(c)
type(c)
