"""
This is a test file for singly_linked_list.py
"""
import singly_linked_list

mysll = singly_linked_list.SLL()
mysll.addfront(0)
mysll.addfront(1)
mysll.addfront(2)
mysll.addback(3)
print(mysll)

mysll.reverse()
print('reversed list: {}'.format(mysll))

print('result for find(2) is {}'.format(mysll.find(2))) 
print('result for find(10) is {}'.format(mysll.find(10)))

mysll.remove(2)
print('mysll after remove 2: {}'.format(mysll))

mysll.remove(10)
print('mysll after remove 10: {}'.format(mysll))