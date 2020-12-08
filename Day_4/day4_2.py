#Part 2
import re
from time import perf_counter

def p2():
    def is_valid_height(s):
        n, unit = int(s[:-2]), s[-2:]
        if unit == 'cm':
            return 150 <= n <= 193
        if unit == 'in':
            return 59 <= n <= 76


    REQUIRED_FIELDS = {
        "byr": lambda s: 1920 <=int(s) <= 2002, 
        "iyr": lambda s: 2010 <=int(s) <= 2020, 
        "eyr": lambda s: 2020 <=int(s) <= 2030, 
        "hgt": is_valid_height,
        "hcl": lambda s: re.match(r'^#[\da-f]{6}$', s),
        "ecl": lambda s: s in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
        "pid": lambda s:re.match(r'^\d{9}$', s),
    }

    passports = [chunk.split() for chunk in open("day4").read().split("\n\n")]

    def is_valid_passport(passport):
        data = dict(line.split(':')  for line in passport)
        for field, func in REQUIRED_FIELDS.items():
            try:
                if not func(data[field]):
                    return False
            except:
                return False
        return True
    start_timer = perf_counter()
    ans = (len([True for p in passports if is_valid_passport(p)]))

    print(f"Result Part 2: {ans}")
    end_timer = perf_counter()
    print(f'Time of execution {round(end_timer - start_timer, 5)} seconds')

