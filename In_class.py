from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("Denomination calculator")
root.configure(bg="light blue")
root.geometry("650x400")

upload = Image.open("./app_img.jpg")
upload = upload.resize((300,300))
image = ImageTk.PhotoImage(upload)

label = Label(root, image=image, bg="light blue")
label.place(x=180, y=20)
label2 = Label(root, text="Hello, welcome to the Denomination Calculator", bg="light blue")
label2.place(relx=0.5, y=340, anchor=CENTER)

def msg():
    Msgbox = messagebox.showinfo("Alert", "Do you want to calculate ?")
    if Msgbox == "ok":
        topwin()

btn = Button(root, text="Click me", command=msg, bg="brown", fg="white")
btn.place(x=260, y=360)

def topwin():
    top = Toplevel()
    top.title("Denomination Calculator")
    top.configure(bg="light grey")
    top.geometry("650x350")

    label = Label(top, text="Enter your total amount", bg="light grey")
    entry = Entry(top)
    lb1 = Label(top, text="output")

    l1 = Label(top, text="200", bg="light grey")
    l2 = Label(top, text="50", bg="light grey")
    l3 = Label(top, text="10", bg="light grey")

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calculator():
        try:
            global amount
            amount = int(entry.get())
            note200 = amount//200
            amount %= 200
            note50 = amount//50
            amount %= 50
            note10 = amount//10
            amount %= 10

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert (END,str(note200) )
            t2.insert (END,str(note50) )
            t3.insert (END,str(note10) )

        except ValueError:
            messagebox.showerror("Error", "Enter a proper number")
    calculate_btn = Button(top, text="Calculate", bg="brown", fg="white", command=calculator)

    label.place(x=230, y=50   )
    entry.place(x=200, y=80   )
    calculate_btn.place(x=240, y=120   )
    lb1.place(x=140, y=170   )

    l1.place(x=180, y=200   )
    l2.place(x=180, y=230   )
    l3.place(x=180, y=260   )

    t1.place(x=270, y=200   )
    t2.place(x=270, y=230   )
    t3.place(x=270, y=260)

    top.mainloop()

root.mainloop()