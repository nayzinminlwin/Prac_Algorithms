intArr = [1,2,3,4,5]
print(intArr)
prefix_sum = [0]*(len(intArr))

prefix_sum[0] = intArr[0]

for i in range(1,len(intArr)):
    prefix_sum[i] = prefix_sum[i-1] + intArr[i]

print(len(prefix_sum),prefix_sum)