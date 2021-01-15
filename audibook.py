'''
Dependencies

pip install pyttsx3
pip install PyPDF2
pip install gtts

Kindly confirm the pip installations on google for a better expirience.

'''

from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import pyttsx3
import PyPDF2
from gtts import gTTS
import datetime
import threading
import subprocess

root = Tk()
root.title("PDF TO AUDIOBOOK")

root.geometry("375x300")
root.configure(bg="#003152")
root.resizable(width=0, height=0)

img = PhotoImage(file="audio.png", width=600, height=100)
lab = Label(root)
lab.grid()
lab["compound"] = LEFT
lab["image"] = img

message_str = StringVar()
entry_box = Entry(root, borderwidth=6,
                  textvariable=message_str, font=10, width=29)
entry_box.grid(row=4, column=3)
entry_box.place(x=5, y=150)

# open .pdf files function


def OpenFile():
    name = askopenfilename(initialdir="C:\Downloads",
                           filetypes=(("Text File", "*.pdf"),
                                      ("All Files", "*.*")),
                           title="Choose a file."
                           )
    entry_box.insert(END, name)


files = Button(root, text="PDFILE", width=10, bg="#1D2951",
               fg="#009dc4", command=OpenFile, pady=5)
files.grid(row=4, column=3)
files.place(x=287, y=150)

# main function to convert the pdf to an mp3 file.


def convert():
    try:
        pdfile = entry_box.get()
        book = open(pdfile, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(book)
        num_pages = pdf_reader.numPages

        play = pyttsx3.init()

        for num in range(0, num_pages):
            page = pdf_reader.getPage(num)
            data = page.extractText()

        final_file = gTTS(text=data, lang='en')
        filename = "Audiobook." + str(datetime.datetime.now().date())
        final_file.save(filename + ".mp3")
        messagebox.showinfo("Success", "Audiobook Created")
    except:
        messagebox.showerror("No Pdf File", "Please insert Pdf")


threads = []


def startThredProcess():
    myNewThread = threading.Thread(target=convert)
    threads.append(myNewThread)
    myNewThread.start()


conv = Button(root, text="CREATE", width=40, bg="#1D2951",
              fg="#009dc4", command=startThredProcess, pady=7)
conv.grid(row=4, column=0)
conv.place(x=45, y=220)

root.mainloop()
