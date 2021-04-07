import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from math import *
from numpy import arange

janela = tk.Tk()

janela.state("zoomed")
janela.title("Fourier")
janela.update()

janelaHeight = janela.winfo_height()
janelaWidth = janela.winfo_width()

frame_grafico = tk.Frame(janela, bd=5, relief='ridge')
frame_grafico.pack()

fi = Figure(figsize=(7.5, 4), dpi=100, edgecolor='black')

canvas = FigureCanvasTkAgg(fi, master=frame_grafico)
canvas.draw()
canvas.get_tk_widget().pack(side='top', fill='both', expand=1)
canvas._tkcanvas.pack(side='top', fill='both', expand=1)

ax = fi.add_subplot(1, 1, 1)



def conta():
    global linha
    x = [i for i in arange(-4, 5, 0.1)]
    y = [0.0] * len(x)
    ini = int(text.get())
    fim = int(text2.get())
    fun = func.get()
    fun1 = fun.replace("N", "(i+1)")
    fun2 = fun1.replace('x', '*x[val]')
    fun3 = fun2.replace("^","**")
    for val in range(0, len(x)):
        for i in range(ini-1, fim ):
            y[val] += eval(fun3)
    ax.clear()
    ax.spines['left'].set_position(('data', 0.0))
    ax.spines['bottom'].set_position(('data', 0.0))
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.set_ylim([-3,3])
    linha, = ax.plot(x, y)
    fi.canvas.draw_idle()


frame_esquerda = tk.Frame(janela)
frame_esquerda.pack(side='left', fill='both', expand=True)


somato = tk.LabelFrame(frame_esquerda, relief='ridge', bd=5, width=30, height=5, text="Somatório")
frame_esquerda.update()
somato.place(x=frame_esquerda.winfo_width() * 0.22, y=20)

text = tk.Entry(somato)
text.grid(row=1, column=1)
text.insert(0, '1')
btn = tk.Button(somato, width=8, text='Valor Inicial')
btn.grid(row=1, column=2)

text2 = tk.Entry(somato)
text2.grid(row=3, column=1)
text2.insert(0, '10')
btn2 = tk.Button(somato, width=8, text='Valor Final')
btn2.grid(row=3, column=2)

btn.config(command=conta)
btn2.config(command=conta)

funclab = tk.LabelFrame(frame_esquerda, relief='ridge', bd=5, height=5, text="Função")
funclab.place(x=frame_esquerda.winfo_width() * 0.375, y=20)

func = tk.Entry(funclab, width=100)
func.pack()

grap = tk.Button(funclab, width=10,text="Plotar", command=conta)
grap.pack()

janela.minsize(janelaHeight, janelaWidth)
janela.mainloop()
