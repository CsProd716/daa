n = int(input("Enter the number of items"))
W = int(input("Enter the Knapsack Capacity"))
items = [0]
values = [0]
weights = [0]
for i in range(1,n+1):
  items.append(i)
  print("Enter the weight of item ",i," :")
  wi = int(input())
  weights.append(wi)
  print("Enter the value of item ",i," :")
  vi = int(input())
  values.append(vi)
print(items)
print(weights)
print(values)
M = [[0 for i in range(W+1)] for j in range(n+1)]
i = 1
while i <= n:
  x = 1
  while x <= W:
    if weights[i] > x:
      M[i][x] = M[i-1][x]
    else:
      M[i][x] = max(M[i-1][x],values[i]+M[i-1][x-weights[i]])
    x = x+1
  i = i+1
print(M)
print("Max Value:",M[n][W])
i = n
k = W
cont = []
while i>0 and k>0:
  if M[i][k]!=M[i-1][k]:
    cont.append(i)
    k = k-weights[i]
    i = i -1
   else:
    i = i-1
print("Items in the Knapsack:")
print(cont)
    
