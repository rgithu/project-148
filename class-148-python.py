from tkinter import *
import random
root=Tk()
root.title("list")
root.geometry("500x500")
random_numberlist= Label(root,text="bottle,tiffin,id card,chocolates,chips,tickets,hanky")
randomnumbersortedlist = Label(root)

def random_number():
    random_list = random.randint(1,7)
    randomnumbersortedlist["text"]="Numbers alloted to the things ad=re from 1 to 7 and things need to be taken to picnic are  "+str(random_list)
    
btn = Button(root , text="generated numbers are ",command=random_number)
random_numberlist.place(relx=0.5,rely=0.1,anchor=CENTER)
randomnumbersortedlist.place(relx=0.5,rely=0.5,anchor=CENTER)
btn.place(relx=0.5,rely=0.3,anchor=CENTER)


root.mainloop()

label_random_number["text"]=str(ran1)