
list1 = [(1, 2,3), [1,2], ['a','hit','less']] 

outer_list = [val for sublist in list1 for val in sublist] 
  
print(outer_list) 