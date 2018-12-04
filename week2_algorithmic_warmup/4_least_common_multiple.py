# python3

#Euclidian algorighm
def lcm(a, b):
    a1=a
    b1=b
    while b!=0:
        (a,b)=(b,a%b)

    return a1*b1//a

n =input()
a, b = map(int, n.split())
print(lcm(a, b))


    