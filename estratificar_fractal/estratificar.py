from crivios import *
import matplotlib
from matplotlib import colors as mcolors
matplotlib.use('TkAgg')
from matplotlib.pyplot import *
from matplotlib.patches import RegularPolygon
from matplotlib.collections import PatchCollection
from mpldatacursor import datacursor
import os
import math 

def plt(Xn,Yn,Xnpri,Ynpri,inicio=0,num=False,hover=False,poli=[False],cor_conj=(1,0,0),cor_fund=(0,0,0)):
    '''Construct the scatter plot of the "n" and "npri" graphics. The graph "n" below the graph "npri" will be constructed.
 
    Args:

    Xn (List) X coordinate of the points of the graph "n"
    Yn (List) Y coordinate of two points in the "n"
    Xnpri (List) X coordinate of the graph points "npri"
    Ynpri (List) Y coordinate of the graph "npri"
    inicio (Int) Start of the enumeration of the points of the graph "n". Default is 0. 
    num (Bool) Boolean variable that indicates whether the point digits should appear in the graph. Default is False, not shows the numbers
    poli (list) Information of poligonos, poli=[Bool,Number of sides, distance between barycenter and vetex], if poli[0]=True program will try draw a poligon.
    Return:
    Returns the scatter plot of n and npri points.
    '''
    fig,ax=subplots()
    fig.tight_layout()
    if (type(Xn),type(Yn),type(Xnpri),type(Ynpri))!=tuple([type(array([]))]*4):
        Xn=array(Xn)
        Yn=array(Yn)
        Xnpri=array(Xnpri)
        Ynpri=array(Ynpri)
    if poli[0]: 
        poligonos=[]
        polipri=[]
        rpoli=poli[2]
        N_lados=poli[1]
        for i in xrange(len(Xn)):
            poligonos.append(RegularPolygon((Xn[i],Yn[i]),N_lados,rpoli))
        for i in xrange(len(Xnpri)):
            polipri.append(RegularPolygon((Xnpri[i],Ynpri[i]),N_lados,rpoli))
        ax.add_collection(PatchCollection(poligonos,facecolor=cor_fund))
        ax.add_collection(PatchCollection(polipri,facecolor=cor_conj))
    else:
        PLOT=plot(Xn,Yn,'.',markerfacecolor=cor_fund,markeredgecolor=cor_fund)
        PLOT2=plot(Xnpri,Ynpri,'.',markerfacecolor=cor_conj,markeredgecolor=cor_conj)
    axis('equal')
    if num:
        cor=[['black','center','top'],['white','center','center']]
        cor=cor[poli[0]]
        for i in xrange(len(Xn)):
            annotate(str(i+inicio),xy=(Xn[i],Yn[i]),color=cor[0],ha=cor[1], va=cor[2],fontweight='bold')
    if hover:
        def numeros(**kwargs):
            dist =abs(Xn - kwargs['x'])+abs((Yn - kwargs['y']))
            i = dist.argmin()
            text=u"Número: "+ str(i+inicio)
            return text
        datacursor(hover=True, formatter=numeros)
    show()
    return

def plt2(x,y,m='y',cmap='viridis',titulo='',xtex='',ytex='',inicio=0,num=False):
    '''Returns the scatter plot of points in ordered pairs X and Y.
    Args:

    X (list) X coordinate of the points to be placed on the graph
    Y (list) Coordinate y two points that will be put on graph
    m (list) List of values ​​that serves as the basis for the gradient, Default is Y
    cmap (str) colormap used in the plot, read more at: matplotlib.org/users/colormaps.html. Default is 'viridis'
    titulo (str) Descriptive text that will appear in the title. Default is empry text ''
    xtex (str) Descriptive text that will appear on the x-axis. Default is empry text ''
    inicio (Int) Start of the enumeration of the points of the graph "n". Default is 0. 
    ytex (str) Descriptive text that will appear on the y-axis. Default is empry text ''
    num (Bool) Boolean variable that indicates whether the point digits should appear in the graph. Default is False, not shows the numbers

       
    Return:

    Returns the scatter plot of points.
    '''
    if m=='y':
        m=y
    if num:
        for i in xrange(len(x)):
            annotate(str(i+inicio),xy=(x[i],y[i]))
    scatter(x,y,c=m,marker='.',cmap=cmap)
    xlabel(xtex)
    ylabel(ytex)
    title(titulo)
    colorbar()
    show()
    return

def fractal(N_lados,nivel,lista=[],num=False,hover=False,inicio=0,salvar=False,retornar=False,poligonos=False,cor_conj="#FF0000",cor_fund="#000000"):
    '''
    It makes the visual panel developed by Isaac Victor Silva Rodrigues, Lúcia Maria dos Santos Pinto and Juscelino Bezerra dos Santos the project in Escola Nacional de Ciências Estatísticas
    The panel is based on the Ulam Spiral to make a visual representation of sequences of integers. Read more about: en.wikipedia.org/wiki/Ulam_spiral
    Such a representation is made using n-gon fractals as a template. Read more about: http://ecademy.agnesscott.edu/~lriddle/ifs/pentagon/sierngon.htm
    Finally, the fractal n-gon is built up to a specific level, in the representation we have only the bicuspid of the polygons of this specific level.


    Args:

    N_lados (int) Number of sides of the base polygon for the fractal ngon
    level (int) Level of construction of the fractal Ngon
    list (List) Number sequence you want to highlight  with red.
    num (Bool) Boolean variable that indicates whether the point digits should appear in the graph. Default is False, not shows the numbers
    inicio (int) Start of the enumeration used in the fractal points. Default is 0
    salvar (Bool) If you want to save the sorted ordered pairs. The program will save to a text file .txt, where the coordinates appear in column format.
    retornar (Bool) If you want to return the result of the calculation of the baricenters out of the function
    poligonos (Bool) If user want to draw the poligons of last level on plot

    Return:

    Some possibles  outputs are:
    plot of the visual panel or 
    x and y values of coordenates of barycentres of last construction level  
    '''
    t_pontos=N_lados**nivel
    TOTAL=t_pontos+inicio
    fator_s=0.5/sum([math.cos(2*pi*k/N_lados) for k in xrange(N_lados/4+1)])
    if N_lados in (2,4):
        fator_s=1/3.0           
    angulo=pi/2
    angulos=[]
    delta=2*pi/N_lados
    Raio=1
    Raios=[]    
    for i in xrange(N_lados):
        angulos.append((math.cos(angulo+i*delta),math.sin(angulo+i*delta)))
    angulos=tuple(angulos)
    X=[0.0]
    Y=[0.0]
    for i in xrange(nivel):
        for k in xrange(N_lados):
            for j in xrange(N_lados**i):
                X.append(X[j]+Raio*angulos[k][0])
                Y.append(Y[j]+Raio*angulos[k][1])
        X=X[N_lados**i:]
        Y=Y[N_lados**i:]
        Raio*=fator_s
        Raios.append(Raio)
    if retornar:
        return (array(X),array(Y))
    if salvar:
        if not os.path.exists('salvos'):
            os.makedirs('salvos')
        arq=open('salvos/'+'pontos enumerados do fractal de '+str(N_lados)+' lados ate o nivel ' +str(nivel)+'.txt','w')
        arq.write("X\tY")
        for i in xrange(len(X)):
            arq.write('\n'+str(X[i])+'\t'+str(Y[i]))
        arq.close()
    Xpri=[]
    Ypri=[]
    if type(lista) in (type(set([])),type([])):
        for i in lista:
            if inicio<=i<TOTAL:
                I=i-inicio
                Xpri.append(X[I])
                Ypri.append(Y[I])
    X,Y=array(X),array(Y)
    Xpri,Ypri=array(Xpri),array(Ypri)
    if nivel!=0: ak=Raios[0]/(1-fator_s)-sum(Raios[:-1])
    else: ak=Raio
    plt(X,Y,Xpri,Ypri,inicio,num,hover,poli=[poligonos,N_lados,ak],cor_conj=cor_conj,cor_fund=cor_fund)
    del X,Y,Xpri,Ypri,inicio,num,hover,Raios,lista
    return 



def fractal_fatorial(N,lista=[],num=False,hover=False,inicio=0,salvar=False,retornar=False):
    R=1.0
    TOTAL=math.factorial(N)
    X=[0.0]
    Y=[0.0]
    for i in xrange(2,N+1):
        L=i
        fator=0.5/sum([math.cos(2*pi*k/L) for k in xrange(L/4+1)])
        if i in (2,4):
            fator=1/3.0
        R*=fator
        delta=2*pi/L
        angulos=[]
        angulo=pi/2
        if L==2:
            angulo=pi
        for k in xrange(L):
            angulos.append((math.cos(angulo+k*delta),math.sin(angulo+k*delta)))
        Xn,Yn=[],[]
        for k in xrange(L):
            for j in xrange(len(X)):
                    Xn.append(X[j]+R*angulos[k][0])
                    Yn.append(Y[j]+R*angulos[k][1])
        X=Xn[:]
        Y=Yn[:]
    Xpri=[]
    Ypri=[]
    if type(lista) in (type(set([])),type([])):
        for i in lista:
            if inicio<=i<TOTAL:
                I=i-inicio
                Xpri.append(X[I])
                Ypri.append(Y[I])
    X,Y=array(X),array(Y)
    Xpri,Ypri=array(Xpri),array(Ypri)
    plt(X,Y,Xpri,Ypri,inicio,num,hover)
    return 

def pltpropor(base,nivel,sn,X=False,Y=False,lista="primos",pro=False,Densidade=False,cmap='viridis',anotate=False,titulo='',poligonos=False,hover=True):
    subnivel=nivel-sn
    if False in (X,Y): X,Y=fractal(base,subnivel,retornar=True)
    if lista=="primos": lista=atkin(base**nivel-1)
    if not pro: lista=estratos_com_elementos(base,nivel,sn,lista)
    if pro and len(lista)>base**subnivel:
        aux=[0]*(base**subnivel)
        for i in xrange(len(lista)):
            aux[i%(base**subnivel)]+=lista[i]
    if Densidade:
        Soma_total_lista=float(sum(lista))
        lista=[i/Soma_total_lista for i in lista]
    fig,ax=subplots()
    X,Y,lista=array(X),array(Y),array(lista)
    if anotate:
        for i in xrange(len(X)):
            annotate(str(i),xy=(X[i],Y[i]))
    if poligonos:
        fator_s=0.5/sum([math.cos(2*pi*k/base) for k in xrange(base/4+1)])
        if base in (2,4): fator_s=1/3.0
        if subnivel!=0: 
            Raios=[fator_s**i for i in xrange(subnivel)]
            L=Raios[0]/(1-fator_s)- sum(Raios[:])
        else:
            L=1/(1-fator_s)
        poligonos=[RegularPolygon((X[i],Y[i]),base,L) for i in xrange(base**subnivel)]
        poligonos=PatchCollection(poligonos,array=lista,cmap=cmap)
        poligonos.set_clim([0, max(lista)])
        ax.add_collection(poligonos)
        fig.colorbar(poligonos,ax=ax)
    else:
        ax.scatter(X,Y,c=lista,marker=".",cmap=cmap,vmin=0,vmax=max(lista))
        fig.colorbar(scatter(X,Y,c=lista,marker=".",cmap=cmap,vmin=0,vmax=max(lista)),ax=ax) 
    if hover:
        subnivel2=nivel-subnivel
        def numeros(**kwargs):
            dist =abs(X - kwargs['x'])+abs((Y - kwargs['y']))
            i = dist.argmin()
            text=u"Números "+ str(i)+u" mod "+str(base**subnivel)+u" do fractal construido até o nível "+str(nivel)+"\n "+str(round(lista[i],5))+u'\n São:'+str(int(round(lista[i]*base**subnivel2)))+u' de '+str(base**subnivel2)+u' números.'
            text=unicode(text)
            return text
        datacursor(hover=True, formatter=numeros)
    axis("equal")
    show()
    return
