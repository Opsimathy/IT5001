from time import time

# you can import the math package and the math package ONLY

def LCM(S):
    return 1

'''
print("Example:")
print(LCM([2,3,4,2]))
# ans = 12
print(LCM([399,772,163,959,242]))
# ans = 832307365428
print(LCM([2,3,7,11,19,23,29,4]))
# ans = 11709852

'''

# Test code for the final part timing

'''
for k in range(1,10):        
    longl = [i for i in range(3,25000*k+2,5)]
    st = time()
    lastTenDigits = LCM(longl)%(10**10)
    print(f'List size = {len(longl)}:Last 10 digits = {lastTenDigits}, time taken = {time()-st:.2f}s')
    
'''


### Results for you to reference
'''
List size = 5000:Last 10 digits = 5784823808, time taken = 0.03s
List size = 10000:Last 10 digits = 4849531904, time taken = 0.08s
List size = 15000:Last 10 digits = 8952091648, time taken = 0.14s
List size = 20000:Last 10 digits = 1723308032, time taken = 0.22s
List size = 25000:Last 10 digits = 2434705408, time taken = 0.31s
List size = 30000:Last 10 digits = 2554353664, time taken = 0.41s
List size = 35000:Last 10 digits = 467366912, time taken = 0.52s
List size = 40000:Last 10 digits = 7877574656, time taken = 0.65s
List size = 45000:Last 10 digits = 8441117696, time taken = 0.78s
'''
