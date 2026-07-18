import tkinter as tk
from tkinter import messagebox

def celsius_para_fahrenheint():
    try:
        c = int(entrada1.get())
        f = (c * 9/5) + 32

        messagebox.showinfo(message=str(f))
    
    except Exception as e:
        messagebox.showerror("Erro!, " + f"{e}")

def fahrenheint_para_celsius():
    try:
        f = int(entrada2.get())
        c = (f - 32) * 5/9

        messagebox.showinfo(message=str(c))
    
    except Exception as f:
        messagebox.showerror("Erro!, " + f"{f}")


janela = tk.Tk()
janela.title("Conversor de celsius para fahrenheint")

tk.Label(janela, text="Escreva no campo abaixo uma temperatura em celsius, e eu, irei converter para fahrenheint.").pack()

entrada1 = tk.Entry(janela)
entrada1.pack()

tk.Button(janela, text="CONVERTER CELSIUS PARA FAHRENHEINT", command=celsius_para_fahrenheint).pack()

tk.Label(janela, text="Escreva no campo abaixo uma temperatura em fahrenheint, e eu, irei converter para celsius.").pack()

entrada2 = tk.Entry(janela)
entrada2.pack()

tk.Button(janela, text="CONVERTER FAHRENHEINT PARA CELSIUS", command=fahrenheint_para_celsius).pack()

janela.mainloop()
