from tkinter import *
def action():
    n1=int(txt1.get())
    n2=2*n1
    txt2.insert(0,n2)
f=Tk()
f.geometry("300x250+300+300")
f.minsize(width=400, height=400)
lbl1=Label(f,text="Donnez le nombre")
lbl1.place(x=50,y=50)
txt1=Entry(f)
txt1.place(x=300,y=50)
lbl2=Label(f,text="Le double est :")
lbl2.place(x=50,y=100)
txt2=Entry(f)
txt2.place(x=300,y=100)
btn=Button(f,text="Valider",command=action)
btn.place(x=350,y=180)
f.mainloop()