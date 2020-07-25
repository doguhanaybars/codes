# import random 

# my_list = [1,2,3,4,5]
# print(random.shuffle(my_list))
# print(my_list)

import pyjokes

joke = pyjokes.get_joke('en','neutral')
print(joke)