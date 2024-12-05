from utils.file_utils import read_file
import re

def is_match(text):
    pattern = r'(MAS|SAM)'
    return bool(re.match(pattern, text))

def search_for_x_mas(matrix):
    count = 0
    mtx = [list(x) for x in matrix]

    for row in range(len(mtx)):
        for col in range(len(mtx)):
            is_a = mtx[row][col] == 'A'
            if (is_a):
                a = mtx[row][col]

                up_l = ''
                up_r = ''
                down_l = ''
                down_r = ''

                # Diagonal checks
                if (row - 1 >= 0 and col + 1 < len(mtx)):
                    up_r = mtx[row - 1][col + 1]
                if (row + 1 < len(mtx) and col + 1 < len(mtx)):
                    down_r = mtx[row + 1][col + 1]
                if (row + 1 < len(mtx) and col - 1 >= 0):
                    down_l = mtx[row + 1][col - 1]
                if (row - 1 >= 0 and col - 1 >= 0):
                    up_l = mtx[row - 1][col - 1]

                first_mas = is_match(''.join([up_l, a, down_r]))
                second_mas = is_match(''.join([up_r, a, down_l]))

                if first_mas and second_mas:
                    count += 1
            
            print
    return count

def search_for_xmas(matrix):
    count = 0
    mtx = [list(x) for x in matrix]

    for row in range(len(mtx)):
        for col in range(len(mtx)):
            is_x = mtx[row][col] == 'X'
            if (is_x):
                x = mtx[row][col]

                up = ''
                down = ''
                left = ''
                right = ''

                up_l = ''
                up_r = ''
                down_l = ''
                down_r = ''

                 # Vertical and Horizontal checks
                if (row - 3 >= 0):
                    up = ''.join([x, mtx[row - 1][col], mtx[row - 2][col], mtx[row - 3][col]])
                if (row + 3 < len(mtx)):
                    down = ''.join([x, mtx[row + 1][col], mtx[row + 2][col], mtx[row + 3][col]]) 
                if (col + 3 < len(mtx)):
                    right = ''.join([x, mtx[row][col + 1], mtx[row][col + 2], mtx[row][col + 3]])
                if (col - 3 >= 0):
                    left = ''.join([x, mtx[row][col - 1], mtx[row][col - 2], mtx[row][col - 3]])

                # Diagonal checks
                if (row - 3 >= 0 and col + 3 < len(mtx)):
                    up_r = ''.join([x, mtx[row - 1][col + 1], mtx[row - 2][col + 2], mtx[row - 3][col + 3]])
                if (row + 3 < len(mtx) and col + 3 < len(mtx)):
                    down_r = ''.join([x, mtx[row + 1][col + 1], mtx[row + 2][col + 2], mtx[row + 3][col + 3]])
                if (row + 3 < len(mtx) and col - 3 >= 0):
                    down_l = ''.join([x, mtx[row + 1][col - 1], mtx[row + 2][col - 2], mtx[row + 3][col - 3]])
                if (row - 3 >= 0 and col - 3 >= 0):
                    up_l = ''.join([x, mtx[row - 1][col - 1], mtx[row - 2][col - 2], mtx[row - 3][col - 3]])

                res = list(filter(lambda x: x != '', [ up, up_r, right, down_r, down, down_l, left, up_l ]))
                count += res.count("XMAS")

    return count

def main():
    matrix = read_file('./input/day4.txt', mode='lines')
    result = search_for_x_mas(matrix)
    print (result)

if __name__ == "__main__":
    main()