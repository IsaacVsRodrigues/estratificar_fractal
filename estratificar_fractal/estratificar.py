from crivios import *
import numpy as np
from matplotlib.pyplot import plot, show, axis, legend, grid, annotate,subplots, subplot, title, scatter, xlabel, ylabel, colorbar
from matplotlib.patches import RegularPolygon
from matplotlib.collections import PatchCollection
from mpldatacursor import datacursor
import os


def plt(Xn,Yn,Xnpri,Ynpri,inicio=0,num=False,poli=[False]):
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
    Xn=np.array(Xn)
    Yn=np.array(Yn)
    if poli[0]:	
	    poligonos=[]
	    polipri=[]
	    rpoli=poli[2]
	    N_lados=poli[1]
	    for i in xrange(len(Xn)):
	        poligonos.append(RegularPolygon((Xn[i],Yn[i]),N_lados,rpoli))
	    for i in xrange(len(Xnpri)):
	    	polipri.append(RegularPolygon((Xnpri[i],Ynpri[i]),N_lados,rpoli))
	    ax.add_collection(PatchCollection(poligonos,color="black"))
	    ax.add_collection(PatchCollection(polipri,color="red"))
    else:
    	plot(Xn,Yn,'.',color='black')
    	plot(Xnpri,Ynpri,'.',color='red')
    axis('equal')
    if num:
        def numeros(**kwargs):
            dist =abs(Xn - kwargs['x'])+abs((Yn - kwargs['y']))
            i = dist.argmin()
            return str(i)
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

def fractal(N_lados,nivel,lista=[],num=False,inicio=0,salvar=False,retornar=False,poligonos=False):
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
    fator_s=0.5/sum([cos(2*pi*k/N_lados) for k in xrange(N_lados/4+1)])
    if N_lados in (2,4):
        fator_s=1/3.0           
    angulo=pi/2
    angulos=[]
    delta=2*pi/N_lados
    Raio=1
    Raios=[]    
    for i in xrange(N_lados):
        angulos.append((cos(angulo+i*delta),sin(angulo+i*delta)))
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
        return X,Y
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
    plt(X,Y,Xpri,Ypri,inicio,num,poli=[poligonos,N_lados,Raios[0]/(1-fator_s)-sum(Raios[:-1])])
    return 

def pltpropor(base,nivel,sn,X=False,Y=False,lista="primos",pro=False,cmap='viridis',anotate=False,titulo=''):
    subnivel=nivel-sn
    if False in (X,Y): X,Y=fractal(base,subnivel,retornar=True)
    if lista=="primos": lista=atkin(base**nivel-1)
    if not pro: lista=estratos_com_elementos(base,nivel,sn,lista)
    if pro and len(lista)>base**subnivel:
        aux=[0]*(6**subnivel)
        for i in xrange(len(lista)):
            aux[i%(6**subnivel)]+=lista[i]
    if anotate:
        for i in xrange(len(X)):
            annotate(str(i),xy=(X[i],Y[i]))

    title(titulo)
    scatter(X,Y,c=lista,marker=".",cmap=cmap) 
    colorbar()
    axis("equal")
    show()
    return
