
import tkinter as tk

root = tk.Tk()
root.geometry("400x400")
root.title("Kustības paātrinājums")

attels_objekts = tk.PhotoImage(file='bilde.gif')
attela_konteineris = tk.Label(root, image=attels_objekts)
attela_konteineris.image = attels_objekts
attela_konteineris.pack(pady=20)



root.mainloop()

