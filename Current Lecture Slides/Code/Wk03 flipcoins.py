from random import randint

def flip_coins():
    print("Flipping 1000 coins")

    num_heads = 0
    for flip in range(0,1000):
        if randint(0,1)==1:
            num_heads = num_heads + 1
    print(num_heads)


flip_coins()

