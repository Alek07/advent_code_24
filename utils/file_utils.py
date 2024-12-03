def read_file(file_path):
    try:
        with open(file_path, "r") as file:
            cleaned_lines = [line.strip() for line in file.readlines()]
        return cleaned_lines
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
