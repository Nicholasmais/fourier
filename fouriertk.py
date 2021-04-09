import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from math import *
from numpy import arange
from numpy import absolute
from sympy import sympify, latex

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
    neg = int(text3.get())
    pos=int(text4.get())
    x = [i for i in arange(-absolute(neg), pos, 0.1)]
    y = [0.0] * len(x)
    ini = int(text.get())
    fim = int(text2.get())
    fun = func.get()
    fun1 = fun.replace("k", "(i+1)")
    fun2 = fun1.replace('x', 'x[val]')
    fun3 = fun2.replace("^","**")
    for val in range(0, len(x)):
        for i in range(ini-1, fim ):
            y[val] += eval(fun3)
    ax.clear()
    ax.spines['left'].set_position(('data', 0.0))
    ax.spines['bottom'].set_position(('data', 0.0))
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    negy = float(text5.get())
    posy=float(text6.get())
    ax.set_ylim([-absolute(negy),posy])
    linha, = ax.plot(x, y)
    fi.canvas.draw_idle()
    display()


def display():
    ini = int(text.get())
    fim = int(text2.get())
    tmptext = func.get()
    tmptext = latex(sympify(tmptext))
    tmptext = "$"+ " \sum_{{n={}}}^{{{}}}".format(ini,fim) + tmptext+"$"

    ex.clear()
    ex.text(0.3, 0.4, tmptext, fontsize = 20)
    fi2.canvas.draw_idle()


frame_esquerda = tk.Frame(janela)
frame_esquerda.pack(side='left', fill='both', expand=True)


somato = tk.LabelFrame(frame_esquerda, relief='ridge', bd=5, width=30, height=5, text="Somatório")
frame_esquerda.update()
somato.place(x=frame_esquerda.winfo_width() * 0.22, y=20)

text = tk.Entry(somato, width=12)
text.grid(row=1, column=1)
text.insert(0, '1')
btn = tk.Button(somato, width=15, text='Valor Inicial')
btn.grid(row=1, column=2)

text2 = tk.Entry(somato,width=12)
text2.grid(row=3, column=1)
text2.insert(0, '10')
btn2 = tk.Button(somato, width=15, text='Valor Final')
btn2.grid(row=3, column=2)

limites = tk.LabelFrame(frame_esquerda, relief='ridge', bd=5, width=30, height=5, text="Limite valores x")
frame_esquerda.update()
limites.place(x=frame_esquerda.winfo_width() * 0.22, y=100)

text3 = tk.Entry(limites,width=12)
text3.grid(row=1, column=1)
text3.insert(0, '-10')
btn3 = tk.Button(limites, width=15, text='Limite negativo')
btn3.grid(row=1, column=2)

text4 = tk.Entry(limites, width=12)
text4.grid(row=2, column=1)
text4.insert(0, '10')
btn4 = tk.Button(limites, width=15, text='Limite Positivo')
btn4.grid(row=2, column=2)

limitesy = tk.LabelFrame(frame_esquerda, relief='ridge', bd=5, width=30, height=5, text="Limite valores y")
frame_esquerda.update()
limitesy.place(x=frame_esquerda.winfo_width() * 0.22, y=180)

text5 = tk.Entry(limitesy,width=12)
text5.grid(row=1, column=1)
text5.insert(0, '-3')
btn5 = tk.Button(limitesy, width=15, text='Limite negativo')
btn5.grid(row=1, column=2)

text6 = tk.Entry(limitesy, width=12)
text6.grid(row=2, column=1)
text6.insert(0, '3')
btn6 = tk.Button(limitesy, width=15, text='Limite Positivo')
btn6.grid(row=2, column=2)

btn.config(command=conta)
btn2.config(command=conta)
btn3.config(command=conta)
btn4.config(command=conta)
btn5.config(command=conta)
btn6.config(command=conta)


funclab = tk.LabelFrame(frame_esquerda, relief='ridge', bd=5, height=5, text="Função")
funclab.place(x=frame_esquerda.winfo_width() * 0.375, y=20)

texto = tk.StringVar()
func = tk.Entry(funclab, width=90, textvariable=texto)
func.pack()
grap = tk.Button(funclab, width=10,text="Plotar", command=conta)
grap.pack()


exfram = tk.LabelFrame(frame_esquerda, relief='ridge',bd=5,height=155,width=555,text="Display")
exfram.place(x=frame_esquerda.winfo_width() * 0.375, y=99)

fi2 = Figure(figsize=(5.45, 1.3), dpi=100, edgecolor='black')

canvas2 = FigureCanvasTkAgg(fi2, master=exfram)
canvas2._tkcanvas.pack()

ex = fi2.add_subplot(111)
ex.get_xaxis().set_visible(False)
ex.get_yaxis().set_visible(False)


ntb = NavigationToolbar2Tk(canvas, frame_esquerda)
ntb.pack()

janela.minsize(janelaHeight, janelaWidth)
janela.mainloop()
