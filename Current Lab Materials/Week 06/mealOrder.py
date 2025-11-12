def makeEmptyOrder():
    return ()

def add_burgerToOrder(order,burger):
    return order + (burger,)

def printReceipt(order):
    return None

def removeOrder(order):
    return ()

def enoughMoney(order,moneyInMyPocket):
    return False


def burgerPrice(burger):
    price = 0
    for char in burger:
        if char == 'B':
            price += 0.5
        elif char == 'C':
            price += 0.8
        elif char == 'P':
            price += 1.5
        elif char == 'V':
            price += 0.7
    return price

myOrder = makeEmptyOrder()
myOrder = add_burgerToOrder(myOrder,'BVPB')
myOrder = add_burgerToOrder(myOrder,'BCPCPB')
