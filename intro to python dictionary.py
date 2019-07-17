
s= input()

dict={}


for word in s.split(' '):
    if word in dict:
        dict[word]=dict[word]+1
    else :
        dict[word]=1


for key, value in dict.items():
    print (key, value)
