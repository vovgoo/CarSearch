import smtplib
from email.mime.text import MIMEText
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

def main_streep(result):

    def click():
        if(len(entry.get()) != 0):
            try:
                email = entry.get()
                #with open("file.txt", "r", encoding="utf-8") as f:
                 #   text = f.read()
                msg = MIMEText(result)
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login("iqtestvovgoo@gmail.com", "jfpxbrpnqlrlfzjd")
                server.sendmail("iqtestvovgoo@gmail.com", email, msg.as_string())
            except:
                pass
        window.destroy()

    window = Tk()

    window.title("Отправка на почту")
    window.geometry('500x300')
    window.resizable(width=False, height=False)
    lbl = ttk.Label(window, font=("Lilita One", 20), text="Введите свою почту ниже", padding=30)
    lbl.pack(anchor="center")

    entry = ttk.Entry(window, width=40, font=("Lilita One", 10))
    entry.pack(anchor="center", padx=10, pady=30)

    s = ttk.Style()
    s.configure('.', font=('Lilita One', 20))

    btn = ttk.Button(window, text="Отправить", command=click)
    btn.pack(anchor="center", padx=10, pady=10)


    window.mainloop()

if __name__ == "__main__":
    main_streep()