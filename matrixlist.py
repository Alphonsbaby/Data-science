input_string = input('Enter elements of a list separated by space ')
print("\n")
x = input_string.split()
# print list
print('list: ', x)

for i in range(len(x)):

    x[i] = int(x[i])
input_string1 = input('Enter elements of a list separated by space ')
print("\n")
y = input_string1.split()
# print list
print('list: ', y)

for i in range(len(y)):
    y[i] = int(y[i])
res = [[0,0,0],
       [0,0,0],
       [0,0,0]]

for i in range(len(x)):
  for j in range(len(x[0])):
    res[i][j] = x[i][j] + y[i][j]
for r in res:
  print(r)