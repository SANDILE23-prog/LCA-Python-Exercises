fruits = ['banana', 'apple', 'pear']
fruits.append('orange')
fruits.insert(0, 'grape')
fruits.remove('apple')
print(fruits)
#
numbers = list(range(1, 6))
squared_numbers = [num**2 for num in numbers]
total_sum = sum(numbers)
average = total_sum / len(numbers)
print(numbers)
print(squared_numbers)
print(total_sum)
print(average)
#
country_capitals = {
    'Japan': 'Tokyo',
    'Spain': 'Madrid'
}
country_capitals['Nigeria'] = 'Lagos'
country_capitals['Spain'] = 'Barcelona'
del country_capitals['Japan']
print(country_capitals)
#
fruits_colors ={
    'Apple': 'Green',
    'Banana' : 'yellow',
    'Lemon' : 'green'
}
print('Fruits', list(fruits_colors.keys()))
print('Colors', list(fruits_colors.values()))
for fruit, color in fruits_colors.items(): print ('{fruit}: {color}')
