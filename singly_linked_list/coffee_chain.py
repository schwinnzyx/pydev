
"""
@ Schwinn Zhang
apply singly-linked-list to create a coffee chain
"""
import singly_linked_list

# CoffeeShop becomes the data that Node object holds
class CoffeeShop(object):
  def __init__(self, id, name, addr, owner):
    self.id = id
    self.name = name
    self.addr = addr
    self.owner = owner
  
  def __str__(self):
    return "id:{}, name:{}, address:{}, owned by: {}".format(self. id, \
                                     self.name, self.addr,self.owner)
  
  def __repr__(self):
    return self.__str__()

# CoffeeChain inherits from SLL, singly-linked-list
class CoffeeChain(singly_linked_list.SLL):
  def __init__(self, name):
    super().__init__()
    # self.head
    self.name = name
    self.id = 0
    self.num_of_stores = 0
  
  def add(self, addr, owner):
    self.id += 1
    self.num_of_stores += 1
    new_shop = CoffeeShop(self.id, self.name, addr, owner)
    
    self.addback(new_shop)
    
    # set the first shop as headquarter
    if self.id == 1:
      self.headquarter = new_shop
    
  def find(self, id):
    
    cur = self.head.next
    
    while(cur):
      if cur.data.id == id:
        return cur.data
      
      cur = cur.next
    return "Id Not Found"
  
  def shutdown(self, id):
    shop = self.find(id)
    if shop != 'Id Not Found':
      self.remove(shop)
      self.num_of_stores -= 1
    
  def __str__(self):
    message = ''
    cur = self.head.next
    while(cur):
      message += cur.data.__str__() + '\n'
      cur = cur.next
    return message
  
  def __repr__(self):
    return self.__str__()


if __name__ == "__main__":
	print("create a CoffeeChain object called 'Starocks'")
	my_coffee_chain = CoffeeChain("Starocks")

	print('open 4 stores')
	my_coffee_chain.add('10 NY', 'Max')
	my_coffee_chain.add('5 Queens', 'Marry')
	my_coffee_chain.add('15 Dundas', 'Flix')
	my_coffee_chain.add('100 Washington', 'Nate')
	print(my_coffee_chain)

	print('find store with id number 2')
	my_coffee_chain.find(2)
	
	print('Where is the headquarter?')
	print(my_coffee_chain.headquarter)

	print('shut down the store with id 3')
	my_coffee_chain.shutdown(3)
	print(my_coffee_chain)
	

