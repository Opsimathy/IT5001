

def make_power_func(n):
    return lambda x:x**n

square = make_power_func(2)
cube = make_power_func(3)
square_root = make_power_func(0.5)

print(square(3))
print(cube(2))
print(square_root(16))

