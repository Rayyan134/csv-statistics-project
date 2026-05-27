# Reads numbers from CSV, calculates mean/max/min,

# writes results into a summary CSV file


# Function 1: Read CSV manually

def read_csv_numbers(file_path: str) -> list:
    """
    Reads a CSV file containing one column of numbers.

    Args:
        file_path (str): path to CSV file

    Returns:
        list: list of floats
    """

    numbers = []

    file = open(file_path, "r")
    lines = file.readlines()
    file.close()

    for line in lines:
        value = float(line.strip())
        numbers.append(value)

    return numbers

# Function 2: Calculate stats

def calculate_stats(numbers: list) -> dict:
    """
    Calculates mean, max, and min from a list of numbers.

    Args:
        numbers (list): list of floats

    Returns:
        dict: dictionary with mean, mean, min
    """

    total = 0

    for num in numbers:
        total = total + num

    mean = total /  len(numbers)

    minimum = maximum = numbers[0]

    for num in numbers:
        if num > maximum:
            maximum = num
        
        if num < minimum:
            minimum = num

    return {
        "mean": mean,
        "max": maximum,
        "min": minimum
    }

# Function 3: Write CSV output

def write_summary(file_path: str, stats: dict) -> None:
    """
    Writes summary statistics into a CSV file.

    Args:
        file_path (str): output file path
        stats (dict): dictionary with mean, max, min
    """

    file = open(file_path, "w")

    file.write("metric, value\n")

    file.write(f"mean, {stats['mean']}\n")

    file.write(f"max, {stats['max']}\n")

    file.write(f"min, {stats['min']}\n")

    file.close()

# MAIN FUNCTION

def main() -> None:
    """
    Main program flow:
    1. Read numbers from CSV
    2. Calculate statistics
    3. Write summary CSV
    """

    input_file = "../data/numbers.csv" # .. goes back one folder

    output_file = "../output/summary.csv"

    numbers = read_csv_numbers(input_file)

    stats = calculate_stats(numbers)

    write_summary(output_file, stats)

    print("Done! summary.csv created successfully!")



# Run program
main()