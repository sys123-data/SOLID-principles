class User:
    def __init__(self, name):
        self.name = name

    def get_acc_info(self):
        print('User info')

    def create_new_table(self):
        print('Table created')

class Admin(User):
    def __init__(self, name):
        super().__init__(name)
        self.user_status = 'admin'

    def rename(self):
        self.name = input('Please provide new name: ')

    def delete_account(self):
        pass
    def delete_table(self,id):
        print(f'Table with id: {id} - deleted')


class VipUser(User):
    def __init__(self, name):
        super().__init__(name)
        self.user_status = 'vip'

    def check_vip(self):
        if self.user_status == 'user': return False
        return True

    def remove_vip(self): self.user_status = 'user'

    def try_remove_vip(self):
        if self.check_vip(): self.remove_vip()

x = VipUser('abc')
print(x.user_status)
x.try_remove_vip()
print(x.user_status)
x = Admin('abc')
print(x.name)
x.rename()
print(x.name)
