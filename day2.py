from utils.file_utils import read_file

def is_safe(levels_list):
    if len(levels_list) <= 1:
        return True
    
    trend = None

    for i in range(len(levels_list) - 1):
        diff = levels_list[i + 1] - levels_list[i]
        
        if diff == 0 or abs(diff) > 3:
            return False
        
        if trend is None:
            trend = diff > 0
            continue
        
        if (diff > 0) != trend:
            return False
            
    return True

def count_safe_reports(reports):
    safe_reports = 0

    for report in reports:
        levels_list = list(map(int, report.split()))
        
        if is_safe(levels_list):
            safe_reports += 1
            continue
            
        for i in range(len(levels_list)):
            modified_levels = levels_list[:i] + levels_list[i+1:]
            if is_safe(modified_levels):
                safe_reports += 1
                break

    return safe_reports

def main():
    reports = read_file('./input/day2.txt')
    result = count_safe_reports(reports)
    print (result)

if __name__ == "__main__":
    main()