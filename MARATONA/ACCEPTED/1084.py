def push(digit, my_list, size):
    i = 1

            

while True:
    total_digits, digits_to_erase = map(int, raw_input().split())
    if total_digits == digits_to_erase == 0:
        break
    number = list(raw_input())
    erased = 0
    to_print = [number[0]]
    size = 1
    to_print_size = total_digits - digits_to_erase
    for i in range(1, total_digits):
        j = size - 1
        while j >= 0 and erased <= digits_to_erase:
            #print i, j, to_print, size, erased, digits_to_erase, number[i]
            if size > 0 and to_print[j] < number[i] and erased < digits_to_erase:
                #print "erased"
                erased += 1
                size -= 1
                to_print.pop()
            if size == 0 or to_print[j-1] >= number[i] or erased == digits_to_erase:
                #print "appended"
                to_print.append(number[i])
                size += 1
                break
            j -= 1

    print "".join(to_print)[:to_print_size]