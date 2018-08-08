from estratificar import *
import __builtin__
import pip
import Tkinter as tk
import ttk
import tkMessageBox
import tkFileDialog as tkFD
import sys
import os.path
from os import makedirs
import code


x=0
############################################################################################################################################################################################
############################################################################################################################################################################################


def openFile():
    filename = tkFD.askopenfilename()
    if filename!='':
        Ltlist['values']=funckeys+[filename]
        Ltlist.current(len(Ltlist['values'])-1)
        
    return

def gerar_propor():
    return

def gerar_fractal():
    N_lados=unicode(EtN_lados.get())
    if N_lados.isnumeric():
        N_lados=int(N_lados)
        nivel=unicode(Etnivel.get())
        if  nivel.isnumeric():
            nivel=int(nivel)
            lista=Ltlist.get()
            if lista in funcs.keys() or '.txt' in lista:
                if Ltcolenu.get()=='Sim':
                    colenu=True
                else:
                    colenu=False
                if '.txt' in lista:
                    lista=optxtseq(lista,colenu)
                else:
                    auxfu=lista
                    if  auxfu in funcs.keys():
                        fun=funcs[auxfu]+str(N_lados**nivel)+')'
                        lista=eval(fun)
            
            num,sv=False,False
            if 'Sim'==Ltnum.get():
                num=True
            if Ltsalvar.get()=='Sim':
                sv=True
            F=fractal(N_lados,nivel,lista,num,salvar=sv)
    return

def con():
    vars = globals().copy()
    vars.update(locals())
    shell = code.InteractiveConsole(vars)
    shell.interact()
    return


if __name__=='__main__':
    funcs= {'Primos': 'atkin(',
            'Primos de Sophie Germain': 'sophiegermain(',
            'Lucky Numbers': 'josephus(',
            'Primos Weak': 'primos_weak(',
            "Coprimos com 'L' ":'coprimos(N_lados,',
            'Fibonacci': 'fibonacci(',
            'Primos Strong': 'primos_strong(',
            'Primos Balanced':'primos_balanced('}

    funckeys=funcs.keys()
    funckeys.sort()

    #janela

    janela = tk.Tk()
    janela.geometry('600x200+100+100')



    choices2=['-----------------']+funckeys
    choices= [u'Não',u'Sim']



    janela.title("Estratificação Visual dos Números interios via Fractais de Sierpinski v0.1")

    #N DE LADOS
    LabN_lados=tk.Label(janela,text="Número de lados 'L' do fractal:",relief='ridge')
    LabN_lados.grid(row=1,column=1,sticky='E')

    EtN_lados=tk.Entry()
    EtN_lados.grid(row=1,column=2,sticky='W')

    #NIVEL
    Labnivel=tk.Label(janela,text=" Nível de construção do fractal: ",relief='ridge')
    Labnivel.grid(row=2,column=1,sticky='E')

    Etnivel=tk.Entry()
    Etnivel.grid(row=2,column=2,sticky='W')

    #LISTA DESEJADA
    Lablista=tk.Label(janela,text='Escolha o arquivo ou selecione um conjunto da lista: ',relief='ridge')
    Lablista.grid(row=3,column=1)

    Ltlist=ttk.Combobox(janela)
    Ltlist.grid(row=3,column=2,sticky='E')
    Ltlist['values']=choices2
    Ltlist.current(0)

    button = tk.Button(janela, text="Selecionar um arquvio", command=openFile)
    button.grid(row=3,column=3,sticky ='W')



    #COLUNA ENUEMRADA
    Labcolenu=tk.Label(janela,text="A lista possui uma coluna enuemrada?",relief='ridge')
    Labcolenu.grid(row=4,column=1,sticky='E')

    Ltcolenu = ttk.Combobox(janela)
    Ltcolenu['values']=choices
    Ltcolenu.current(0)
    Ltcolenu.grid(row=4,column=2,sticky='W')


    #ENUMERACAO
    Labnum=tk.Label(janela,text="Deseja que a enumeração apareça no resultado?",relief='ridge')
    Labnum.grid(row=5,column=1,sticky='E')

    Ltnum=ttk.Combobox(janela)
    Ltnum['values']=choices
    Ltnum.current(0)
    Ltnum.grid(row=5,column=2,sticky='W')


    #SALVAR
    Labsalvar=tk.Label(janela,text="Deseja salvar o resultado? ",relief='ridge')
    Labsalvar.grid(row=6,column=1,sticky='E')

    Ltsalvar = ttk.Combobox(janela)
    Ltsalvar['values']=choices
    Ltsalvar.current(0)
    Ltsalvar.grid(row=6,column=2,sticky='W')


    #BUTAO DE GERAR FRACTAL
    bt=tk.Button(janela,text='Gerar o fractal',command=gerar_fractal)
    bt.grid(row=7,column=2,sticky='W')


    bt=tk.Button(janela,text='Console Python 2.7.15',command=con)
    bt.grid(row=1,column=3,sticky='W')

    janela.mainloop()

############################################################################################################################################################################################
############################################################################################################################################################################################

