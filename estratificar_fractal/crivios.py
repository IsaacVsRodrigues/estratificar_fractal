from numpy import *
from itertools import  *
from sets import *
import sys
from ctypes import *
import math 
dir(sys)
maximointeiro=sys.maxint



def optxtseq(n,enu=False,real=False,*args,**kwargs):
     '''The function opens a .txt file and collects only the numbers. For ease of reading, any non-numeric character is considered a separator.
     Here are some sequences detectable types witch u can read in .txt
     Examples:
     Either of the examples below will return the list = [1,2,2,4,8,6,7]
     
     1 2 2 4 8 6 7
     or

     1a2a2.4,8, 6,7
     or
     1
     2
     2
     4
     8
     6
     7
     or

     1 2 2 4
     8 6
     7
     There are many ways to do these sequences, because the program looks only for integers, any other type of character is considered separator.
     
     If the first column of the file is just an enumeration of the elements of the sequence that we should ignore, this must be said in args.

     Args:
          n     (str)          Is string of archive location on ur computer. 
     enu  (bool)    Is to specify whether the first column of the file should be skipped in reading. Default is False for not in

     Return:
     lista     (list)    List with the numbers identified in the file
     '''
     vetaux=set([str(i) for i in xrange(10)]+[[],[",","."]][real])
     x=open(n,'r')
     linhas=x.readlines()
     s=''
     lista=[]
     linha=''.join(linhas)
     if not enu:
          for e in linha:
               if e in vetaux:
                    s+=e
               elif s!='':
                    lista.append(int(s))
                    s=''
     else:
          ini=int(linha[0])
          linha=linha[1:]
          k=0
          for e in linha:
               if e in vetaux:
                    s+=e
               elif s!='':
                    if k==0:
                         lista.append(int(s))
                         s=''
                    elif int(s)==ini+1:
                         ini=ini+1
                         k=0
                         s=''
                    if e=='\n':
                         k=1
     if s!='':
          lista.append(int(s))
     return lista

def test(n):
    '''Check whether n is prime or not:

     Args:
     n (int) int for check
     
     Return:
     
     tex (bool)  Boolean decision if n is prime(True) or no(False)'''
    if n==1:
         return False
    s=int(math.sqrt(n))
    k=1
    tex=False
    while k<s:
         k+=1
         if n%k==0 : return tex
    tex=True
    
    return tex

def atkin(nmax,*args,**kwargs):
    '''Return result of Sieve of Atkin for make list of primes. Read more about: en.wikipedia.org/wiki/Sieve_of_Atkin
     Exemple:

     atkin(29)
     [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

     Args:
     nmax (int) the program will return prime numbers between 0 and nmax(include nmax, if nmax is prime
     
     Return:
     
     primos (list) list of prime numbers p, like 0<=p<=nmax
     '''
    if nmax<2:
        return []
    elif nmax==2:
        return [2]
    elif nmax==3:
        return [2,3]
    else:
        aux=(c_bool*(nmax+1))()
        lim=int(math.sqrt(nmax))+1
        for x in xrange(1, lim):
            for y in xrange(1, lim):
                x3=3*x**2
                y2=y**2
                n = (2*x)**2 + y2
                if (n <= nmax) and n % 12 in (1,5):
                    aux[n] = not aux[n]
                n = x3 + y2
                if (n <= nmax) and (n % 12 == 7):
                    aux[n] = not aux[n]
                n = x3 - y2
                if (n <= nmax) and (x > y) and (n % 12 == 11):
                    aux[n] = not aux[n]
        for n in xrange(5,lim):
            if aux[n]:
                k=n**2
                for ik in xrange(k,nmax+1,k):
                    aux[ik] = False
        primos = [2,3]+[i for i in xrange(5,nmax + 1) if aux[i]]
        return primos

def sundaram(nmax):
    ''' return Sieve of Sundaram result for a given nmax, this go to find all primes betwen 1 and 2*nmax+1'''
    if nmax<2:
        return []
    elif nmax==2:
        return [2]
    elif nmax==3:
        return [2,3]
    aux=(c_bool*(nmax+1))()
    #to find j limit solve i+j+2ij<nmax, 
    #to find i lim solve i<=(nmax-i)/(1+2*i) is condition existence for j. U shoudlbe find i=(nmax-i)/(1+2*i) 
    lim=(-1+math.sqrt(1+2*nmax))*0.5
    for i in xrange(1,int(round(lim))+1):
        for j in xrange(i,(nmax-i)/(1+2*i)+1):
            aux[i+j+2*i*j]=True
    aux[0]=True
    return [2] + [2*(i)+1 for i in xrange(nmax) if not aux[i]]


def erastotenes(L):
    ''' Return  Sieve of Erastotenes result, returs all primes betwen 0 and L(inclde L), read  more about: en.wikipedia.org/wiki/Sieve_of_Eratosthenes
     Exemple:

     erastotenes(29)
     [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
     or
     erastotenes(50)
     [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

     Args:

     L (int)  the program will return prime numbers between 0 and L(include L, if L is prime

     Return:

     x (list) list of primes'''
    if L<2:
        return []
    if L==2:
        return [2]
    if L==3:
        return [2,3]
    aux=range(2,L+1)
    primos=[]
    for i in xrange(int(math.sqrt(L+1))+1):
        w=aux[0]
        aux=filter(lambda aux: aux%w!=0,aux)
        primos.append(w)
    return primos+aux

def erastotenes2(L):
    ''' Return  Sieve of Erastotenes result, returs all primes betwen 0 and L(inclde L), read  more about: en.wikipedia.org/wiki/Sieve_of_Eratosthenes
     Exemple:
     
     erastotenes(29)
     [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
     or
     erastotenes(50)
     [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
     
     Args:
     
     L (int)  the program will return prime numbers between 0 and L(include L, if L is prime
     
     Return:
     
     x (list) list of primes'''
    if L<2:
        return []
    if L==2:
        return [2]
    if L==3:
        return [2,3]
    primos=range(2,L+1)
    for i in xrange(int(math.sqrt(L+1))+1):
        w=primos[i]
        primos=filter(lambda primos: primos%w!=0 or primos==w,primos)
    return primos

def josephus(L):
    '''return result of The Sieve of Josephus Flavius: Read more about en.wikipedia.org/wiki/Lucky_number

    Args:
    L (int) limit for sieve

    Return:

    s_numbero (list) result of Sieve resultx'''
    i=1
    s_numero=range(1,L+1,2)
    while i<len(s_numero):
        del(s_numero[s_numero[i] - 1::s_numero[i]])
        i+=1
    return s_numero

def gcd(x,y):
    '''Program will return greatest common divisor between x and y, read more about: en.wikipedia.org/wiki/Greatest_common_divisor
     Program use Euclidean algorithm, u can read more here: en.wikipedia.org/wiki/Euclidean_algorithm
     
     Args:
     x (int) number for comparation
     y (int) number for comparation

     Return: x (int) '''
    if(y*x!=0):
        if y>x: (y,x)=(x,y)
        while y>0: (x,y)=(y,x%y)
    return x

def primos_par_impar(n,par=True,impar=True,primos='atkin'):
    resultado=dict()
    if primos=='atkin':
        primos=set(atkin(n))
    aux=[]
    for i in primos:
        if sum(int(k) for k in str(i))%2==1:
            aux.append(i)
    aux=set(aux)
    if par:
        resultado['par']=primos-aux
    if impar:
        resultado['impar']=aux
    return resultado

def factor(n,primos='atkin'):
    '''Returns n decomposed into prime factors :
     Args:
     n (int) number for decomposed
     primos (list) list of prime numbers less then n,  if no list is provided the program will use the atkin function

     Exemple:

     factor(30)
     [2,3,5]
     
     because 2*3*5=30
     Return:
     fac (list) factors primes of n.'''
    if primos=='atkin':
        primos=atkin(int(math.ceil(math.sqrt(n))))
    fac=[]
    s=math.sqrt(n)
    for i in primos:
        while n%i==0:
            n/=i
            s=math.sqrt(n)
            fac.append(i)
        if i>=s:
            if n==1:
                return fac
            return fac+[n]

def factor_fermat(n):
    '''Return Fermat factorization  of n>3, read about here : https://en.wikipedia.org/wiki/Fermat%27s_factorization_method

     Args:
     n (int) number for factorization

     Return:
     n  factored in 2 terms, in tuple format'''
    if n%2==1:
        for a in xrange(int(math.ceil(math.sqrt(n))),int(math.ceil((n+9)/6.0 +1))):
            b=math.sqrt(a**2-n)
            if int(b)==b:
                return a-b,a+b
        return n
    else:
        return 'n tem que ser impar > 3!'

def factor_lehman(n):
    '''Return Lehman factoring algorithm of n.

     Args:
     n (int) number for factorization

     Return:
     n  factored in 2 terms, in tuple format
     '''
    if n>21:
        z=int(math.ceil(pow(n,1/3.0)))
        nr=pow(n,1/6.0)
        for k in xrange(1,z+1):
            if n%(k+1)==0:
                return (k+1,n/(k+1))
            q=math.sqrt(4*k*n)
            q2=q*q
            for a in xrange(int(math.ceil(q)),1+int(math.ceil(q+nr/(4*math.sqrt(k)) ) ) ):
                b=round(math.sqrt(a*a-q2),4)
                if int(b)==b:
                    s=gcd(a+b,n)
                    return s,n/s
        return n

def mobius(n,primos='atkin'):
    '''Return result of mobius function for n

     Args:
     n (int) variable  return result on function

     Return:
     result of function,  the result exist  in  set {-1,0,1} and depends of n.
     '''
    k=factor(n,primos)
    s=len(k)
    if len(set(k))!=s:
        return 0
    if  s%2==0:
        return 1
    return -1

def base(n,b):
    '''Convert n in number system 10 to n in b number system. Read about: en.wikipedia.org/wiki/Radix

     Args:
     n (int) number in base 10
     b (int) base to convert
     
     Return:
    N (list)  terms of n in base b
    int(S) (int) n in base b
     '''
    k=int(math.ceil(math.log(n+1,b)))
    if b**k==n:
        N,S=[1]+[0]*(k-1),'1'+"0"*(k-1)
    else:
        N=[]
        S=''
        for i in xrange(k,-1,-1):
            z1=(b**i)
            z=n/z1
            N.append(int(z))
            S+=str(z)
            n-=z*z1
    return N,int(S)

def base_factorial(n):
    '''Convert n in base 10 number system to n in factorial number system "b!" Read about: en.wikipedia.org/wiki/Factorial_number_system

     Args:
     n (int) number in base 10
     
     Return:
    N (list)  terms of n in base b!
    int(S) (int) n in base b!
     '''
    z=1
    while math.factorial(z+1)<n: z+=1
    N=[]
    S=''
    for k in xrange(z,-1,-1):
        b=math.factorial(k)
        N.append(aux)
        S+=str(aux)
        n-=aux*b
        k-=1
    return N,int(S)

def baseb_to_10(n,b):
    '''Return number in base b number system to base 10 number system

    Args:
    n (int) Number in base b
    b (int) Base value
    Return: int in base 10 numerical system.
    '''
    s=str(n)
    k=len(s)-1
    return sum(int(s[k-i])*(b**i) for i in xrange(k,-1,-1))

def base_change_fractal_method(n,b):
    '''Use recursive fractal method to convert all numbers betwen 0 and n in base 10 to base b
    Args:
    n (int) Number limit 
    b (int) Base value
    Return: 
    list of strings  with numbers in base b writed in str format,'''
    nivel=int(math.ceil(math.log(n+1,b)))
    numeros=['']
    tex=tuple([str(a) for a in xrange(b)])
    pot=1
    for i in xrange(nivel-1):
        for j in tex:
            for k in xrange(pot):
                numeros.append(j+numeros[k])
        numeros=numeros[pot:]
        pot*=b
    aux=0
    while pot+aux<=n:
        for j in tex[1:]:
            for k in xrange(pot):
                numeros.append(j+numeros[k])
                aux+=1
                if pot+aux>=n:
                    return numeros
    return numeros


def sophiegermain(n,primos='primos'):
    ''' Return Primes of Sophie Germain between 0 and n. Read about: en.wikipedia.org/wiki/Sophie_Germain_prime

    Args:
    n (int) limit of seach
    primes (set) Set of primes before n

    Return:
    sgs (set) return set of Sophie germain Primes before n(include n if n is Sophie Germain prime).'''
    if primos=='primos':
        primos=set(atkin(2*n+1))
    sgs=primos - set(range(n+1,2*n+2))
    for i in sgs.copy():
        if 2*i+1 not in primos:
            sgs.remove(i)
    return sgs
def safe_primes(ate):
    L=[2*i+1 for i in sophiegermain(ate) if 2*i+1<ate]
    return L


def cunningham_chain(ate):
    '''Returns all numbers that exist in Cunnigham chains of different sizes. Read about: en.wikipedia.org/wiki/Cunningham_chain

    Args:
    ate (int) top of seach

    Return:
    cadeias (list of sets) list of all numbers inside Cunnigham sets Stratified by size of chain. 

     Upper limit of the number of terms in a chain proof:
     a0=p, a1=2p+1, a2=2(2p+1)+1=4p+3, ..., an=(2^(n-1))p+2^(n-1)-1=(2^(n-1))(p+1)-1

     so an=(2^(n-1))*(p+1)-1 where an<N
     when u solve this equation u find n<log((N+1)/(p+1))/log(2)+1
     and set p=2 because is lesser prime number, so u find one superior limit of size of cunningham chain. 
     '''
    sg=set(sophiegermain(ate))
    z=math.log((ate+1)/3.0,2)+1
    maiorcadeia=trunc(z)
    cadeias=[]
    for i in xrange(maiorcadeia,1,-1):
        aux=set([])
        for p in sg.copy():
            s=set((2**n)*(p+1)-1 for n in xrange(i))
            if s-sg==set([]):
                aux=aux.union(s)
        sg=sg-aux
        cadeias.append(aux)    
    return cadeias

def chen_primos(n):
    primos=[2, 3, 5, 7, 11, 13, 17, 19]
    if n<=21:
        return [i for i in primos if i<=n]

    primos=atkin(n+2)
    if primos[-1]>n:
        primosaux=set(primos[8:-1])
    else:
        primosaux=set(primos[8:])
    primos=set(primos)
    lista_chen=[2, 3, 5, 7, 11, 13, 17, 19]
    aux=[]
    for p in primosaux:
        if p+2 in primos:
            lista_chen.append(p)
        else:
            s=factor_lehman(p+2)
            if s[0] in primos and s[1] in primos:
                lista_chen.append(p)
    del primos
    del primosaux
    return lista_chen
def primos_weak(n):
     ''' Return  Weak primes before n(n not include in test), Read about, code folow this definition here: numbersaplenty.com/set/weak_prime/    ;      oeis.org/A051635

        Args:
        n (int) top of seach

        Return:
        d (list) list of Weak primes.
    '''
     primos=atkin(n)
     d=[]
     for i in xrange(1,len(primos)-1):
         m=0.5*(primos[i-1]+primos[i+1])
         if m>primos[i]: d.append(primos[i])
     return d

def primos_balanced(n):
     ''' Return all balanced primes before n. Read about: en.wikipedia.org/wiki/Balanced_prime

    Args:
    n (int) top of seach

    Return:

    d (list) list of balanced primes'''
     primos=atkin(n)
     d=[]
     for i in xrange(1,len(primos)-1):
         m=0.5*(primos[i-1]+primos[i+1])
         if m==primos[i]: d.append(primos[i])
     return d

def primos_strong(n):
     '''Return list of Strong primes before n. Read about: en.wikipedia.org/wiki/Strong_prime

    Args:
    n (int) top of seach

    Return:

    d (list) list of Strong primes'''
     primos=atkin(n)
     d=[]
     for i in xrange(1,len(primos)-1):
         m=0.5*(primos[i-1]+primos[i+1])
         if m<primos[i]: d.append(primos[i])
     return d

def  primos_fra_equi_for(n):
    '''Return dicionary with weak(fraco), balanced(equilibrado) and strong(forte) primes before n. Read about:  in functions primos_strong, primos_balanced and primos_weak

    Args:
    n (int) top of seach

    Return:

    d (dict of lists) dicionary of lists with type of primes'''
    primos=atkin(n)
    d={'fraco':[],"equilibrado":[],"forte":[]}
    for i in xrange(1,len(primos)-1):
         m=0.5*(primos[i-1]+primos[i+1])
         if m>primos[i]: d['fraco'].append(primos[i])
         elif m==primos[i]: d['equilibrado'].append(primos[i])
         else: d['forte'].append(primos[i])
    return d

def phieuler(n,primos='atkin'):
    ''' Return totient function value of n. Read about: en.wikipedia.org/wiki/Euler%27s_totient_function

     Args:
     n (int) n for seach totient function value
     primes (list) list of prime numbers

     Return:
     s (int) is totient value for n'''
    div=list(set(factor(n,primos=primos)))
    s=float(n)
    for i in div:
        s*=(1-1.0/i)
    return int(s)

def coprimos(com,ate):
    ''' Return all coprimes with  int 'com' between 1 and 'ate'. Read about: en.wikipedia.org/wiki/Coprime_integers
     Exemple:
     if com=2 and ate=10
     
     code will return: [1,3,5,7,9]
     
     Args:
     com (int) Number of witch we want know coprimes with him, 
     ate (int) limit of seach coprime

     Return:
     co (list) of all coprimes with 'com' before 'ate' '''
    ks=[]
    for i in xrange(com/2+1):
        if gcd(com,i)==1:
            ks.append(i)
            ks.append(com-i)
    ks=set(ks)
    co=[i for i in xrange(1,ate) if i%com in ks]
    return co

def raizdigital(n,grup=False):
    ''' Return digital hot of all numbers before n. Read About: en.wikipedia.org/wiki/Digital_root

      Args:
      n (int) top of code calculate, if n=100 code will calculate all digital roots before n(include n)
      grup (bool) Bolean variable for if user want stratify  numbers by value of digital root

      Returns:
          l (list) list of digital roots before n(include n)
          W (list of list) list of all numbers stratfy by a digital root'''
    l=[]
    W=[set([]) for i in xrange(10)]
    for i in xrange(n+1):
        s=i
        while s>9:
            s=sum(int(j) for j in str(s))
        l.append(s)
        W[s%9].add(i)
    if grup:
        return l,W
    else:
        return l

def pares(n,b=6,a=1,primos='atkin',just_primes=0):

    ''' Return values of k  and values of numbers p1 and p2 when the result p1=k*b-a and p2=k*b+a are primes is satisfied:

     if b=6 and a=1 we have k and p  twin primes. Read about en.wikipedia.org/wiki/Twin_prime

     Args:
     n    (int) top of seach for code
     b    (int) b of k*b+a=p where k is variable
     a    (int) a of k*b+a=p where k is variable
     primos (list) list of primes

     Return:
      L (list)  values of possible k wich condition is satisfied
      p (list)  values of possible primes  wich condition is satisfied
    '''
    if primos=='atkin':
        primos=set(atkin(n))
    L,p=[],[]
    null=set([])
    for i in xrange(0,n,b):
          if set([i-a,i+a]) - primos==null:
            L.append(i/b)
            p.append(i-a)
            p.append(i+a)
    if just_primes==0: return p
    if just_primes==1: return L
    return L,p

def nlucas(ate,l1=2,l2=1):
    ''' Lucas number's  sequence Read about www.teses.usp.br/teses/disponiveis/55/55136/tde-03032017-143706/pt-br.php

     Args:
     ate (int) top limit of value of number
     l1 (int) fist element of sequence
     l2 (int) second element of sequence

     Return:
     L (list) resultant sequence
     '''
    L=[l1,l2]
    s=2
    while L[-1]<ate:
        L.append(L[-2]+L[-1])
    return L[:-1]

def fibonacci(ate):
    ''' fibonacci sequence Read about www.teses.usp.br/teses/disponiveis/55/55136/tde-03032017-143706/pt-br.php
     Args:
     ate (int) top limit of value of number

     Return:
     nlucas(ate,1,1) (list) resultant sequence
     '''
    return nlucas(ate,1,1)

def perfect_numbers(a,b,pot='todas',perfect=True):
    ''' The algoritm will return all perfect or not perfect powers numbers betwen a and b
    Args:
    a       (int)   lower bound limit to seach
    b       (int)   upper bound of seach
    perfect (bool)  if true function will return list of perfect powers

    Return: 
    L       (list) list of all perfect or not perfect numbers betwen a and b
    '''
    if pot=='todas':
        L=[]
        for j in xrange(2,b):
            aux=[2,math.ceil(math.log(a,j))]
            k=max(aux)
            while j**k<b:
                L.append(j**k)
                k+=1
        if perfect:
            return L
        L=set(range(a,b))-set(L)
        return L
    if a==0:
        minimo=int(a)
    else:
        minimo=int(min(a,math.ceil(math.log(a,pot))))
    L=set([i**pot for i in xrange(minimo,int(trunc(pow(float(b),1.0/pot))) ) ])
    return(L)



def estratos_com_elementos(base,nivel,sn,lista='primos',pro=False,por_tlista=False):
    '''Use base**nivel to constroction '''
    maxi=base**nivel
    if lista=='primos': lista=atkin(base**nivel)
    b2=maxi/(base**sn)
    estratos=[0]*b2
    aux=[array([1]*maxi),lista][pro]
    k=0
    for i in xrange(min(len(lista),maxi)):
        if lista[i]<base**nivel:
               estratos[lista[i]%b2]+=aux[i]
               k+=1.0
    if not pro:
        aux=[float(base**(sn)),k][por_tlista]
        estratos=array(estratos)/aux
    return estratos
def conjectura_de_collatz_count(n):
    k=0
    while n!=1:
        if n%2==1: n=3*n+1
        else: n/=2
        k+=1
    return(k)


def conjectura_de_collatz(n,enc=False):
    listas_collatz=[]
    def func_auxiliar(n=n):
        aux=n
        Lista=[]
        while n!=1:
            Lista.append(n)
            if n%2==1:
                n=3*n+1
            else:
                n/=2
                if aux>n>3 and enc:
                    listas_collatz.append(Lista+listas_collatz[n-3])
                    return
        listas_collatz.append(Lista)
        return
    raux=0.0
    if enc:
        a=0
        for i in xrange(3,n+1):
            AUX=func_auxiliar(i)
            del AUX
            r=len(listas_collatz[-1])
            if r>raux:
                raux=float(r)
                a=i
        return(set(listas_collatz[a-3]))
    func_auxiliar(n)
    return(set(listas_collatz[0]))


def primos_com_simetria_fractal(primos,nlados,nivel):
    pri=[base_repr(i,nlados) for i in primos]
    base=[nlados**(nivel-i-1) for i in xrange(nivel)]
    for i in xrange(len(pri)):
        s=''
        for k in pri[i]:
            if k=='0':
                s+=k
            else:
                s+=str(nlados-int(k))
        pri[i]=baseb_to_10(int(s),nlados)
    return set(pri).intersection(set(primos))

def primos_com_simetria_fractal2(primos,X,Y,nlados,nivel):
    L=[]
    delta=nlados**(nivel-1)
    delta=((X[0]-X[delta])**2+(Y[0]-Y[delta])**2)**2
    for p1 in primos:
        for p2 in primos[1:len(primos)]:
            k=(X[p1]+X[p2],Y[p1]-Y[p2])
            k=k[0]**2+k[1]**2
            if k<delta and p1!=p2:
                L+=[p1,p2]
                primos.remove(p1)
                primos.remove(p2)
    return set(L)