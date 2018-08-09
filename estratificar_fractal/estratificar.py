from crivios import *
from matplotlib.pyplot import plot, show, axis, legend, grid, annotate, subplot, title, scatter, xlabel, ylabel, colorbar


def plt(Xn,Yn,Xnpri,Ynpri,inicio=0,num=False):
    '''Construct the scatter plot of the "n" and "npri" graphics. The graph "n" below the graph "npri" will be constructed.
     
    Args:

    Xn (List) X coordinate of the points of the graph "n"
    Yn (List) Y coordinate of two points in the "n"
    Xnpri (List) X coordinate of the graph points "npri"
    Ynpri (List) Y coordinate of the graph "npri"
    inicio (Int) Start of the enumeration of the points of the graph "n". Default is 0. 
    num (Bool) Boolean variable that indicates whether the point digits should appear in the graph. Default is False, not shows the numbers

    Return:

    Returns the scatter plot of n and npri points.
    '''
    if num:
        for i in xrange(len(Xn)):
            annotate(str(i+inicio),xy=(Xn[i],Yn[i]))
    plot(Xn,Yn,'.',color='black')
    plot(Xnpri,Ynpri,',',color='red')
    axis('equal')
    show()
    return

def plt2(x,y,m='y',cmap='viridis',titulo='',xtex='',ytex='',num=False):
    '''Returns the scatter plot of points in ordered pairs X and Y.
    Args:

    X (list) X coordinate of the points to be placed on the graph
    Y (list) Coordinate y two points that will be put on graph
    m (list) List of values ​​that serves as the basis for the gradient, Default is Y
    cmap (str) colormap used in the plot, read more at: matplotlib.org/users/colormaps.html. Default is 'viridis'
    titulo (str) Descriptive text that will appear in the title. Default is empry text ''
    xtex (str) Descriptive text that will appear on the x-axis. Default is empry text ''
    ytex (str) Descriptive text that will appear on the y-axis. Default is empry text ''
    num (Bool) Boolean variable that indicates whether the point digits should appear in the graph. Default is False, not shows the numbers

       
    Return:

    Returns the scatter plot of points.
    '''
    if m=='y':
        m=y
    if num:
        for i in xrange(len(x)):
            annotate(str(i),xy=(x[i],y[i]))
    scatter(x,y,c=m,marker='.',cmap=cmap)
    xlabel(xtex)
    ylabel(ytex)
    title(titulo)
    colorbar()
    show()
    return

def fractal(N_lados,nivel,lista='primos',num=False,inicio=0,salvar=False,retornar=False):
    '''
    It makes the visual panel developed by Isaac Victor Silva Rodrigues, Lúcia Maria dos Santos Pinto and Juscelino Bezerra dos Santos the project in Escola Nacional de Ciências Estatísticas
    The panel is based on the Ulam Spiral to make a visual representation of sequences of integers. Read more about: en.wikipedia.org/wiki/Ulam_spiral
    Such a representation is made using n-gon fractals as a template. Read more about: http://ecademy.agnesscott.edu/~lriddle/ifs/pentagon/sierngon.htm
    Finally, the fractal n-gon is built up to a specific level, in the representation we have only the bicuspid of the polygons of this specific level.


    Args:

    N_lados (int) Number of sides of the base polygon for the fractal ngon
    level (int) Level of construction of the fractal Ngon
    list (List) Number sequence you want to highlight. Default is prime list before
    num (Bool) Boolean variable that indicates whether the point digits should appear in the graph. Default is False, not shows the numbers
    inicio (int) Start of the enumeration used in the fractal points. Default is 0
    salvar (Bool) If you want to save the sorted ordered pairs. The program will save to a text file .txt, where the coordinates appear in column format.
    retornar (Bool) If you want to return the result of the calculation of the baricenters out of the function


    Return:

    Two possible outputs are:
    plot of the visual panel or x and y values of coordenates of barycentres
    '''
    t_pontos=N_lados**nivel
    fator_s=0.5/sum([cos(2*pi*k/N_lados) for k in xrange(N_lados/4+1)])
    if N_lados in (2,4):
        fator_s=1/3.0           
    angulo=pi/2
    angulos=[]
    delta=2*pi/N_lados
    Raio=fator_s**nivel
    Raios=[]    
    for i in xrange(N_lados):
        angulos.append((cos(angulo+i*delta),sin(angulo+i*delta)))
    angulos=tuple(angulos)
    X=[0.0]
    Y=[0.0]
    for i in xrange(nivel):
        for j in xrange(N_lados**i):
            x,y=X[j],Y[j]
            for k in xrange(N_lados):
                X.append(x+Raio*angulos[k][0])
                Y.append(y+Raio*angulos[k][1])
        X=X[N_lados**i:]
        Y=Y[N_lados**i:]
        Raio/=fator_s
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
            if i<t_pontos:
                Xpri.append(X[i-inicio])
                Ypri.append(Y[i-inicio])
    if num:
        plt(X,Y,Xpri,Ypri,inicio,num)
    else:
        plt(X,Y,Xpri,Ypri)
    return 

def pltpropor(base,nivel,sn,X=False,Y=False,lista="primos",pro=False,cmap='viridis',anotate=False,titulo=''):
    subnivel=nivel-sn
    if False in (X,Y): X,Y=fractal(base,subnivel,retornar=True)
    print len(X)
    if lista=="primos": lista=atkin(base**nivel)
    if not pro: lista=estratos_com_elementos(base,nivel,sn,lista)
    if pro and len(lista)>base**subnivel:
        aux=[0]*(6**subnivel)
        for i in xrange(len(lista)):
            aux[i%(6**subnivel)]+=lista[i]
    if anotate:
        for i in xrange(len(X)):
            annotate(str(i),xy=(X[i],Y[i]))

    title(titulo)
    print len(lista),len(X)
    scatter(X,Y,c=lista,marker=".",cmap=cmap) 
    colorbar()
    axis("equal")
    show()
    return



