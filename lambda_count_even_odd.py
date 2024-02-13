#count no. of even odd no.s usi ng lambda.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

is_even = lambda x: x % 2 == 0

even_count = len(list(filter(is_even, numbers)))
odd_count = len(numbers) - even_count

print("Number of even numbers:" ,even_count)
print("Number of odd numbers:",odd_count)
