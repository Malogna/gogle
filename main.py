from tkinter import *
import webbrowser
from PIL import Image, ImageTk
from AnimatedGIF import *
window=Tk()

#cate 1
categif1 = AnimatedGif(window, 'img/cate.gif', 0.01)  # (tkinter.parent, filename, delay between frames)
categif1.pack()
categif1.place(x=205, y=145)
categif1.start()  # Shows gif at first frame and we are ready to go

#cate 2
categif2 = AnimatedGif(window, 'img/cate.gif', 0.01)  # (tkinter.parent, filename, delay between frames)
categif2.pack()
categif2.place(x=50, y=145)
categif2.start()  # Shows gif at first frame and we are ready to go

#goglelubb henter text fra entry boksen og putter det inn i bing jeg mener gogle 2007 trademark
def submit(): 
    gogleglubb=entry.get()
    webbrowser.open(f"https://www.bing.com/search?q={gogleglubb}")

lbl=Label(window, text="gogle trademark 2007", fg='red', font=("Helvetica", 16))
lbl.place(x=60, y=50)
entry=Entry(window, text="skriv hva er søke", bd=5)
entry.place(x=80, y=150)
btn=Button(window, text="tryk får søke", fg='blue', command=submit)
btn.place(x=80, y=100)

#epic image
imgload = Image.open("img\poopy.png")
imgload.thumbnail((250, 250))
render = ImageTk.PhotoImage(imgload)
img = Label(image=render, borderwidth=0)
img.image = render
img.place(x=0, y=200)

window.resizable(False, False)
window.title('g0ogple')
window.geometry("300x300+10+10")
window.mainloop()