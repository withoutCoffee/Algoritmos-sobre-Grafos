import grafo
from random import randint

arquivo="arquivo_grafos/digrafo01.txt"
matriz = grafo.readGraph(arquivo)#Retorna tupla com matriz, ordem, tamanho e graus

def ndev(v):
    n=[]
    m = matriz[0]
    for i in range(len(m[v])):#verificando alinha do vértice V
        if(m[v][i]!=0):
            n.append(i)
    return n;#retorna lista com os vértices que N+ de V

def procedimento(v):
    global relogio
    relogio+=1
    pe[v] = relogio
    for w in ndev(v):
        if pe[w]==0:
            #marcar vw como azul na floresta de pronfundidade
            print("Aresta azul da floresta T:",[v,w])
            pai[w]=v
            procedimento(w);
        else:
            if (ps[w]==0):
                #marcar vw como aresta de retorno
                print("Retorno aqui em",[v,w])
            elif(pe[v]<pe[w]):
                #marcar aresta de avanço
                print("Avanço aqui em",[v,w])
            else:
                print("Cruzamento aqui em",[v,w])
    relogio+=1
    ps[v]=relogio;

#inicialização
relogio=0 #Relógio grobal
pe = [0 for i in range(matriz[1])]#tempo de entrada no vértice
ps = [0 for i in range(matriz[1])]#tempo de saida no vértice
pai = [None for i in range(matriz[1])]#pais dos vértices
#definindo raiz da busca
raiz = randint(0,matriz[1]-1)#Raiz da busca, 0 a ordem -1;
while(min(pe)==0):
    procedimento(pe.index(min(pe)))
print("\nTempo de entrada dos vértices:",pe,"\nTempo dos saída dos vértices:",ps)
print("Pais dos vértices:",pai)
