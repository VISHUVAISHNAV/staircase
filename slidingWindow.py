def maxSubarraySum(arr,num):
    maxsum = 0
    tempsum = 0
    if len(arr)<num:
        return False
    for i in range(0,num):
        maxsum+=arr[i]
    tempsum=maxsum
    for i in range(num,len(arr)):
        tempsum = tempsum - arr[i-num] + arr[i]
        maxsum=max(maxsum,tempsum)
    
    return maxsum  
