def highest_number_with_digits_of(num):
    new_num = "%04d" % (num)
    arranged = sorted(list(new_num), reverse=True)
    return int(''.join(arranged))

def lowest_number_with_digits_of(num):
    new_num = "%04d" % (num)
    arranged = sorted(list(new_num), reverse=False)
    return int(''.join(arranged))

def krapekar(number):
    count = 0
    while number != 6174:
        high = highest_number_with_digits_of(number)
        low = lowest_number_with_digits_of(number)
        last = number
        number = high - low
        count += 1
        if number == last:
            return -1
    return count

quantity = int(raw_input())
for i in range(quantity):
    number = int(raw_input())
    print "Caso #%d: %d" % (i+1, krapekar(number))
    