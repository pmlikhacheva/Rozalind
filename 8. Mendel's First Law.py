#not ready
k = 2
m = 2
n = 2
sum = k+m+n
probability = (k*(k-1)+k*m+k*n+m*(m-1)*0.75+m*n*0.5)/(sum*sum-1)
print(probability)