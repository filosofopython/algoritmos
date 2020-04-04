
def subsetsum(set,n,sum):

    #preenchendo matriz
    matriz = ([[False for i in range(sum + 1)]
               for i in range(n + 1)])
    #preenchendo caso de zero elementos e soma 0 na matriz
    for i in range(n+1):
        matriz[i][0]=True
        for i in range(1,sum+1):
            matriz[0][i]=False
        for i in range(1, n + 1):
             for j in range(1, sum + 1):
                 #comparando se com menos numeros é possivel e se com o valor subtraido da soma também é possivel
                if j<set[i-1]:
                    matriz[i][j] = matriz[i-1][j]
                if j>= set[i-1]:
                    matriz[i][j] = (matriz[i-1][j] or   matriz[i - 1][j-set[i-1]])
        # printando o set
        if matriz[n][sum]:
            m=n
            b=sum
            S=[]
            #quando b for 0 quer dizer que ja passou voltando pelos itens que eram verdadeiros
            while b > 0:
                if matriz[m-1][b]:
                    m=m-1
                else:
                    m=m-1
                    S.append(set[m])
                    b=b-set[m]
            print(S)
    return matriz[n][sum]

sum=int(input("digite a soma"))
set=[int(s) for s in input("digite os números do set:").split()]
n=len(set)

if (subsetsum(set, n, sum) == True):
    print("existe um subset")
else:
    print("não existe um subset")
