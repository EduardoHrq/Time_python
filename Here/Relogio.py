
import tkinter as tk

import datetime

class TelaPrincipal:
    def __init__(self, master):
        self.nossaTela = master
        self.lblRelogio = tk.Label(
            self.nossaTela, font=('Arial-Black',26, 'bold'), fg='Black')
        self.lblRelogio.pack(pady=30, padx=75)
        self.alteracao()

    def alteracao(self):
        now = datetime.datetime.now()

        self.lblRelogio['text'] = now.strftime('%H:%M:%S')
        self.nossaTela.after(1000, self.alteracao)




janela = tk.Tk()
TelaPrincipal(janela)
janela.resizable(width=False, height=False)
janela.mainloop()


