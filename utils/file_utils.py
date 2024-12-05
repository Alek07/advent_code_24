def read_file(file_path, mode='lines'):
    """
    Read a file with different modes of operation
    
    Args:
        file_path (str): Path to the file
        mode (str): Reading mode - 'lines' (default), 'string', or 'raw'
            - 'lines': Returns list of stripped lines
            - 'string': Returns entire file as single string
            - 'raw': Returns list of unmodified lines with whitespace
    
    Returns:
        Union[List[str], str]: File contents based on mode
    """
    try:
        with open(file_path, "r") as file:
            if mode == 'string':
                return file.read()
            elif mode == 'raw':
                return file.readlines()
            else:  # default 'lines' mode
                return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return [] if mode != 'string' else ''