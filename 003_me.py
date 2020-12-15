# Largest prime factor

import math

# nu_in = input("Enter you'r Number for get Largest prime factor?\n-->")
# nu = int(nu_in)

nu = 13195
#nu = 600851475143

number_list = [1, 2, 5, 7, 11]

for nu_get in range(3, nu+1):
    if nu_get > 1 and nu_get < nu and nu % nu_get != 0 and nu % nu_get != 0:
        continue
    if nu_get % 2 != 0 and nu_get % 5 != 0 and nu_get % 7 != 0 and nu_get % 11 != 0:
        if int(math.sqrt(nu_get)) != float(math.sqrt(nu_get)) and int(nu_get ** (1. / 3)) != float(nu_get ** (1. / 3)):
                if nu % nu_get == 0:
                    number_list.append(nu_get)
                    print(number_list)

# print(number_list)

prime_number = []

for number in number_list:
    factor = []
    for number_quotient in range(1, number+1):
        if number % number_quotient == 0:
            # print(number, " -> ", number_quotient)
            factor.append(number_quotient)
            if number_quotient == number and len(factor) == 2:
                # print(factor)
                # print(number_quotient)
                prime_number.append(number_quotient)

# print("Prime number: ", prime_number)

prime_factor = []
for i in prime_number:
    if nu % i == 0:
        prime_factor.append(i)

print(prime_factor)
