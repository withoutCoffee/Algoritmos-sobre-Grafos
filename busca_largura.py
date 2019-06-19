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

#inicialização
t=0
fila=[]#fila de vértices
lv=[0 for i in range(matriz[1])] #L(v) é o índice de v na busca em largura
pai=[None for i in range(matriz[1])]
nivel=[None for i in range(matriz[1])]
#definindo raiz da busca
v = 0#randint(0,matriz[1]-1)#Raiz da busca, 0 a ordem -1;
while(min(lv)==0):
    nivel[v]=0
    t+=1
    lv[v]=t
    fila.append(v)
    #realizar busca em lagura
    while(fila!=[]):
        v=fila[0]#v ← primeiro elemento de F
        fila.remove(v)
        for w in ndev(v):
            if(lv[w] == 0):
                #marcar vw como azul na floresta de pronfundidade
                print("Aresta azul da floresta T:",[v,w])
                pai[w]=v
                nivel[w]=nivel[v]+1
                t+=1
                lv[w]=t
                fila.append(w)
            elif(nivel[w]==nivel[v]):
                if(pai[w]==pai[v]):
                    #vw é aresta “irmão”
                    print("Aresta irmão:",[v,w])
                else:
                    #vw é aresta primo
                    print("Aresta primo:",[v,w])
            elif(nivel[w]==nivel[v]+1):
                #vw é aresta tio
                print("Aresta tio:",[v,w])
    #fim da busca em largura

print("\nTempo de entrada dos vértices:",lv)
print("Pais dos vértices:",pai)
