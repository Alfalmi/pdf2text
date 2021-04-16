import tkinter

window = tkinter.Tk()
window.geometry('450x400')

tag = tkinter.Label(window, text='Hola Mundo!', bg='Blue')
tag.grid(row=0, column=0)

# tag.pack(fill=tkinter.BOTH, expand=False)


def saludo(nombre):
    print('Hola ' + nombre)


def textin():
    txt = inputtext.get()
    tag['text'] = txt
    print("Tu : " + txt)


boton1 = tkinter.Button(window, text='Push', command=textin, padx=30, pady=20)
# boton1.pack()
boton1.grid(row=2, column=1)

inputtext = tkinter.Entry(window, font="Helvetica 20")
# inputtext.pack()
inputtext.grid(row=2, column=0)
window.mainloop()
