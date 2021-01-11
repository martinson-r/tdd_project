# def parse(numeral):
#     if numeral == "I":
#         return 1
#     elif numeral == "II":
#         return 2
#     elif numeral == "III":
#         return 3
#     elif numeral == "IV":
#         return 4
#     elif numeral == "V":
#         return 5
#     elif numeral == "VI":
#         return 6
#     elif numeral == "VII":
#         return 7
#     elif numeral == "VIII":
#         return 8


def parse(numeral):
    roman_numerals = {
        "I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8
    }
    for key in roman_numerals:
        if numeral == key:
            return roman_numerals[key]
