### Setup: ###
from math import floor
### Read input: ###
with open('input.txt') as f:
    input = f.read()

input_by_line = input.strip().split('\n')

test_input = ['L68', 'L30','R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']
# input_by_line = test_input

### Part 1: ###

### Part 1: ###
dial = 50
count = 0
for i in input_by_line:
    print(f'Dial at: {dial}')
    print(f'Current instruction: {i}')
    if i[0] == 'R': mod = 1
    else: mod = -1

    dial += int(i[1:]) * mod
    if dial > 99 or dial < 0: dial = dial % 100
    print(f'Result: {dial}')
    
    if dial == 0: count += 1

print(count)

### Part 2: ###
dial2 = 50
count2 = 0
for i in input_by_line:
    print(f'Dial2 at: {dial2}')
    print(f'Current instruction: {i}')
    if i[0] == 'R': mod = 1
    else: mod = -1
    keep = dial2

    # positive or negative instruction
    change = int(i[1:]) * mod
    # add 100s to change, retain remainder
    count2 += floor(abs(change/100))
    change = change % (100 * mod)

    dial2 += change
    print(f'Dial sum: {dial2}')
    if dial2 > 99 and dial2 % 100 != 0: 
        count2 += 1
    if dial2 < 0 and keep != 0:
        count2 += 1
            
    dial2 = dial2 % 100
    print(f'Result: {dial2}')
    
    if dial2 == 0: 
        count2 += 1
    print(f'-- Current count: {count2}')

print(count2)