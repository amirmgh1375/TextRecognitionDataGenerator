from random import randint

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return str(randint(range_start, range_end))

f = open('fake_shaba_numbers.txt', 'w')
for i in range(1000000):
    random_number = random_with_N_digits(24)
    #shaba_final = "IR" + str(random_number) + '\n'
    shaba_final = "IR" + random_with_N_digits(2) + ' ' + random_with_N_digits(4) + ' ' + random_with_N_digits(4) + ' ' + random_with_N_digits(4) + ' ' + random_with_N_digits(4) + ' ' + random_with_N_digits(4) + ' ' + random_with_N_digits(2) + '\n'
    f.write(shaba_final)

