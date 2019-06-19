import grafo
def ordenacaoArestas(grafo_matriz,ordem):
    array_arestas = []
    pesos = []
    for i in range(ordem):
        for j in range(i+1,ordem):
            if(grafo_matriz[i][j]!=0):
                pesos.append(grafo_matriz[i][j])
                array_arestas.append([i,j])
    pesos.sort()
    #print(array_arestas,"\n",pesos)
    arestas_ordenadas = []
    cont = 0
    quant_arestas = len(pesos)
    while(len(arestas_ordenadas) < quant_arestas):

        for i in range(len(array_arestas)):
            aresta = array_arestas[i]
            if(grafo_matriz[aresta[0]][aresta[1]] == pesos[cont]):
                arestas_ordenadas.append(aresta)
                array_arestas.remove(aresta)
                break;
        cont+=1;
    #print(arestas_ordenadas,"\n",pesos)
    return arestas_ordenadas;

def findIndex(floresta,vertice):
    for i in range(len(floresta)):
        for j in range(len(floresta[i])):
            if(floresta[i][j] == vertice):
                listaIndex = floresta[i]
                return listaIndex,i;
#FIND SET, do slide
def findSet(floresta,vertice):
    vertices_conectados = []
    listaIndex = findIndex(floresta,vertice)# listaIndex[0] linha onde está o vérices na floresta
    for i in range(len(listaIndex[0])):
        vertices_conectados.append(floresta[listaIndex[1]][i])
    return vertices_conectados;
#comparacaoFindSet do slide
def comparacaoFindSet(arr1,arr2):
    a = len(arr1)
    b = len(arr2)
    if(a>b):
        for i in range(b):
            if(arr1[i] == arr2[i]):
                return False;
    else:
        for i in range(a):
            if(arr1[i] == arr2[i]):
                return False;
    return True;
# UNION, do slide
def union(floresta,aresta):
    listaIndex = findIndex(floresta,aresta[0])
    listaIndex2 = findIndex(floresta,aresta[1])

    floresta[listaIndex[1]] = floresta[listaIndex[1]] + listaIndex2[0]
    if([] in floresta):
        floresta.remove([])
    else:
        floresta.remove(listaIndex2[0])
    return floresta;


#Começa aqui

file = "arquivo_grafos/grafoTesteComPesos.txt"#arquivo do grafo a ser lido
conteudo = grafo.readGraph(file)
'''O métodos de leitura de grafo retornam tupla (grafo,ordem,tamanho,Lista de graus)'''
grafo_matriz = conteudo[0] #matriz de adjacências
ordem = conteudo[1] #ordem do grafo; cardinalidade do conjunto dos vértices

floresta = []
for i in range(ordem):
    floresta.append([i])

arestas_ordenadas = ordenacaoArestas(grafo_matriz,ordem);
arvoreGeradora = []
for i in range(len(arestas_ordenadas)):
    #print("FLORESTA:",floresta)
    if(len(arvoreGeradora) < ordem-1):
        aresta = arestas_ordenadas[i]
        a = findSet(floresta,aresta[0])
        b = findSet(floresta,aresta[1])
        if(comparacaoFindSet(a,b)):
            arvoreGeradora.append(aresta)
            floresta = union(floresta,aresta)
    else:
        break;
#fim
print("ARVORE GERADORA",arvoreGeradora)
soma=0
for i in range(len(arvoreGeradora)):
    linha = arvoreGeradora[i][0]
    coluna = arvoreGeradora[i][1]
    soma+=grafo_matriz[linha][coluna]
print("\nCUSTO DA ARVORE:",soma)
