import os
import sys

def extract_logs_by_date(file_path, target_date, output_dir):
    os.makedirs(output_dir, exist_ok=True) # Checking to see if the output directory exists

    # Create the output file path
    output_file = os.path.join(output_dir, f"output_{target_date}.txt")

    try:
        with open(file_path, 'r') as log_file, open(output_file, 'w') as output:
            for line in log_file:
                if line.startswith(target_date): # Check if the line starts with the target date
                    output.write(line)

        print(f"Logs for {target_date} have been written to {output_file}")
        return output_file

    # ERROR HANDLING
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied for file: {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

def main():
    # Ensure correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: python extract_logs.py <YYYY-MM-DD>")
        sys.exit(1)

    # Getting the target date from commandline arguments
    target_date = sys.argv[1]

    # Validate the format of the date(YYYY-MM-DD)
    if len(target_date) != 10 or target_date[4] != '-' or target_date[7] != '-':
        print("Error: Invalid date format. Use YYYY-MM-DD.")
        sys.exit(1)

    # File path to the large log file
    log_file_path = "test_logs.log"  # Update if the file has a different name

    # Directory to save the output logs
    output_directory = "output"

    # Extract logs for the specified date
    extract_logs_by_date(log_file_path, target_date, output_directory)

if __name__ == "__main__":
    main()
