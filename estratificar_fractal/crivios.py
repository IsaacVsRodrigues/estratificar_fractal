from numpy import *
from itertools import  *
from time import clock,asctime
from sets import *
import sys
from ctypes import *
from math import *
dir(sys)
maximointeiro=sys.maxint

def optxtseq(n,enu=False,*args,**kwargs):
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
     vetaux=set(str(i) for i in xrange(10))
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
    s=int(sqrt(n))
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
        lim=int(sqrt(nmax))+1
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
    primos=range(2,L+1)
    for i in xrange(int(sqrt(L+1))+1):
        w=primos[i]
        primos=filter(lambda primos: primos%w!=0 or primos==w,primos)
    return primos

def josephus(L):
    '''return result of The Sieve of Josephus Flavius: Read more about en.wikipedia.org/wiki/Lucky_number

    Args:
    L (int) limit for sieve

    Return:

    s_numbero (list) result of Sieve'''
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
        primos=atkin(int(ceil(sqrt(n))))
    fac=[]
    s=sqrt(n)
    for i in primos:
        while n%i==0:
            n/=i
            s=sqrt(n)
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
        t=clock()
        for a in xrange(int(ceil(sqrt(n))),int(ceil((n+9)/6.0 +1))):
            b=sqrt(a**2-n)
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
        z=int(ceil(pow(n,1/3.0)))
        for k in xrange(1,z+1):
            if n%(k+1)==0:
                return (k+1,n/(k+1))
            q=sqrt(4*k*n)
            for a in xrange(int(ceil(q)),int(ceil(q+pow(n,1/6.0)/(4*sqrt(k))))):
                b=sqrt(a*a-q*q)
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
    k=int(log(n,b))
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
    while factorial(z+1)<n: z+=1
    N=[]
    S=''
    for k in xrange(z,-1,-1):
        b=factorial(k)
        aux=n/b
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

def cunningham_chain(ate):
    '''Returns all numbers that exist in Cunnigham chains of different sizes. Read about: en.wikipedia.org/wiki/Cunningham_chain

    Args:
    ate (int) top of seach

    Return:
    cadeias (list of sets) list of all numbers inside Cunnigham sets Stratified by size of chain. Order folow the minimum size(2) to max possible size, log((ate+1)/3.0,2)+1
    '''
    sg=set(sophiegermain(ate))
    z=log((ate+1)/3.0,2)+1
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
     até (int) limit of seach coprime

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

def pares(n,b=6,a=1,primos='atkin'):
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
    return L

def fibonacci(ate):
    ''' fibonacci sequence Read about www.teses.usp.br/teses/disponiveis/55/55136/tde-03032017-143706/pt-br.php

     Args:
     ate (int) top limit of value of number

     Return:
     nlucas(ate,1,1) (list) resultant sequence
     '''
    return nlucas(ate,1,1)

def estratos_com_elementos(base,nivel,sn,lista='primos'):
     '''Use base**nivel to constroction '''
     maxi=base**nivel
     if  lista=='primos':
          num=range(base**nivel)
          lista=atkin(base**nivel)
     b2=maxi/(base**sn)
     estratos=[0]*b2
     for i in lista:
          if i<base**nivel:
               estratos[i%b2]+=1
     for i in xrange(len(estratos)):
          estratos[i]/=float(base**sn)
     return estratos
