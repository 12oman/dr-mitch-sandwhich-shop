from glob import has_magic


def user_input():
    run = True
    list = []
    while run:
        i_user = input("please enter stuff: ")
        print(len(i_user))
        length = len(i_user)
        if(length > 0):
            list.append(i_user)
        else:
            run = False

    return list

def order(_input):
    order = []
    order.append(_input)  

    print(f"You ordered a {order}")
    return order
    
order(user_input())

