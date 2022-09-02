inp = [['A', 'Laptop'], ['A', 'Laptop'], ['A', 'Mouse'], ['B', 'Laptop'], ['A', 'Headset'], ['B', 'Headset']]
# Implement a logic which gives the following output
# out1 = [['A',4], ['B',2]]
# out2 = [['A','Laptop',2], ['A', 'Mouse',1], ['A','Headset',1], ['B','Laptop',1],
# ['B','Headset',1]]
# out3 = ['A','B',['Laptop','Headset']]]
counta = 0
countb = 0
out1 = []
for i in inp:
    for j in i:
        if j == "A":
            counta += 1
            out1.append(["A", counta])
        if j == "B":
            countb += 1
            out1.append(["B", countb])
out1.sort()
for i in range(len(out1)):
    if i < len(out1)-1:
        if out1[i][0] == out1[i + 1][0] and out1[i][1] < out1[i + 1][1]:
            out1.remove(out1[i])
for i in range(len(out1)-1):
    if i < len(out1)-1:
        if out1[i][0] == out1[i + 1][0] and out1[i][1] < out1[i + 1][1]:
            out1.remove(out1[i])
print(out1)

# ----------------------------------------------------------------------------
inp = [['A', 'Laptop'], ['A', 'Laptop'], ['A', 'Mouse'], ['B', 'Laptop'], ['A', 'Headset'], ['B', 'Headset']]
# Implement a logic which gives the following output
# out2 = [['A','Laptop',2], ['A', 'Mouse',1], ['A','Headset',1], ['B','Laptop',1],
# ['B','Headset',1]]
out2 = []
for i in inp:
    x = inp.count(i)
    out2.append([i[0],i[1],x])
for i in range(len(out2)):
    if i < len(out2)-1:
        if out2[i] == out2[i+1]:
            out2.remove(out2[i])
out2.sort()
print(out2)

#---------------------------------------------------------------------------------------------------------------------
# Implement a logic which gives the following output
# out3 = ['A','B',['Laptop','Headset']]]
inp = [['A', 'Laptop'], ['A', 'Laptop'], ['A', 'Mouse'], ['B', 'Laptop'], ['A', 'Headset'], ['B', 'Headset']]
out3 = []
inpa = []
inpb = []
nested_out3 = []
for i in range(len(inp)):
    if inp[i][0] == "A":
        inpa.append(inp[i])
    else:
        inpb.append(inp[i])
print(inpa, inpb)
for i in inpa:
    for j in inpb:
        if i[1] == j[1]:
            out3.append(i[0])
            nested_out3.append(i[1])

out3 = out3.append(nested_out3)
print(out3)

# -------------------------------------------------------------------------------
A = [1, 2, 3, 'ae']
B = [1, 1, 'b', 6]
# if alpha char exists then it should be treated as 0
# C = A + B if even otherwise 0
# 1) Get output C. With above example C = [2, 0, 0, 6]
# 2) An find out maximum repeated element in C
for (i,j) in zip(A,B):
    if i is str or (j is str):







# Program to find the largest sum of contiguous integers in the array. Example: if
# the input is (-10, 2, 3, -2, 0, 5, -15), the largest sum is 8




    


