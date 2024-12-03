from utils.file_utils import read_file

def get_total_distance(locations_id):
    total_distance = 0
    left, right = zip(*(location.split() for location in locations_id))

    right = sorted(right)
    left = sorted(left)

    for l, r in zip(left, right):
        total_distance += abs(int(l) - int(r))

    return total_distance

def main():
    locations = read_file('./input/day1.txt')
    result = get_total_distance(locations)
    print (result)

if __name__ == "__main__":
    main()