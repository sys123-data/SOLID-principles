# classes modules functions should be open for extension but closed for modification
import re

def special_match(strg, search=re.compile(r'[^a-z]').search):
    '''
    :param strg: the string
    :param search: should have !!!!only!!!! [0-9] and ( ,. or , or . or '' )
    :return: True or False
    '''
    return not bool(search(strg))


class MyClass:
    def __init__(self):
        self.__name = 'abc'
        self.categories = {'A','B','C'}

    def print_name(self):
        print(self.__name)


    def get_input(self):
        return input('Please provide name: ')

    def test_input(self,x):
        return special_match(x)

    def change_name(self):
        x = self.get_input()
        if self.test_input(x): self.__name = x

    def print_categories(self):
        print(self.categories)
    def print_form(self):
        for _ in self.categories:
            self.show_element(_)
    def show_element(self,_):
        print('------*',_,'*------')

User1 = MyClass()
User1.categories.add('D')
User1.print_categories()
User2 = MyClass()
User2.print_categories()
User3 = MyClass()
User3.categories1 = {'1','2','3'}
print(User3.categories1)
User3.print_form()