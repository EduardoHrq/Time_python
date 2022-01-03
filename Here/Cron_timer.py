from tkinter import *
from time import sleep
from tkinter import messagebox
from tkinter import font

class Cron:
    
    def __init__(self, master):

        def cm(horas, minut, second):
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

        def tm(horas, minut, second):
            while Pause.get() == 'Pause':
                if horas == 0 and minut == 0 and second == -1:
                    ress.set("00:00:00")    
                    messagebox.showinfo(message="TIMER FINALIZADO")
                    break
                if horas < 10:
                    if minut < 10:
                        if second < 10:
                            ress.set(f"▼  0{horas}:0{minut}:0{second}  ▼")
                        else:
                            ress.set(f"▼  0{horas}:0{minut}:{second}  ▼")
                    else:
                        ress.set(f"▼  0{horas}:{minut}:{second}  ▼")
                else:
                    ress.set(f"▼  {horas}:{minut}:{second}  ▼")
                Second.set(second)
                if second == 0 and minut > 0:
                    second = 60
                    minut -= 1
                if minut == 0 and horas > 0:
                    minut = 59
                    horas -= 1
                    second = 60os.system('clear')
                Horas.set(horas)
                sleep(1)                               
                janela.update()

        def bt1_clk():
            messagebox.showwarning(title=f"{'‼‼‼'*5} ATENÇÃO {'‼‼‼'*5}" ,message="Antes de fechar esta janela precione o botão STOP")
            if sc.get() > 0 or mt.get() > 0 or hr.get() > 0:
                Second.set(sc.get())
                Minut.set(mt.get())
                Horas.set(hr.get())
                Pause.set('Pause')
                tm(hr.get(), mt.get(), sc.get())
            else:
                Second.set(0)
                Minut.set(0)
                Horas.set(0)
                Pause.set('Pause')
                cm(Horas.get(), Minut.get(), Second.get())
            
        def b2_clk():
            if Pause.get() == 'Pause':
                Pause.set('Paused')
                KeyboardInterrupt
            elif Pause.get() == 'Paused':
                Pause.set('Pause')
                if sc.get() > 0 or mt.get() > 0 or hr.get() > 0:
                    tm(Horas.get(), Minut.get(), Second.get())
                else:
                    cm(Horas.get(), Minut.get(), Second.get())

        def b3_clk():
            Pause.set('Paused')
            ress.set('')
            KeyboardInterrupt
            KeyboardInterrupt  

        def slv():

            janela2 = Tk()

            janela2.title("SAVES")
    
            cont = IntVar()

            salve = StringVar()

            def lbl():
                

                if Horas.get() < 10:
                    if Minut.get() < 10:
                        if Second.get() < 10:
                            salve.set(f"►  0{Horas.get()}:0{Minut.get()}:0{Second.get()}")
                        else:
                            salve.set(f"►  0{Horas.get()}:0{Minut.get()}:{Second.get()}")
                    else:
                        salve.set(f"►  0{Horas.get()}:{Minut.get()}:{Second.get()}")
                else:
                    salve.set(f"►  {Horas.get()}:{Minut.get()}:{Second.get()}")


                janela2.update()
                
            
            Label(janela2, text=salve, font=("arial", 12, "bold"), fg="black").grid(row=1)
            
            Button(janela2, command=lbl, text="▀▌").grid(row=0)

            janela2.mainloop()


       

        self.frm = master

        ress = StringVar()
        Pause = StringVar()
        Second = IntVar()
        Minut = IntVar()
        Horas = IntVar()

        hr = IntVar()
        mt = IntVar()
        sc = IntVar()

        fr = Frame(self.frm).grid(row=0,column=2)

        Label(fr, text="Timer:", font=("arial", 14, "bold"), fg="black", pady=7).grid(row=0, columnspan=2)
        Entry(fr, font=("arial", 12, "bold"), textvariable=hr, fg="black", width=8).grid(row=0, columnspan=4)
        Entry(fr, font=("arial", 12, "bold"), textvariable=mt, fg="black", width=8).grid(row=0, column=2)
        Entry(fr, font=("arial", 12, "bold"), textvariable=sc, fg="black", width=8).grid(row=0, column=2, columnspan=4)

        Button(fr, text="▀▌", font=("arial", 12, "bold"), bg="gray", command=slv).place(y=5, x=435)

        Label(self.frm, textvariable=ress, font=('arial', 26, 'bold'), fg='black', pady=25).grid(row=1, columnspan=5)
        Button(
            self.frm, font=('arial', 12, 'bold'), command=bt1_clk, text='Start', fg='white', bg='red', borderwidth=2,relief='ridge', width=15).grid(column=0, row=2)
        Button(
            self.frm, font=('arial', 12, 'bold'), command=b2_clk, textvariable=Pause, fg='white', bg='red', borderwidth=2,relief='ridge', width=15).grid(column=2, row=2)
        Button(
            self.frm, font=('arial', 12, 'bold'), command=b3_clk, text='Stop', fg='white', bg='red', borderwidth=2,relief='ridge', width=15).grid(column=4, row=2)
        messagebox.showinfo(
        message=f'''{"‼‼"*12} INTRUÇÕES {"‼‼"*12}

► Caso for usar o timer:
    • defina todos os valores e pressione "START", não os deixe em branco

► Caso queira usar o cronometro:
    • defina todos os valores do timer como "0" e pressione "START"
{"_"*62}

‼ Antes de fechar a janela pressione "STOP" para que limpe a janela e interropa a ações
        ''')  

janela = Tk()
Cron(janela)

janela.title('CRONOMETRO')

janela.resizable(width=False, height=False)

janela.mainloop()