import sys
from os import path, getcwd
from time import perf_counter
from day4_2 import *

HAS_TO_HAVE = ['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']

def read_file(filename):
    with open(filename) as f:
        content = f.readlines()

    content = [info.strip() for info in content]
    return content
    
def handle_refactor_info_item(data_input):
  result = []
  data_line = dict()

  for line in data_input:
    if line != '':
      for item in line.split(' '):
        key, value = item.split(':')
        data_line[key] = value
     
    else:
      result.append(data_line)
      data_line = dict()
  
  if data_line != {}:
    result.append(data_line)

  return result

def find_valid_passports(data):
  count_valid_passports = 0
  
  for item in data:
    item_sorted = sorted(item, key=str.lower)
    items = [item for item in item_sorted if item != 'cid']

    if set(HAS_TO_HAVE) == set(items):
      count_valid_passports += 1

  return count_valid_passports

if __name__ == "__main__":
    start_timer = perf_counter()

    filename = path.join(getcwd(), 'day4')
    input_data = read_file(filename)

    data_refactored = handle_refactor_info_item(input_data)

    result = find_valid_passports(data=data_refactored)

    print(f'Result Part 1: {result}')
    end_timer = perf_counter()
    print(f'Time of execution {round(end_timer - start_timer, 5)} seconds')

    p2()