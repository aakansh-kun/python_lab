#write a program that count how many even and odd no.s in a list.
def count_even_odd(numbers):
    even = len([num for num in numbers if num % 2 == 0])
    odd = len(numbers) - even
    return even, odd

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even, odd = count_even_odd(numbers)
print("Number of even numbers: ", even)
print("Number of odd numbers: ", odd)
