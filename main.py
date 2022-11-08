# import utility
# from shopping.shopping_cart import buy

# print(shopping.shopping_cart.buy("apple"))  We only need this line if we import shopping_cart module from the shopping package

# print(buy('apple'))


# print(utility.this_here(1, 2, 3))

# print(utility.multiply(5, 10))


# if __name__ == '__main__':
#     print('please run this')

# The above line of code tells the program to only run this code if it is the main Python file

def do_stuff(num=0):
    try:
        if num:
            return int(num) + 5
        else:
            return 'please enter a number'
    except ValueError as err:
        return err