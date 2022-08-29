import math

def letter_count(n):
    """Counts the number of letters when a positive integer n <= 1000 is written out in words
    The spelling is based on British English, which means that 'and' is part of the spelling"""

    digits = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    tens   = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    if n <= 10:
        return len(digits[n])
    elif n == 11:
        return 6  # eleven
    elif n == 12:
        return 6  # twelve
    elif n == 13:
        return 8  # thirteen
    elif n == 14:
        return 8  # fourteen
    elif n == 15:
        return 7  # fifteen
    elif n == 16:
        return 7  # sixteen
    elif n == 17:
        return 9  # seventeen
    elif n == 18:
        return 8  # eighteen
    elif n == 19:
        return 8  # nineteen
    elif n < 100:
        return len(tens[n // 10 - 2]) + len(digits[n % 10])
    elif n == 1000:
        return 11  # one thousand
    else:
        # the first part corresponds to the "something hundred" and the second part corresponds to "and something"
        return (len(digits[n // 100]) + 7) + ((3 + letter_count(n % 100)) if n % 100 != 0 else 0)

# letter_count(115)  # test case
sum([letter_count(n) for n in range(1, 1001)])
