# SOLID principles and Naming Convention in python
 [SOLID-principles](https://github.com/georgecristian97/SOLID-principles/blob/main/SOLID%20Principles%20with%20Python%20Examples.md) 



[Naming convention](https://github.com/georgecristian97/SOLID-principles/tree/main/Naming)



:star: [SRP](https://github.com/georgecristian97/SOLID-principles/tree/main/SOLID%20Demos/SRP):

O metoda contine o singura functionalitate

OPEN SQLITE -> new db	

Username text PK

Password 

EmailID

:star:[ISP](https://github.com/georgecristian97/SOLID-principles/tree/main/SOLID%20Demos/ISP):

Dupa mostenirea unei clase obiectul are acces limitat conform drepturilor acestuia.

```python
class User:
  def __init__(self,name):
    self.name = name
    self.user_status = 'user'
  def get_acc_info(self)
    print('User info')
    

class Admin(User):
	def delete_account(self)
		pass
  
class VipUser(User):
  def __init__(self,name):
    super().self.__init__(self,name)
    
  def remove_vip(self)
  	self.user_status = 'user'
```

