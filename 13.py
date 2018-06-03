def bf(adj_list,n,s):
  distance = [999 for i in range(n+1)]
  path = [[None] for i in range(n+1)]
  path[s] = [s]
  distance[s] = 0
  for i in range(n-1):
    for pair in adj_list:
      tmp = distance[pair[1]]
      distance[pair[1]] = min(distance[pair[1]],distance[pair[0]]+pair[2])
      if tmp != distance[pair[1]]:
        path[pair[1]] = path[pair[0]]+[pair[1]]
  del(distance[0])
  del(path[0])
  print(distance)
  for i in path:
    print(s,"--->",path.index(i)+1,":",i)
def main():
  adj_list = []
  n = int(input("Enter number of vertices"))
  e = int(input("Enter number of edges"))
  for i in range(e):
    print("For edge ",i+1,":")
    u = int(input("Enter first vertice:"))
    v = int(input("Enter second vertice:"))
    w = int(input("Enter weight"))
    adj_list.append([u,v,w])
  print(adj_list)
  s = int(input("Enter the source"))
  bf(adj_list,n,s)
main()
