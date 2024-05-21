def getEven(numbers):
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

numbers = [2, 5, 8, 10, 15, 12, 17, 20]

print("Even numbers in the list:", getEven(numbers))