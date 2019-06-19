def readFile(fileName):#leitura de arquivo de texto
    file = open(fileName,'r')#leitura do arquivo
    content=file.readlines()#leritura das linhas do arquivo
    file.close()#fecha transmissão de dados do arquivo
    return content#retorna conteúdo do arquivo

def writeFile(fileName,content):#escrever arquivo de texto
    file = open(fileName,'w')#escrever arquivo
    file.writelines(content)
    file.close()
    return True#deu tudo blz

#Matriz de adjacências
def readGraph(arquivo):
    lista = readFile(arquivo)
    grafo = []
    arestas = 0
    graus = [0]*int(lista[0])

    for i in range(int(lista[0])):
        linha=[]
        for k in lista[i+1].split():
            if(int(k)!=0):
                arestas+=1
                graus[i]+=1
            linha.append(int(k))
        grafo.append(linha)
    arestas = int(arestas/2)
    tamanho= int(lista[0])+arestas
    ordem = int(lista[0])
    return grafo,ordem,tamanho,graus#ordem significa o quantidede vértices

#Lista de adjacências
def graphList(arquivo):
    lista = readFile(arquivo)
    grafo = [];
    arestas = 0
    graus = [0]*int(lista[0])

    for i in range(int(lista[0])):
        linha = []
        cont = 0;
        for k in lista[i+1].split():
            cont+=1
            if(int(k)!=0):
                graus[i]+=1
                arestas+=1
                linha.append(cont)

        grafo.append(linha)
    arestas = int(arestas/2)
    tamanho= int(lista[0])+arestas
    ordem = int(lista[0])
    return grafo,ordem,tamanho,graus

#Extração de grau máximo mínimo e médio
def propiedadeGraus(listaGraus):
    maior = listaGraus[0]#maior grau
    menor = listaGraus[0]#menor grau
    soma = 0
    for i in listaGraus:
        soma+=i
        if(maior<i):
            maior = i
        if(menor>i):
            menor = i
    return maior,menor, soma/len(listaGraus)
