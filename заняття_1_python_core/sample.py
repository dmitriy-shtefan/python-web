
# goods_list -> xxxxx
# goods_list -> yyyyy 1

goods_list = ['phone', 'TV', 'sofa']
print(id(goods_list))

goods_list.append('car')
print(id(goods_list))

goods_list = 1 # int
number_one = 1 # int

print(id(goods_list))
print(id(number_one))

print(goods_list)

goods_list = ['phone', 'TV', 'sofa']

for index, item in enumerate(goods_list):
    print(index, item)




goods_list.insert(0, 'bike')
print(goods_list)

fruits = ['apple', 'banana', 'orange']
goods_list.extend(fruits)
print(goods_list)

goods_list[1] = "iphone"
print(goods_list)

numbers = (1, 2, 3)
print(numbers)

numbers = (1, 2, 3)

print(numbers[0])
print(numbers.count(2))

a, b, c = numbers
print(a, b, c)

*a, b = numbers
print(a, b)


users = {
    'name': 'Alyona',
    'level': 'senior'
}

print(users['name'])

print(users.get('last name', 'Бенедюк'))

for key, value in users.items():
    print(key, value)

for key in users.keys():
    print(key, users[key])

for key in users:
    print(key, users[key])

for value in users.values():
    print(value)

fruits = ['apple', 'banana', 'orange', 'apple']
mySet = set(fruits)
print(mySet)

mySet.add('pear')
print(mySet)

mySet.remove('pear')
print(mySet)

mySet.discard('pear')
print(mySet)

mySet1 = {1, 2, 3, 4, 5}
print(mySet1)

mySet2 = {3, 4, 5, 6, 7}
print(mySet2)

mySet3 = mySet1.intersection(mySet2)
print(mySet3)

mySet3 = mySet1 & mySet2 # intersection | AND
print(mySet3)

mySet4 = mySet1.union(mySet2)
print(mySet4)

mySet4 = mySet1 | mySet2 # union | OR
print(mySet4)

# mySet1 = {1, 2, 3, 4, 5}
# mySet2 = {3, 4, 5, 6, 7}

mySet5 = mySet2.difference(mySet1)
print(mySet5)

mySet5 = mySet2 - mySet1 # difference
print(mySet5)

mySet6 = mySet1.symmetric_difference(mySet2)
print(mySet6)

mySet6 = mySet1 ^ mySet2 # symmetric difference | XOR
print(mySet6)