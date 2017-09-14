# Author : André Ramos Neves TIA : 41445368
import numpy as np

def jacobi(A,TOL,N):
    #Step 1
    n,m = np.shape(A)
    #Step 1 Inicializo minha primeira iteração com 0
    k = 1
    x = [0 for y in range(n)]
    xo = [0 for y in range(n)]
        #Step 2  Para cada equação
    while(k<=N):
        for i in range(n):
            somatoria = 0
        #Step 3
            temp = A[i][i]
            b = A[i][n]/temp	
            for j in range(0,len(x)):
                if(j != i):
                    somatoria = somatoria + (-1*A[i][j]/temp)*xo[j]
            x[i] = somatoria + b
        #Step 4
        if (dif_norma_inf(x,xo)/max(x)) < TOL:
            print("Tolerancia atingida ")
            return x
        #Step 5
        k += 1
        #Step 6
        xo = [0 for y in range(n)]
        for  i in range(n):
            xo[i] = x[i]
    return x
    
def dif_norma_inf(x,xo):
  dif = 0;
  for i in range(len(x)):
    if(i == 0 or abs(x[i] - xo[i]) > dif ):
      dif = abs(x[i]-xo[i])
  return dif      

print(jacobi(np.array([[10.0,-1,2,0,6],
                     [-1,11,-1,3,25],
                     [2,-1,10,-1,-11],
                     [0,3,-1,8,15]]),.001,9))