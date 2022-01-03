from tkinter import *
from time import sleep
from tkinter import messagebox

class Cron:
    
    def __init__(self, master):

        def st():
            horas = Horas.get()
            minut = Minut.get()
            second = Second.get()
            while Pause.get() == 'Pause':
                if horas < 10:
                    if minut < 10:
                        if second < 10:
                            ress.set(f"0{horas}:0{minut}:0{second}")
                        else:
                            ress.set(f"0{horas}:0{minut}:{second}")
                    else:
                        ress.set(f"0{horas}:{minut}:{second}")
                else:
                    ress.set(f"{horas}:{minut}:{second}")
                Second.set(second)
                second += 1
                if second == 60:
                    second = 0
                    minut += 1
                if minut == 60:
                    minut = 0
                    horas += 1
                Minut.set(minut)
                Horas.set(horas)
                sleep(1)                
                janela.update()


        def bt1_clk():
            Second.set(0)
            Minut.set(0)
            Horas.set(0)
            Pause.set('Pause')
            messagebox.showwarning(title=f"{'‼‼‼'*5} ATENÇÃO {'‼‼‼'*5}" ,message="Antes de fechar esta janela precione o botão STOP")
            st()
            

        def b2_clk():
            if Pause.get() == 'Pause':
                Pause.set('Paused')
                KeyboardInterrupt
            elif Pause.get() == 'Paused':
                Pause.set('Pause')
                st()

        def b3_clk():
            Pause.set('Paused')
            ress.set('')
            KeyboardInterrupt
            KeyboardInterrupt

        self.frm = master

        ress = StringVar()
        Pause = StringVar()
        Second = IntVar()
        Minut = IntVar()
        Horas = IntVar()

        Label(self.frm, textvariable=ress, font=('arial', 26, 'bold'), fg='black', pady=25).grid(row=0, columnspan=5)
        bt1 = Button(
            self.frm, font=('arial', 12, 'bold'), command=bt1_clk, text='Start', fg='white', bg='red', borderwidth=2,relief='ridge', width=15).grid(column=0, row=1)
        bt2 = Button(
            self.frm, font=('arial', 12, 'bold'), command=b2_clk, textvariable=Pause, fg='white', bg='red', borderwidth=2,relief='ridge', width=15).grid(column=2, row=1)
        bt3 = Button(
            self.frm, font=('arial', 12, 'bold'), command=b3_clk, text='Stop', fg='white', bg='red', borderwidth=2,relief='ridge', width=15).grid(column=4, row=1)
    
janela = Tk()
Cron(janela)

janela.title('CRONOMETRO')

janela.resizable(width=False, height=False)

janela.mainloop()