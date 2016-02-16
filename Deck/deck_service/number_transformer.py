NUMBER_MAPPING = {
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

BIG_NUMBER_MAPPING = {
    'thousand': 1000,
    'million': 10 ** 6,
}
HUNDRED = 'hundred'


class NumberTransformer(object):
    """
    Transforms words to number
    """

    @classmethod
    def transform(cls, name):
        ten = 0
        hund = 0
        rez = []

        for num in cls._split_name(name):
            units = NUMBER_MAPPING.get(num, None)

            if cls._is_tens(units):
                ten += units

            elif cls._is_hundreds(num, ten):
                ten *= 100

            elif cls._is_big(num):
                ten *= BIG_NUMBER_MAPPING.get(num)
                hund += ten
                ten = 0

            else:
                rez.append(num)

        if ten + hund != 0:
            rez.append(ten + hund)

        return rez

    @classmethod
    def _is_big(cls, num):
        return num in BIG_NUMBER_MAPPING

    @classmethod
    def _is_hundreds(cls, num, ten):
        return num == HUNDRED and ten != 0

    @classmethod
    def _is_tens(cls, units):
        return units is not None

    @staticmethod
    def _split_name(name):
        return [word.lower() for word in name.split()]

