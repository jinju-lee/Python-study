##윈도우용 프로그램 라이브러리
from tkinter import * 

##전역변수##
window = None
canvas = None
x1, x2, y1, y2 = None, None, None, None

##함수##
def  Click(event):
    global x1, y1, x2, y2
    x1 = event.x
    y1 = event.y

def  Drop(event):
    global x1, y1, x2, y2
    x2 = event.x
    y2 = event.y
    canvas.create_line(x1, y1, x2, y2,width=5, fill="blue")
    
##메인코드##
window=Tk()                                                      ##윈도우 창 만들어주는 함수
window.title("그림판")
canvas= Canvas(window, height=300, width=300)  ##프레임 만들어주는 함수
canvas.bind("<Button-1>",Click)                         ##왼쪽버튼클릭 자동으로 함수 호출
canvas.bind("<ButtonRelease-1>",Drop)             ##왼쪽버튼클릭 자동으로 함수 호출
canvas.pack()                                                   ##따로 있는 창을 묶어주는 함수
window.mainloop()                                            ##창 끌때까지 계속 실행
