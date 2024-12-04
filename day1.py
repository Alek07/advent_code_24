from utils.file_utils import read_file

def calculated_total_similarity_score(left, right):
    similarity_score = 0

    for value in left:
        similarity_score += (int(value) * right.count(value))

    return similarity_score


def get_total_distance(locations_id):
    total_distance = 0
    left, right = zip(*(location.split() for location in locations_id))

    right = sorted(right)
    left = sorted(left)

    for l, r in zip(left, right):
        total_distance += abs(int(l) - int(r))

    total_similarity_score = calculated_total_similarity_score(left, right)

    return [total_distance, total_similarity_score]

def main():
    locations = read_file('./input/day1.txt')
    result = get_total_distance(locations)
    print (result)

if __name__ == "__main__":
    main()