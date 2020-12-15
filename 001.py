# Multiples of 3 and 5
multiples_sum = 0
for number in range(1, 1000):
    if number % 3 == 0 or number % 5 == 0:
        multiples_sum += number
        # print(number)

print(multiples_sum)