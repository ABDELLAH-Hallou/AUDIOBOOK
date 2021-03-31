import sys
import pyttsx3
import PyPDF2
from tkinter import *
from tkinter import filedialog
import tkinter.ttk as ttk
import io
import os
from os import chdir, getcwd, listdir, path
import codecs
from PIL import Image
from PIL import ImageTk
# import locale
# locale.getdefaultlocale()
# import os
# import keyboard
# import multiprocessing
# import time
# import threading
# from threading import Thread, Lock
# tkinter
root = Tk()
root.title("AudioBook")
root.geometry("880x520")
root['background']='#80d4ff'
s = ttk.Style()
s.configure('Wild.TRadiobutton',background='#80d4ff')
engine = pyttsx3.init()
#help

def helpwin():
    win = Toplevel(root)
    win.title("Guide") 
    win.geometry("1200x500")
    Label(win,  
          text ="Qui sommes nous ?\n"
          "AUDIOBOOK est un convertisseur gratuit dédie a vous aider à \ntransformer vos livres,"
          " fichier de format PDF, ou un texte saisie, en fichier audio.\n"
          "Comment convertir un fichier PDF en un fichier MP3.\n"
          "Pour effectuer ce genre de tache doit juste saisire le texte \nsur l'interface"
          " principale de l'application ou bient télécharger un fichier \nPDF déja existant "
          "sur votre machine on utilisant le bouton <<Telecharger>> qui s'affiche en haut de l'écran.\n"
          "Pour commencer la lecture, il suffit de cliquer sur le button \n<<speak>> "
          "qui est sous forme d'une icone d'un homme qu'est entrain de parler\n"
          "vous pouvez également apporter quelque modifications aux \ndifferents paramétre de lecture\n"
          "Vous avez la chance de changer la voix par defaut par celle \nd'un robot d'une femme,"
          " vous pouvez également ajuster la vitesse de lectures selon vos besoin.\n"
          "Pour importer un fichier, il suffit de cliquer sur le bouton <<télécharger>>\n"
          "Pour sortir de l'application utilisez le bouton <<exit>>\n"
          "Pour obtenir une aide utiliser le bouton <<help>>.\n "
          "la conversion avec votre service est-elle vraiment gratuit?\n"
          "Oui, notre service est complétement gratuit Vraiment!",font=("Courier", 12)).place(x=50,y=50)



# setting function
def conf(rate, volume, voice, gender):
    engine.setProperty('rate', rate)
    engine.setProperty('volume', volume)
    voices = engine.getProperty('voices')
    # for voice in voices:
    #     print(voice.id)
    if voice=='English':
        print('eng')
        if gender=='Male':
            engine.setProperty('voice', voices[0].id)
        else:
            engine.setProperty('voice', voices[7].id)
    elif voice=='Français':
        print('fr')
        if gender=='Male':
            engine.setProperty('voice', voices[4].id)
        else:
            engine.setProperty('voice', voices[5].id)
    else:
        print('ar')
        if gender=='Male':
            engine.setProperty('voice', voices[1].id)
        else:
            engine.setProperty('voice', voices[6].id)
# voices : 
# HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0
# HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_arSA_NaayfM
# HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enUS_MarkM
# HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_frCA_CarolineM
# HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_frCA_ClaudeM
# HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_frCA_NathalieM
# HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_arEG_Hoda
# HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0
# start talking
def talk(lg,gender):
    conf(rate.get(), volume.get()/10, lg,gender)
    engine.say(my_entry.get("1.0",END))
    engine.runAndWait()
    # my_entry.delete(0,END)
# stop talking
def stop():
    root.quit()
    sys.exit()
# upload a pdf and convert it
def load(lg,gender):
    root.filename=filedialog.askopenfilename(initialdir="D:\hallou abdo\technologie\EST\S4\GP\projet", title="Select A File")
    if root.filename == '':
        pass
    else:
        book = open(root.filename, 'rb')
        # with open(root.filename, 'rb') as b:
        #     book = b.read()
        # book = open(root.filename, encoding=locale.getdefaultlocale()[1])
        pdfReader = PyPDF2.PdfFileReader(book)
        pages = pdfReader.numPages
        if len(pge.get())==0:
            pge.insert(0,pages)
        conf(rate.get(), volume.get()/10, lg,gender)
        wholeText = ' '
        for i in range(int(pgs.get()), int(pge.get())):
            page = pdfReader.getPage(i)
            text = page.extractText()
            wholeText = wholeText + text
        # wholeText.encode('utf-8')
        my_entry.insert("1.0",wholeText)
def telecharger(lg,gender):
    conf(rate.get(), volume.get()/10, lg,gender)
    audio = my_entry.get("1.0",END)
    engine.save_to_file(audio,  'AudioBook'+'.mp3')
    engine.runAndWait()
# switching languages
languages = [
    ("English","English"),
    ("Français","Français"),
    ("عربي","Arabe"),
]

lg = StringVar()
lg.set("English")
x=25
y=375
for text, value in languages:
    ttk.Radiobutton(root, text=text, variable=lg, value=value, style = 'Wild.TRadiobutton').place(x=x, y=y)
    y+=50
# switching genders
genders = [
    ("Female","Female"),
    ("Male","Male"),
]

gender = StringVar()
gender.set("Male")
x=135
y=375
for text, value in genders:
    ttk.Radiobutton(root, text=text, variable=gender, value=value, style = 'Wild.TRadiobutton').place(x=x, y=y)
    y+=50
# images
imgDownload = Image.open('images/download.png')
imgDownload = imgDownload.resize((70,70), Image.ANTIALIAS)
imgUpload = Image.open('images/upload.png')
imgUpload = imgUpload.resize((70,70), Image.ANTIALIAS)
imgSpeak = Image.open('images/speaking.png')
imgSpeak = imgSpeak.resize((70,70), Image.ANTIALIAS)
imgExit = Image.open('images/exit.png')
imgExit = imgExit.resize((70,70), Image.ANTIALIAS)
imgInfo = Image.open('images/info.png')
imgInfo = imgInfo.resize((70,70), Image.ANTIALIAS)
imageDownload = ImageTk.PhotoImage(imgDownload)
imageUpload = ImageTk.PhotoImage(imgUpload)
imageSpeak = ImageTk.PhotoImage(imgSpeak)
imageExit = ImageTk.PhotoImage(imgExit)
imageInfo = ImageTk.PhotoImage(imgInfo)
# GUI
my_entry = Text(root, font=("Helvetica", 12), width=80,height=20)
my_entry.place(x=25, y=5)
scroll_y = Scrollbar(root, orient="vertical", command=my_entry.yview)
scroll_y.pack(side="left", fill="y")
my_entry.configure(yscrollcommand=scroll_y.set)
fromPage = Label ( root, text="From page :", bg='#80d4ff' )
fromPage.place(x=225, y=375)
pgs = Entry(root, font=("Helvetica", 12), width=5, bg='white')
pgs.place(x=300, y=375)
pgs.insert(0,0)
toPage = Label ( root, text="To page :", bg='#80d4ff'  )
toPage.place(x=360, y=375)
pge = Entry(root, font=("Helvetica", 12), width=5, bg='white')
pge.place(x=420, y=375)
# convert = Button(root, image = imageSpeak, bg='#FF636F',activebackground='#AAF2FF' ,command=lambda: talk(lg.get(),gender.get()),borderwidth=0)
# stop = Button(root, image= imageExit, command=stop,borderwidth=0)BBA6A8
# upload = Button(root, image = imageUpload, bg='#AAF2FF',activebackground='#FF636F' ,command=lambda: load(lg.get(),gender.get()),borderwidth=0)
# download = Button(root, image= imageDownload, bg='#AAF2FF',activebackground='#FF636F' ,command=lambda: telecharger(lg.get(),gender.get()),borderwidth=0)
convert = Button(root, image = imageSpeak, bg='#80d4ff', command=lambda: talk(lg.get(),gender.get()), borderwidth=0, cursor="hand2")
stop = Button(root, image= imageExit, bg='#80d4ff',command=stop, borderwidth=0, cursor="hand2")
upload = Button(root, image = imageUpload, bg='#80d4ff',command=lambda: load(lg.get(),gender.get()), borderwidth=0, cursor="hand2")
download = Button(root, image= imageDownload, bg='#80d4ff',command=lambda: telecharger(lg.get(),gender.get()), borderwidth=0, cursor="hand2")
helpbutton = Button(root, image= imageInfo, bg='#80d4ff',command=helpwin, borderwidth=0, cursor="hand2")
rate = Scale(root, showvalue = 0, tickinterval = 100, length=200, from_=0, to=400, orient = HORIZONTAL, background='#80d4ff', highlightthickness = 0)
rate.set(200)
ratelabel = Label ( root, text="Rate :", bg='#80d4ff' )
volume = Scale(root, showvalue = 0, tickinterval = 1, length=200, from_=0, to=10, orient = HORIZONTAL, background='#80d4ff', highlightthickness = 0)
volume.set(10)
volumelabel = Label ( root, text="Volume :", bg='#80d4ff' )
upload.place(x=775, y=5)
convert.place(x=775, y=100)
download.place(x=775, y=200)
stop.place(x=775, y=300)
helpbutton.place(x=775, y=400)
ratelabel.place(x=545, y=375)
rate.place(x=545, y=400)
volumelabel.place(x=545, y=435)
volume.place(x=545, y=460)
root.mainloop()