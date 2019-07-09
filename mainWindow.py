from tkinter import *
from tkinter import filedialog
from tkinter import ttk # 콤보박스 사용 위해
from sendLogic import *


#send 클릭 이벤트 함수
def send_info():
    varTo = e_To.get()
    varFrom = e_From.get()
    varSubject = e_Subject.get()
    varText = e_Text.get("1.0","end-1c") #왜?? 1.0, end-1c를 써야되지??
    varPath = fn["text"]
    varPw = e_Pw.get()
    varToSever = combo.get()
    varFromSever = combo.get()
    init_connection(varTo, varFrom, varSubject, varText, varPath, varPw, varToSever, varFromSever)

def openFile():
    mainWindow.filename = filedialog.askopenfilename(initialdir = "/", title='파일 선택', filetypes = (("txt file", ".txt"),("all files", "*.*")))
    fn["text"] = mainWindow.filename


if __name__ == "__main__":
    mainWindow = Tk()
    mainWindow.title("eMailSRender")

    width_of_program = 650
    height_of_program = 300

    #화면의 정 중앙
    screenX = mainWindow.winfo_screenwidth()/2
    screenY = mainWindow.winfo_screenheight()/2

    locationX = screenX - (width_of_program/2)
    locationY = screenY - (height_of_program/2)

    mainWindow.geometry("%dx%d+%d+%d" % (width_of_program, height_of_program, locationX, locationY))

    mainWindow.resizable(width=False, height=False)
    #콤보박스
    combo = ttk.Combobox(mainWindow)
    combo['value'] = ('google.com', 'naver.com', 'hanmail.net')
    combo.current(0)
    combo2 = ttk.Combobox(mainWindow)
    combo2['value'] = ('google.com', 'naver.com', 'hanmail.net')
    combo2.current(0)

    l_To = Label(mainWindow, text = "To.")
    e_To = Entry(mainWindow)

    l_From = Label(mainWindow, text = "From.")
    e_From = Entry(mainWindow)

    l_Pw = Label(mainWindow, text = "Your PW.")
    e_Pw = Entry(mainWindow, show="*")

    l_Subject = Label(mainWindow, text = "Subject.")
    e_Subject = Entry(mainWindow)

    l_Text = Label(mainWindow, text = "Text.")
    e_Text = Text(mainWindow, width=40, height=5)

    l_File = Label(mainWindow, text = "File.")
    fn = Label(mainWindow)

    b_SelcetFile = Button(mainWindow, text="파일 선택", command = openFile)
    b_Send = Button(mainWindow, text="Send", command=send_info)
    
    l_To.grid(row=0, column=0)
    e_To.grid(row=0, column=1, columnspan=2, sticky=EW)
    Label(mainWindow, text='@').grid(row=0, column=3)
    combo.grid(row=0, column=4, columnspan=2, sticky=EW)

    l_From.grid(row=1, column=0)
    e_From.grid(row=1, column=1)
    Label(mainWindow, text='@').grid(row=1, column=2)
    combo2.grid(row=1, column=3)

    l_Pw.grid(row=1, column=4)
    e_Pw.grid(row=1, column=5)

    l_Subject.grid(row=2, column=0)
    e_Subject.grid(row=2, column=1, columnspan=5, sticky=EW)

    l_Text.grid(row=3, column=0)
    e_Text.grid(row=3, column=1, columnspan=5, sticky=NSEW)

    l_File.grid(row=4, column= 0)
    b_SelcetFile.grid(row=4, column=1, columnspan=2, sticky=EW)
    fn.grid(row=4, column=3, columnspan=3, sticky=EW)

    b_Send.grid(row=5, column=3, columnspan=3, sticky=EW)

    mainWindow.mainloop()