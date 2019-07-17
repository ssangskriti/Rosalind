


def insort(num):
    swap=0
    i=1
    while i < (len(num)):
        k=i
        while k>0 and num[k]<num[k-1] :

            p = num[k]
            num[k] = num[k-1]
            num[k-1] = p

            swap = swap +1

            k = k-1
        i = i+1

    return swap


array = []

n= int (input())

x = str(input())
x = x.split()
array = [int(i) for i in x]




r= insort(array)

print (r)
