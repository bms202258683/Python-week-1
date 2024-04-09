def create_and_write_to_file(filename):
    try:
        with open(filename, 'w') as file:  
            file.write("Welcome all!")
            file.write("We have created a new instance")
            file.write("Hope it works!")
        print(f"Successfully wrote to {filename}")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error: {e}")
    finally:
        print("File creation and writing operation completed.")

def read_and_display_file_contents(filename):
    try:
        with open(filename, 'r') as file:
            file_contents = file.read()
            print(f"Contents of {filename}:")
            print(file_contents)
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error: {e}")
    finally:
        print("File reading operation completed.")
def append_to_file(filename):
    try:
        with open(filename, 'a') as file:
            file.write("Daniel")
            file.write("Kariuki")
            file.write("Ngahu")
        print("Successfully appended to the file.")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error: {e}")
    finally:
        print("File appending operation completed.")

def main():
    filename = "my_file.txt"

    create_and_write_to_file(filename)

    read_and_display_file_contents(filename)

    append_to_file(filename)

    read_and_display_file_contents(filename)

if __name__ == "__main__":
    main()
