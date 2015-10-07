
# coding: utf-8

# **Course website**: http://www.leouieda.com/matematica-especial
# 
# **Note**: This notebook is part of the course "Matemática Especial I" of the [Universidade do Estado do Rio de Janeiro](http://www.uerj.br/). All content can be freely used and adapted under the terms of the 
# [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/).
# 
# ![Creative Commons License](https://i.creativecommons.org/l/by/4.0/88x31.png)

# # Tarefas de Python II

# Nessas tarefas, vocês vão praticar os conceitos de programação em Python que aprenderam na prática passada. Além disso, vão aprender algumas coisas novas, como ler dados de arquivos.
# 
# Algumas células de código estarão preenchidas. Essas células são exemplos ou códigos que devem ser rodados para verificar se seu resultado está de acordo com o esperado.

# ## Leitura recomendada
# 
# O material da lição "Programming with Python" versão 4 do
# [Software Carpentry](http://software-carpentry.org/).
# Particularmente:
# 
# * Lists
# * Input and Output
# * Strings

# ## Listas
# 
# Vocês tiveram um contato limitado com listas antes. Agora, vamos aprender como fazer coisas mais sofisticadas com listas, como adicionar valores, fazer uma cópia, e utilizar a lista no `for`.
# 
# Primeiro, vamos criar uma lista para testarmos.

# In[1]:

lista = [42, 21, 14, 7, 29]


# Você pode perguntar o número de elementos que existem em uma lista utilizando a função `len` (muito melhor que contar os elementos na mão).

# In[2]:

N = len(lista)
print(N)


# Outra coisa que podemos fazer é adicionar coisas a nossa lista utilizando o método `append`. 
# 
# **Nota**: "funções" são coisa como `print`, `len` e `range` que são executadas com `()` e produzem algo. "Métodos" são funções que operam em uma determinada variável e a alteram, como `append` e `format`.

# In[3]:

lista2 = [5, 15, 31, 43, 67, 88, 97]


# lista2.append(7)

# In[4]:

print(lista2)


# Experimente adicionar elementos a `lista` (utilize a célula vazia abaixo; isso não é uma tarefa ainda).

# In[6]:

lista2.append(7)


# Até agora, vocês viram o `for` utilizado somente em conjunto com a função `range`, por exemplo:
# 
#     for i in range(10):
#         print(i)
# 
# Essa é uma parte de como o `for` realmente opera. Na realidade, o `for` itera sobre *elementos de uma lista*. Qualquer lista. O `i` no exemplo acima é uma variável como qualquer outra e pode ter o nome que você quiser. 
# 
# Por exemplo, para iterar sobre os elementos de nossa `lista`:

# In[8]:

for valor in lista2:
    print("valor ==", valor)


# ## Lendo dados de arquivos
# 
# No mundo real, vocês precisarão rotineiramente trabalhar com dados que estão salvos em arquivos. Um formato muito utilizando é o CSV (Comma Separated Values). Nas tarefas dessa prática, vocês terão que analisar os dados do arquivo `dados.csv` que está junto no repositório. Abra esse arquivo em um editor de texto (Notepad++ ou SublimeText) para ver como é o arquivo. A primeira coluna do arquivo representa a hora do dia (de 0 a 24) e a segunda coluna representa um dado fictício de temperatura.
# 
# Precisamos carregar esses dados para duas listas (uma para as horas e outra para as temperaturas) para podermos trabalhar com eles no Python. Para abrir um arquivo para leitura, utilize a função `open` do Python. Por exemplo: 

# In[9]:

arquivo = open('dados.csv')


# A variável produzida por `open` possui alguns métodos para acessar o conteúdo do arquivo em formato de texto (strings).
# Um desses métodos é o `readline`. Esse método lê a próxima linha do arquivo e a retorna como texto. Por exemplo:

# In[13]:

linha = arquivo.readline(1)
print(linha)


# Rode a célula acima novamente e veja o que acontece.
# 

# Quanto terminamos de utilizar o arquivo, devemos fechá-lo (como as figuras).

# In[14]:

arquivo.close()


# Uma vez obtida a linha em formato de texto, precisamo separar os dois valores. Os objetos de texto (strings) possuem diversos métodos para trabalharmos com eles. Um desses vocês já conhecem, o método `format`. Para ver uma lista dos métodos disponíveis, digite na célula abaixo `linha.` e aperte a tecla TAB.

# In[15]:

linha.split


# O método que queremos chama-se `split`. Ele faz exatamente o que o nome diz: quebra uma string em várias. O argumento que é passado para ele é o texto que separa os diversos blocos. Por exemplo:

# In[16]:

texto = "Texto ? separado ? por ? interrogacoes"
blocos = texto.split(' ? ')
print(blocos)


# Note que o resultado produzido por `split` é uma lista.

# In[17]:

blocos[0]


# Experimente separar a linha do arquivo que vemos acima nos dois valores que ela contem (utilize a célula vazia abaixo; isso não é uma tarefa ainda).

# In[ ]:




# Depois que conseguirmos nossos valores em formato texto, precisamos convertê-los para números. O Python nos fornece algumas funções para isso: `int` (para números inteiros), `float` (para números "reais" ou ponto flutuante) e `complex` (para números complexos). Por exemplo: 

# In[ ]:

valor_em_texto = "8888"
valor = int(valor_em_texto)
print(valor + 1)


# In[ ]:

float_em_texto = "4.2"
valor = float(float_em_texto)
print(valor/2)


# Por último, podemos tratar a variável `arquivo` retornada por `open` como uma lista das linhas do arquivo. Isso quer dizer que podemos utilizá-la em um `for` como:

# In[ ]:

arquivo = open('dados.csv')
num_linhas = 0
for linha in arquivo:
    num_linhas = num_linhas + 1    
arquivo.close()
print(num_linhas)


# Experimente imprimir todas as linhas do arquivo `README.md` (utilize a célula vazia abaixo; isso não é uma tarefa ainda).

# In[ ]:




# ## **IMPORTANTE**: Cada tarefa abaixo deve ser feita por um membro DIFERENTE do grupo. Os outros devem ajudá-lo mas a pessoa digitando deve ser quem está encarregado da tarefa.

# ## Tarefa 1
# 
# * Carregue os dados do arquivo `dados.csv` em duas listas: `tempos` e `dados` (os nomes precisam ser esses!). `tempos` deve conter os valores da primeira coluna e `dados` os da segunda.
# * Faça um gráfico dos hora x temperatura (lembre-se de utilizar a mágia `%matplotlib inline`).
# 
# Você pode utilizar quantas células achar necessário para realizar a tarefa (use o menu "Insert"). Inclua comentátios para explicar o que você está fazendo.

# In[9]:

tempos = []
dados = []
arquivo = open('dados.csv')
for linha in arquivo:
    blocos = linha.split(',')
    tempos.append(blocos[0])
    dados.append(blocos[1])
print("tempos", tempos)
print("dados", dados)
arquivo.close()

import matplotlib.pyplot as plt 
x = tempos
y = dados
plt.figure()
plt.plot(x, y, "-k")
plt.xlabel("Hora")
plt.ylabel("Temperatura")
plt.savefig("fig/grafico-horaxtemp.png")
plt.show()
plt.close()


# ### Resultado esperado
# 
# A figura gerada deve ser parecida com:
# 
# ![images/dados.png](images/dados.png)
# 
# Ao executar a célula abaixo, o resultado deve ser similar a:
# 
#     Tempos: [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, ...]
#     Dados: [0.0, 0.61464164, 1.0320324, 1.1238251, 0.87540985, 0.39101585, -0.14270041, ...]

# In[ ]:

print("Tempos:", tempos)
print("Dados:", dados)


# ## Tarefa 2
# 
# * Calcule a temperatura média para o dia inteiro e guarde-a em uma variável chamada `media`.
# * Calcule o desvio padrão da temperatura para o dia inteiro e guarde-o em uma variável chamada `desvio_padrao`.
# 
# Lembre-se que o desvio padrão é
# 
# $$
# \sigma = \sqrt{\sum\limits_{i=1}^{N}\frac{ (x_i - x_{media})^2 }{N}}
# $$
# 
# em que $x_i$ são os dados, $x_{media}$ é a média e $N$ é o número de dados.
# 
# **Dica**: Para elevar um número a uma potência, utilize `**`. Por exemplo, `2**4 == 16`.

# In[ ]:




# ### Resultado esperado
# 
# As celúlas abaixo comparam a sua média e desvio padrão com os calculados pela biblioteca [numpy](http://numpy.org/).
# Ambas devem imprimir `True` quando executadas.

# In[ ]:

import numpy as np
print("Media esta igual?", np.allclose(media, np.mean(dados)))


# In[ ]:

print("Desvio padrao esta igual?", np.allclose(desvio_padrao, np.std(dados)))


# ## Tarefa 3
# 
# * Ache o valor máximo de temperatura medido e guarde-o na variável `maximo`.
# * Ache o valor mínimo de temperatura medido e guarde-o na variável `minimo`.
# 
# **Dica**: o Python inclui um valor especial chamado de `None`. Ele é comumente utilizado para marcar que uma variável está "vazia" ou não utilizada ainda. Um detalhe desse valor é que não podemos utilizar `==` para checar se uma variável possui o valor `None`. Ao invés disso, devemos utilizar o comando `is`. Por exemplo:
# 
#     variavel = None
#     if variavel is None:
#         print("A variavel eh None")
#         variavel = 20
#         

# In[ ]:




# ### Resultado esperado
# 
# As celúlas abaixo comparam os valores máximo e mínimo com os calculados pelas funções `max` e `min` do Python.
# Ambas devem imprimir `True` quando executadas.

# In[ ]:

print("Maximo esta igual?", np.allclose(maximo, max(dados)))


# In[ ]:

print("Minimo esta igual?", np.allclose(minimo, min(dados)))


# ## Tarefa 4
# 
# * Calcule a temperatura média por hora e guarde-as em uma lista chamada `media_hora`.
# * Faça um gráfico dos dados originais juntamente com as médias que você calculou.
# 
# **Dica 1**: quantos dados existem por hora?
# 
# **Dica 2**: veja esse [exemplo de como colocar uma legenda no grafico](http://matplotlib.org/examples/api/legend_demo.html).

# In[ ]:




# ### Resultado esperado
# 
# A figura gerada deve ser parecida com:
# 
# ![images/media-por-hora.png](images/media-por-hora.png)

# ## Tarefa Bônus
# 
# Essa tarefa vale um bônus de 0.5 pontos na nota da prática.
# 
# * Calcule os máximos de temperatura por hora.
# * Calcule os mínimos de temperatura por hora.
# * Faça um gráfico com: (1) os dados originais (2) as médias por hora (3) os máximos por hora (4) os mínimos por hora.

# In[ ]:




# ### Resultado esperado
# 
# A figura gerada deve ser parecida com:
# 
# ![images/media-maximo-minimo-por-hora.png](images/media-maximo-minimo-por-hora.png)
