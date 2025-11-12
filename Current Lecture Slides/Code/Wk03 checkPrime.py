
def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def is_prime(n):
    divisible_by_some = False
    for i in range(2,n):
        if n%i==0:
            return False
    return not divisible_by_some


for i in range(2,20):
    if is_prime(i):
        print(i)

