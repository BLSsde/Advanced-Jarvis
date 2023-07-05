from tkinter import *;

# Un USED -> TO Be deleted
root = Tk()
root.configure(background='#26273b')
root.title("Internet Speed Tracker")
root.geometry('300x300')
down_label = Label(root, text="Dowload Speed: x Mbps", fg='#1cbfff',bg="#26273b",font="Arial 15 bold")
down_label.pack(padx=10,pady=20)

up_label = Label(root, text="Uploading Speed: y Mbps", fg='#1cbfff',bg="#26273b",font="Arial 15 bold")
up_label.pack(padx=10,pady=20)

progress = Label(root, text="Loading..", fg='#1cbfff',bg="#26273b",font="Arial 15 italic")
progress.pack(padx=10,pady=20)


def setValues(upload_speed, download_speed):
    down_label.config(text="Dowload Speed: "+str(download_speed)+" Mbps")
    up_label.config(text="Upload Speed: "+str(upload_speed)+" Mbps")
    progress.config(text="Completed!",fg='#00FF00')
    exit()

root.mainloop()