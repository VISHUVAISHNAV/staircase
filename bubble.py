arr = list(map(int,input("Enter : ").split()))

for i in range(len(arr),-1,-1):
    #print(arr)
    for j in range(0,i-1,1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            
print(arr)
