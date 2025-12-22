# Task 1: Numbers divisible by 4 between 30-80
print("Numbers divisible by 4 between 30-80:")
for num in range(30, 81):
    if num % 4 == 0:
        print(num, end=", ")
print()  # new line

# Task 2: First 8 odd numbers from 15
print("\nFirst 8 odd numbers from 15:")
for num in range(15, 30, 2):  # 15 to 29 stepping by 2
    print(num, end=", ")
print()

# Task 3: Counting backwards, divisible by 5
print("\nCounting backwards, divisible by 5:")
for num in range(50, 9, -5):  # 50 to 10 stepping by -5
    print(num, end=", ")
print()

# Task 4: Product of numbers divisible by 3
print("\nProduct of numbers divisible by 3 (1-30):")
product = 1
for num in range(3, 31, 3):  # stepping by 3 directly
    product *= num
print(product)