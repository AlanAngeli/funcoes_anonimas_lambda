lista = [
    ["P1",13],
    ["P2",6],
    ["P3",7],
    ["P4",50],
    ["P5",8],
]

#def func(item):
#    return item[1]

#lista.sort(key=func, reverse=True) #ordenar a lista de forma decrescente

#como codar isso com lambda:

lista.sort(key=lambda item: item[1], reverse=True) #item[1] se refere ao preço, item[0] ao produto (P1, P2,P3...)

print(lista)