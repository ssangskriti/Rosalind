fibo = {}

fibo[0]=0
fibo[1]=1

n=input()
n=int(n)

if n > 1:
    i = 2
    while i <= n:
        fibo[i] = fibo[i-1] + fibo[i-2]
        i = i+1



print (fibo[n])