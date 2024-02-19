import logging
import config


async def calculate(problem):
    try:
        response = eval(problem)
        return response

    except Exception as e:
        logging.error(e)


async def calculate_extended(data):
    first_to_ten = ""
    second_to_ten = ""
    result = ""
    operations_dict = {"plus": "+",
                       "minus": "-",
                       "divide": "//",
                       "multiply": "*"}
    try:
        if data[0] == "first_two":
            first_to_ten = transform_to_ten(data[1], 2)
        elif data[0] == "first_eight":
            first_to_ten = transform_to_ten(data[1], 8)
        elif data[0] == "first_sixteen":
            first_to_ten = transform_to_ten(data[1], 16)
        elif data[0] == "first_ten":
            first_to_ten = data[1]

        if data[2] == "second_two":
            second_to_ten = transform_to_ten(data[3], 2)
        elif data[2] == "second_eight":
            second_to_ten = transform_to_ten(data[3], 8)
        elif data[2] == "second_sixteen":
            second_to_ten = transform_to_ten(data[3], 16)
        elif data[2] == "second_ten":
            second_to_ten = data[3]

        res_ten = str(eval(f"{first_to_ten} {operations_dict[data[4]]} {second_to_ten}"))

        if data[5] == "answer_two":
            result = from_ten_to_ans(res_ten, 2)
        elif data[5] == "answer_eight":
            result = from_ten_to_ans(res_ten, 8)
        elif data[5] == "answer_sixteen":
            result = from_ten_to_ans(res_ten, 16)
        elif data[5] == "answer_ten":
            result = res_ten

        return result

    except Exception as e:
        logging.error(e)


def transform_to_ten(number, system):
    res = 0
    mult = len(number) - 1
    for symbol in number:
        res += int(symbol) * system ** mult
        mult -= 1
    return res


def from_ten_to_ans(number, system):
    res = ""
    divided = int(number)
    while divided != 0:
        res += str(divided % system)[::-1]
        divided //= system
    return (res[::-1])
