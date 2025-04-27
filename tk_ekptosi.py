# tk_ekptosi.py - Υπολογισμός έκπτωσης
#
# Ο χρήστης εισάγει την αρχική τιμή και το ποσοστό έκπτωσης και
# το πρόγραμμα υπολογίζει την τελική τιμή με την έκπτωση.
#
# Κυριάκος, 11/4/2025
# kyke@otenet.gr

from tkinter import *

def clicked(*args):
    try:
        arxiki_timi = float(txt_timi.get())
        pososto = float(txt_pososto.get())
        poso_ekptosis = arxiki_timi * pososto / 100
        timi_me_ekptosi = arxiki_timi - poso_ekptosis
        timi_me_ekptosi = f"Τιμή με έκπτωση: {timi_me_ekptosi:.2f} ευρώ"
        lbl_result.configure(text = timi_me_ekptosi, font=("Arial 12"))
    except ValueError:
        lbl_result.configure(text = "Εισάγετε αριθμούς μόνο")

root = Tk()
root.title("Υπολογισμός έκπτωσης")
root.geometry("300x150")
root.resizable(False, False)

root.columnconfigure([0, 1], weight = 1)

lbl_timi = Label(root, text = "Τιμή προϊόντος:")
lbl_timi.grid(column = 0, row = 0)

txt_timi = Entry(root, width=10)
txt_timi.grid(sticky = "W", column = 1, row = 0)

lbl_pososto = Label(root, text = "Ποσοστό έκπτωσης %:")
lbl_pososto.grid(column = 0, row = 1)

txt_pososto = Entry(root, width = 10)
txt_pososto.grid(sticky = "W", column = 1, row = 1)

btn = Button(root, text = "Υπολογισμός", command = clicked)
btn.grid(column = 0, row = 2, pady = 5)

lbl_result = Label(root)
lbl_result.grid(column = 0, row = 3, columnspan = 2)

txt_timi.focus_set()

root.bind("<Return>", clicked)
root.mainloop()