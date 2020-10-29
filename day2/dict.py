numbers = [1,2,3]
h = {}
h ={x+1:(x+1)**2 for x in range(0,len(numbers))}
print(h)
list=[h[x] for x in h]
print(list)