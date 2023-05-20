# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

n = int(input("Chocolate bar size n "))
m = int(input("Chocolate bar size m "))
k = int(input("Chocolate bar size k "))

if k < m*n and (k%m==0 or k%n==0):
    print("MAY")
else:
    print("CANNOT")