
def binarySearch(arr, l, r, x):
    if r >= l:
        mid = (l+r)/2
        mid = int(mid)

        if arr[mid] == x:
            return mid+1
        elif arr[mid] > x:
            return binarySearch(arr, l, mid -1 , x)
        else:
            return binarySearch(arr, mid + 1, r, x)

    else: return -1

arr=[]
k=[]
n= int(input())
m= int(input())

x = str(input())
x = x.split()
arr = [int(i) for i in x]


x = str(input())
x = x.split()
p = [int(i) for i in x]

i=0
while i < m:
    s = p[i]
    value = binarySearch(arr, 0, n-1,  s)
    #print(value)
    k.append(value)
    i = i+1



i = 0
while i < m:
    print (k[i], end=" ")

    i = i+1



