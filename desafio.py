number_1 = int(input())
number_2 = int(input())

for num in range (number_1, number_2):
    if num > 5 and num % 2 == 0:
        print(f"First even number greater than 5: {num}")
        break
for num in range (number_1, number_2):
    if num % 7 == 0:
        print(f"First number divisible by 7: {num}")
        break