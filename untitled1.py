from tkinter import *

root = Tk()
root.title("Ascii")

root.geometry("400x400")
root.configure(background="snow")

entry_word = Entry(root)
entry_word.place(relx = 0.5, rely = 0.4, anchor = CENTER)
label = Label(root,text="",bg="gold",fg="black")
def asciiconvert():
    label_word = entry_word.get()
    for letters in label_word:
        label["text"] += str(ord(letters)) + " "
button = Button(root, text = "generate", command=asciiconvert)
button.place(relx=0.5,rely = 0.5, anchor = CENTER)
label.place(relx=0.5,rely = 0.6, anchor = CENTER)

root.mainloop()