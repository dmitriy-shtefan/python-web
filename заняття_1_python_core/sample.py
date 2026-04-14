
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

print(numbers[0])
print(numbers.count(2))

a, b, c = numbers
print(a, b, c)

*a, b = numbers
print(a, b)