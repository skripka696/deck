
def transform(name):
    unit = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'ten': 10,
        'eleven': 11,
        'twelve': 12,
        'thirteen': 13,
        'fourteen': 14,
        'fifteen': 15,
        'sixteen': 16,
        'seventeen': 17,
        'eighteen': 18,
        'nineteen': 19,
        'twenty': 20,
        'thirty': 30,
        'forty': 40,
        'fifty': 50,
        'sixty': 60,
        'seventy': 70,
        'eighty': 80,
        'ninety': 90,
    }

    big = {
        'thousand': 1000,
        'million': 10 ** 6,
    }
    all_name = name

    numbers = [name.lower() for name in name.split()]

    ten = 0
    hund = 0

    # for num in numbers:
    #     units = unit.get(num, None)
    #     if units is not None:
    #         ten += units
    #     elif num == 'hundred' and ten != 0:
    #         ten *= 100
    #
    #     elif num == 'thousand':
    #         ten *= 1000
    #         hund += ten
    #         ten = 0
    #     elif num == 'million':
    #         ten *= 1000000
    #         hund += ten
    #         ten = 0
    #     else:
    #         return all_name
    for num in numbers:
        units = unit.get(num, None)
        if units is not None:
            ten += units
        elif num == 'hundred' and ten != 0:
            ten *= 100
        elif big.get(num, None):
            ten *= big.get(num, None)
            hund += ten
            ten = 0
        else:
            return all_name


    print ten+hund
    return ten+hund
