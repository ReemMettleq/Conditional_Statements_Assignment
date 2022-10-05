numbers = []
while len(numbers) < 5:
    number = int(input("Enter number: "))
    numbers.append(number)

max_value = max(numbers)
min_value = min(numbers)

print("Maximum value= ", max_value)
print("Minimum value= ", min_value)
