
import tkinter as tk
from tkinter import messagebox
import math

root = tk.Tk()
root.geometry("550x520")
root.title("Kustības paātrinājuma kalkulātors")

# Izveidots Logs, loga izmērs, kā arī loga virsraksts

tk.Label(root, text="Ieraksti sākuma ātrumu (m/s):", font=("Arial", 11)).pack(pady=5)
ievade1 = tk.Entry(root, width=10)
ievade1.pack(pady=5)

tk.Label(root, text="Ieraksti beigu ātrumu (m/s):", font=("Arial", 11)).pack(pady=5)
ievade2 = tk.Entry(root, width=10)
ievade2.pack(pady=5)

tk.Label(root, text="Ieraksti kustības laiku (s):", font=("Arial", 11)).pack(pady=5)
ievade3 = tk.Entry(root, width=10)
ievade3.pack(pady=5)

# Izveidoti ievadlauki, kuros lietotājs ievada savus skaitļus

def rezultats():
    try:
        sa = float(ievade1.get())
        ba = float(ievade2.get())
        la = float(ievade3.get())

        if la == 0:
            messagebox.showerror("Kļūda", "Laiks nevar būt 0!")

        sum = math.fabs((ba - sa) / la)
        rezultata_teksts.config(text="Paātrinājums: " + str(sum) + " m/s²")

    except ValueError:
        messagebox.showerror("Kļūda", "Nav ievadīts skaitlis!")

# Funkcija, kura aprēķina rezultātu pec formulas
# Iekļauta arī kļūdu izsniegšana try/except, priekš Laiks = 0, vai ja skaitļi nav ievadīti vai ievadīts burts
# Matemātiska funkcija math.fabs() ir funkcija, kura rezultātu vienmēr parādis kā pozitīvu skaitli, kaut tas ir negatīvs

rezultata_poga = tk.Button(root, text="Aprēķināt", command=rezultats,
                           bg="#0FE907", font=("Arial", 11, "bold"))
rezultata_poga.pack(pady=10)
rezultata_teksts = tk.Label(root, text="Paātrinājums: ", font=("Arial", 12))
rezultata_teksts.pack(pady=5)

# Poga un teksts priekš aprēķina parādīšanas, poga izpilda funkciju

attels_objekts = tk.PhotoImage(file='bilde.gif')
attela_konteineris = tk.Label(root, image=attels_objekts)
attela_konteineris.image = attels_objekts
attela_konteineris.pack(pady=20)

# Ievietots attēls no www.uzdevumi.lv/p/fizika-skola2030/8-klase/ka-kermeni-kustas-79540/re-3dea7b00-8a47-434c-9a4c-bc854a035bdb

root.mainloop()
