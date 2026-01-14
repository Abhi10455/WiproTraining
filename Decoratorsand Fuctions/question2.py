def write_numbers_to_file(filename):
    try:
        file = open(filename, "w")
        for number in range(1, 101):
            file.write(str(number) + "\n")
        file.close()
        print("File written successfully.")

    except FileNotFoundError:
        print("Error: File not found.")

    except PermissionError:
        print("Error: Permission denied.")

    except Exception as error:
        print("Unexpected error:", error)


def read_file_safely(filename):
    try:
        file = open(filename, "r")
        print("\nFile Content:\n")

        for line in file:
            print(line.strip())

        file.close()

    except FileNotFoundError:
        print("Error: File not found.")

    except PermissionError:
        print("Error: Permission denied.")

    except Exception as error:
        print("Unexpected error:", error)

file_name = "numbers.txt"
write_numbers_to_file(file_name)
read_file_safely(file_name)
