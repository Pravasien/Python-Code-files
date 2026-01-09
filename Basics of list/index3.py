L=[4,5,1,2,9,7,10,8]
print("Original List:",L)
count=0
for i in L:
    count+=i
avg=count/len(L)
print("Average of the list is:",avg)
print("sum =",count)
L.sort()
print("Smallest element is:",L[0])
print("Largest element is:",L[-1])