from utils.file_utils import read_file
import re

def mul(corrupted_memory):
    total = 0
    enable = True
    instructions = re.finditer(r'(?:do\(\)|don\'t\(\)|mul\((\d{1,3}),(\d{1,3})\))', corrupted_memory)

    for match in instructions:
        process = match.group(0)

        if process == 'do()':
            enable = True
        elif process == "don't()":
            enable = False
        elif enable:
            num1 = int(match.group(1))
            num2 = int(match.group(2))
            total += num1 * num2
            
            
    return total

def main():
    memory_content = read_file('./input/day3.txt', mode='string')
    result = mul(memory_content)
    print (result)

if __name__ == "__main__":
    main()