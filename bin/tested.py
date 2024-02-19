def ten_to_two(number, system):
    res = ""
    divided = int(number)
    while divided != 0:
        res += str(divided % system)[::-1]
        divided //= system
    return(res[::-1])

print(ten_to_two("1000", 16))