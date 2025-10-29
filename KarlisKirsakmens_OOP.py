
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("600x400")
root.title("Kustības paātrinājums")


tk.Label(root, text="Ieraksti sakuma ātrumu: ").pack()
ievade1 = tk.Entry(root)
ievade1.pack()

tk.Label(root, text="Ieraksti beigu ātrumu: ").pack()
ievade2 = tk.Entry(root)
ievade2.pack()

tk.Label(root, text="Ieraksti kustības laiku: ").pack()
ievade3 = tk.Entry(root)
ievade3.pack()

def rezultats():
    try:
        sa = float(ievade1.get())
        ba = float(ievade2.get())
        la = float(ievade3.get())
        sum = (ba - sa) / la
    except:
        messagebox.showerror("Kļūda", "Nav ievadīts skaitlis!")

    rezultata_teksts.config(text="Paātrinājums: " + str(sum))

rezultata_poga = tk.Button(root, text="Summa", command=rezultats)
rezultata_teksts = tk.Label(root, text="Paātrinājums: ")

rezultata_poga.pack()
rezultata_teksts.pack()

attels_objekts = tk.PhotoImage(file='bilde.gif')
attela_konteineris = tk.Label(root, image=attels_objekts)
attela_konteineris.image = attels_objekts
attela_konteineris.pack(pady=20)

root.mainloop()
