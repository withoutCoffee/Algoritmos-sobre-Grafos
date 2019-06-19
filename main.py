import grafo

arquivo="grafoTeste.txt"
#matriz de adjacências
matriz = grafo.readGraph(arquivo)
'''O métodos de leitura de grafo retornam tupla (grafo,ordem,tamanho,Lista de graus)'''

str="Matriz Adjacências:\n{0}\n\nOrdem:{1}\nTamanho Grafo:{2}\nLista de Graus:{3}"
print(str.format(matriz[0],matriz[1],matriz[2],matriz[3]))

maior_menor = grafo.propiedadeGraus(matriz[3])#tupla com (maior,menor) graus
print("Maior grau: {0}, menor grau: {1}, grau médio: {2}".format(maior_menor[0],maior_menor[1],maior_menor[2]))

print("*********************************************************************************************************")

#lista de adjacências
lista = grafo.graphList(arquivo)
str="Lista Adjacências:\n{0}\n\nOrdem:{1}\nTamanho Grafo:{2}\nLista de Graus:{3}"
print(str.format(lista[0],lista[1],lista[2],lista[3]))

maior_menor = grafo.propiedadeGraus(lista[3])#tupla com (maior,menor) graus
print("Maior grau: {0}, menor grau: {1}, grau médio: {2}".format(maior_menor[0],maior_menor[1],maior_menor[2]))
