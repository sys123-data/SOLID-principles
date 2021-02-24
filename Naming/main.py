from mypackage.my_sum import gauss_sum

class MyClass:# class
    def __init__(self):
        self.__var1 = 100 # wont be accessible with assignment
        self.val1 = 2*self.__var1
def print_hi(name): #method
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    x = 10 # variable
    x_1 = 0 # variable
    SPEED_OF_LIGHT = 3*(10**8) # Constants
    X = MyClass()
    print(X.val1) # print 200
    # print(X.__var1) # AttributeError: 'MyClass' object has no attribute '__var1'
    x1 = '.1'
    print(f'S({x1}) = ',gauss_sum(x1))
    x1 = ',1'
    print(f'S({x1}) = ', gauss_sum(x1))
    x1 = '..1'
    print(f'S({x1}) = ',gauss_sum(x1))
    x1 = '.,1'
    print(f'S({x1}) = ',gauss_sum(x1))
    x1 = '.2,1'
    print(f'S({x1}) = ',gauss_sum(x1))
    x1 = ',2,1'
    print(f'S({x1}) = ',gauss_sum(x1))
    x1 = '7,19782315724567294'
    print(f'S({x1}) = ',gauss_sum(x1))
    x1 = '7.19782315724567294'
    print(f'S({x1}) = ',gauss_sum(x1))
    x1 = '22'
    print(f'S({x1}) = ',gauss_sum(x1))
    x1 = 3
    print(f'S({x1}) = ',gauss_sum(x1))
    x1 =3.1
    print(f'S({x1}) = ',gauss_sum(x1))
    x1 =3,1
    print(f'S({x1}) = ',gauss_sum(x1))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
