def display_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Content of the file '{filename}':\n{content}")
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
filename = "2024-05-31_16-14-19.txt"
display_file(filename)