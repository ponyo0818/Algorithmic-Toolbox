# python3

#Euclidian algorighm
def gcd(a, b):
    while b!=0:
        (a,b)=(b,a%b)
# =============================================================================
#     if a==1:
#         return ('the dont have common non-trivial divisors')
#     else:
# =============================================================================
    return a
    

n =input()
a, b = map(int, n.split())
print(gcd(a, b))
