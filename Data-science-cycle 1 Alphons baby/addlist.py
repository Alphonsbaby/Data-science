l = [5,6,7,8]
k=[1,2,3,4]
print("list 1 element ", l)
print("list 2 element", k)
res_list = [l[i] + k[i] for i in range(len(l))]

print("Resultant list is : " + str(res_list))