
Estratificação Visual dos Números Inteiros Via Fractais de Sierpinski
=====

## Sobre

O Pacote
----

Este site  é uma documentação da biblioteca em Python 2.7.* nomeada Estratificar. Esta ferramenta foi desenvolvida dentro do projeto de iniciação científica nomeado **Fractais, Congruências e Primos: Uma Estratificação Visual dos Números Inteiros via Fractais de Sierpinski**, desenvolvido na [Escola Nacional de Ciências Estatísticas](http://www.ence.ibge.gov.br). O seu desenvolvimento foi para auxiliar o estudo de conjunto de números inteiros. Além da biblioteca em Python, o leitor pode baixar os scripts do Python aqui (CITAR SCRPT).


Estratificação Visual dos Números Inteiros Via Fractais de Sierpinski
----

A biblioteca Estratificar foi baseada na Estratificação Visual de Números Inteiros via Fractais de Sierpinski foi desenvolvida a partir de reflexões durante a iniciação científica. Seu desenvolvimento envolveu estudos com a espiral de Ulam e fractais no formato n-gons. Este texto não pretende focar na parte matemática do estudo, no entanto, é recomendável que os utilizadores da biblioteca leiam ou o artigo ou o relatório da iniciação científica.  A visualização de números utilizando estruturas visuais estão presentes desde os primórdios da matemática. Apesar disto a abordagem proposta  que conduziu a criação desta biblioteca é um estudo ímpar sobre o assunto. Então, como dito, é necessário ler sobre o assunto  nos textos de referência para poder utilizar esta biblioteca interpretando o resultado. O foco do estudo está em aritmética modular, no entanto, existem interpretações de funções de probabilidade discreta, que foram incluídas no Relatório da Iniciação científica. Assim como qualquer representação gráfica, essa representação possui  pontos fortes e pontos fracos para destacar. Um ponto forte desta  é tornar visível características de aritmética modular existentes em conjuntos numéricos. Caso o utilizador leia o artigo, poderá ver algumas conclusões e características que foram ressaltadas do estudo.


## Iniciando

É recomendável antes de iniciar ler sobre o assunto nos textos (CTAR RELATÓRIO E ARTIGO). Relacionados a isto, as funções do pacote mais importante são **fractal** e **pltpropor**. Nessas duas funções é feito o a estrutura visual utilizada. As outra funções do pacote são apenas complementares ao estudo. Além do pacote também existe um programa .exe desenvolvido para possíveis pesquisadores que tenham dificuldade de utilizar Python. Tal executável pode ser baixado aqui (CITAR EX). A documentação do executável e do pacote podem ser vistos aqui (CITAR SITE).

### Pré-requistos

O pacote do Python precisa das bibliotecas Matplotlib, Numpy as outras bibliotecas  utilizadas estão presentes no Python 2.7. Abaixo o leitor pode ver todos os imports feitos pelo o pacote. A biblioteca **crivios** é um dos scripts do pacote, ela não precisa ser instalada, pois será instalada ao instalar o pacote. O pacote está disponível apenas para Python 2.7.* prever-se futuramente uma versão para Python 3.* e para linguagem de programação R.
```
from crivios import *
from numpy import *
from itertools import  *
from time import clock,asctime
from sets import *
import sys
from ctypes import *
from math import *
from matplotlib.pyplot import plot, show, axis, legend, grid, annotate, subplot, title, scatter, xlabel, ylabel, colorbar
```

### Instalando

## Instalação via pip 

O pacote pode ser instalado via comando pip como está indicado abaixo. 
```
pip install Estratificar
```

## Executável

Também existe um programa executável que pode ser baixado aqui (CITAR LINK DO EXECUTÁVEL). A documentação do executável pode ser encontrada aqui(CITAR LINK DA DOC DO EXECUTAVEL)




## Feito com os seguintes pacotes do Python

	Abaixo estão destacados os principais projetos de Python utilizados no projeto. Destes, os únicos pre-requistos são o _Numpy_ e o _Matplotlib_. O resto foi utilizado para fazer partes do projeto e então merecem ser destacados. 

* [Python 2.7.* ](https://www.python.org) - Usado para fazer as funções.
* [Matplotlib  ](https://matplotlib.org) - Usado para fazer os gráficos matemáticos.
* [Numpy ](http://www.numpy.org) - Usado para algumas funções matemáticas.
* [Pyinstaller](https://www.pyinstaller.org) - Utilizado para fazer os .exe.
* [Tkinter](https://docs.python.org/2.7/library/tkinter.html) - Utilizado para fazer a interface gráfica do .exe.
* [Sphinx](http://www.sphinx-doc.org/en/master/) - Usado para fazer o site da documentação.

## Contato

Contato pessoal: [Isaac Victor Silva Rodrigues](isaacvictor@fisica.if.uff.br), estamos dispostos a receber sugestões e tirar dúvidas


## Authors


* **Isaac Victor Silva Rodrigues** - Estudante do projeto de iniciação cientifica

* **Lúcia Maria dos Santos Pinto** - Orientador do projeto de iniciação cientifica

* **Juscelino Bezerra dos Santos** - Co-orientador do projeto de iniciação cientifica


## Licença

Esse projeto está sobre a licença MIT, veja em [LICENSE.md](LICENSE.md) para detalhes.

