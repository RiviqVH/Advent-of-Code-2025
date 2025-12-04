### Setup: ###
### Read input: ###
with open('input.txt') as f:
    input = f.read()
    
input_by_line = input.strip().split('\n')

test_input = ['987654321111111',
'811111111111119',
'234234234234278',
'818181911112111']

# input = test_input
input = input_by_line

### Part 1: ###
total = 0
for i in input:
    joltage = ['','']
    # first scan
    first = -1
    index_first = -1

    for idx, c in enumerate(list(i)[:-1]):
        if c == '9':
            joltage[0] = '9'
            index_first = idx
            break
        if int(c) > first:
            first = int(c)
            index_first = idx
            joltage[0] = c
    
    # second scan
    second = -1
    for k in list(i)[index_first+1:]:
        
        if k == '9':
            joltage[1] = '9'
            break
        if int(k) > second:
            second = int(k)
            joltage[1] = k

    print(f'Joltage: {int(''.join(joltage))}')
    total += int(''.join(joltage))
print(total)

### Part 2: ###
total2 = 0
sequence_length = 12
for i in input:
    print(f'Working on: {i}')
    joltage2 = [''] * sequence_length
    list_i = list(i)
    prev_index = -1
    # scan loop
    for l in range(0, sequence_length):
        print(f'Loop number {l}')
        highest = -1
        print(f'Looking between indices {prev_index+1} and {len(list_i)-(sequence_length-l-1)}')
        current_slice = list_i[prev_index+1:len(list_i)-(sequence_length-l-1)]
        print(f'This slice looks like: {current_slice}')
        joltage2[l] = max(current_slice)
        prev_index += current_slice.index(max(current_slice)) + 1
        print(f'Highest index: {prev_index}')
        print(f'Joltage: {joltage2}')
        print('\n')

    print(f'Joltage: {int(''.join(joltage2))}')
    total2 += int(''.join(joltage2))

print(total2)