import time

# colocar diretorio do arquivo
arq = open("/home/hyuri/Documentos/in1","r")
b = []
data = arq.readlines()
for linha in range(0, len(data)):
    #print(linha)
    b.append(int(linha))
    #print(b[linha])

a = [-2,11,-4,13,-5,-2]
# se a for todo de elementos negativos sumMax = 0
sumMax = 0
index1 = 0
index2 = 0

inicio = time.time()
for i in range(0, len(a)):
    for j in range(i, len(a)):
        sum = 0
        for k in range(i,j):
            sum +=a[k]
          #  print(a[k])
        if sum > sumMax:
            sumMax = sum
            index1 = i
            index2 = j

fim = time.time()
print("-----------------")
print(sumMax)
print(index1)
print(index2)
print(fim - inicio)