### Setup: ###
### Read input: ###
with open('input.txt') as f:
    input = f.read()

input_by_line = input.strip().split('\n')

print(input)
test_input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,\
1698522-1698528,446443-446449,38593856-38593862,565653-565659,\
824824821-824824827,2121212118-2121212124"

# input = test_input
ranges = input.split(',')

### Part 1: ###
count=0
for r in ranges:
    first, last = r.split('-')

    for i in range(int(first), int(last)+1):
        chars = len(str(i))
        if chars % 2 != 0:
            continue
        
        half_chars = int(chars/2)
        if str(i)[:half_chars] == str(i)[half_chars:]:
            count += i
print(count)

### Part 2: ###
count2=0
for r in ranges:
    first, last = r.split('-')

    for i in range(int(first), int(last)+1):
        chars = len(str(i))
        if chars == 1:
            continue
        
        for div in range(1, chars+1):
            # print(div)
            if chars % div == 0:
                parts = [str(i)[j:j+div] for j in range(0, chars, div)]
                if len(parts) == 1: continue
                if len(set(parts)) == 1:
                    print(f'Invalid: {i}')
                    print(parts)
                    count2 += i
                    break


print(count2)