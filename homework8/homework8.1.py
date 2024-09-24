numbers: list[int] = []
num: int = 0
for i in range(100):
    num += 1
    numbers.append(num)
print(f"the numbers are:{numbers} ")
print("the first number is:", numbers[0])
print("the last number is:", numbers[-1])
print(f"the amount of numbers in a list is:{len(numbers)}")
print("numbers from 3-12:", numbers[2:12])
print("numbers from 80:", numbers[79:])
print("numbers till index 17:", numbers[:17])
print("numbers from in a opposite order:", numbers[::-1])
print("even numbers in this list are:", numbers[1::2])
print("numbers that can be divided by 3 are:", numbers[2::3])
print("numbers that can be divided by 7 are:", numbers[6::7])
print("numbers that multiply by 10 are:", numbers[9::10])
print("numbers from 99-66 in jumps of 3:", numbers[98:64:-3])
numbers.insert(50, 999)
print(numbers)
numbers.pop(100)
print(numbers)
