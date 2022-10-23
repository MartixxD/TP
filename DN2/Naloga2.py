import collections
our_list = [1,2,3,4,5,6,7]
our_dict = {
    "a": 2,
    "b": 5,
    "c": 8,
    "d": 12,
    "e": 357,
    "f": 12
}
our_tuple = (357, 12, 12, 8, 5, 2, 2)

temp = our_list[4]
print(our_list)
our_list.pop(4)
print(our_list)
print(temp)

print(our_dict)
our_dict.update({"d":temp})
print(our_dict)

new_tupl=[]

for item in our_dict.values():
    #print(item)
    new_tupl.append(item)

new_tupl.sort(reverse=True)
new_tup = tuple(new_tupl)

print(our_tuple)
print(new_tup)

list1=list(our_tuple)
list2=list(new_tup)

if collections.Counter(list1) == collections.Counter(list2):
    print ("Tupla sta enaka") 
else: 
    print ("Tupla nista enaka") 