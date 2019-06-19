import grafo
from random import randint
import math
listaAux=[]
def buscaAresta(vetor,aux):#busca de custa de arestas
    saida = []
    for i in aux:
        if(vetor[i] != 0):
            saida.append(vetor[i])
    if(saida!=[]):
        listaAux.append(saida)#adiciona vertor de vértices candidatos a entrarem na árvore
    else:
        listaAux.append([math.inf])
    #print("SAIDA:",saida)
    #print("MIN:",min(saida))
    return True #min(saida),max(saida)
def menorPos(vetor):
    maior = vetor[0][0]
    menor = maior
    exit = vetor[0]
    for i in range(len(vetor)):
        for j in range(len(vetor[i])):
            if(maior<vetor[i][j]):
                maior = vetor[i][j]
            elif(menor > vetor[i][j]):
                menor = vetor[i][j]
                exit = vetor[i]
    return exit #retorna vetor linha com a menor posição da matriz dada

file = "arquivo_grafos/grafoTesteComPesos.txt"#arquivo do grafo a ser lido
conteudo = grafo.readGraph(file)
'''O métodos de leitura de grafo retornam tupla (grafo,ordem,tamanho,Lista de graus)'''

matriz = conteudo[0] #matriz de adjacências
ordem = conteudo[1] #ordem do grafo; cardinalidade do conjunto dos vértices

conjunto_aux = [i for i in range(ordem)]#conjunto auxiliar (vértices que não estão na árvore)
arvore = []#arvore vazia
raiz = randint(0,ordem-1)#vertice raiz da arvore
arvore.append(raiz)

conjunto_aux.remove(raiz)#removendo vértice do conjunto auxiliar
arvoreGeradora=[];

#while acaba quando a arvore tiver todos os vértices
while(len(arvore) != ordem):
    for i in arvore:
        #busca arestas do vértice em questão, usando como auxíliar conjunto de vértices que não estão na árvore
        #conjunt auxíliar ajuda para pesquisar apenas arestas que estão ligadas em vértices que não estão na árvore
        buscaAresta(matriz[i],conjunto_aux)
    b = arvore[listaAux.index(menorPos(listaAux))]# b = vértice com menor peso dos vértices candidatos

    if(matriz[b].index(min(menorPos(listaAux))) not in arvore):#verifica se indice da menor posição do vértice está na árvore(verifica se vértice está na árvore).
        arvore.append(matriz[b].index(min(menorPos(listaAux))))#adiciona vértice na arvore
        #remove vértice do conjunto auxiliar (vértices que não estão na árvore)
        conjunto_aux.remove(matriz[b].index(min(menorPos(listaAux))))
    vX = b
    vY = arvore[len(arvore)-1]#vértice Y, (X,Y) cordenada do par não ordenado,(aresta)
    arvoreGeradora.append([vX,vY])#colocando aresta na árvore geradora de custo mínimo
    listaAux=[]

print("ARVORE GERADORA DE CUSTO MÍNIMO:",arvoreGeradora)
#Custa da arvore
soma=0
for i in range(len(arvoreGeradora)):
    linha = arvoreGeradora[i][0]
    coluna = arvoreGeradora[i][1]
    soma+=matriz[linha][coluna]
print("\nCUSTO DA ARVORE:",soma)
