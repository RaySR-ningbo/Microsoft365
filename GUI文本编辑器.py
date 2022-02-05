from tkinter import *
from tkinter.scrolledtext import ScrolledText

print("尊敬的客户您好，由于服务器故障，系统正在维护中，请暂停使用，谢谢配合")
def load():
    with open(filename.get()) as file:
        contents.delete('1.0', END)
        contents.insert(INSERT, file.read())

def save():
    with open(filename.get(), 'w') as file:
        file.write(contents.get('1.0', END))

top = Tk()
top.title("Simple Editor")

contents = ScrolledText()
contents.pack(side=BOTTOM, expand=True, fill=BOTH)

filename = Entry()
filename.pack(side=LEFT, expand=True, fill=X)

Button(text='尊敬的客户您好，由于服务器故障，系统正在维护中，请暂停使用，谢谢配合',command=load).pack(side=LEFT)
Button(text='维护中',command=save).pack(side=LEFT)

mainloop()
