import os

def list_directories_files(path, all_content=False):
    print("Listing directories:")
    directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    print(directories)
    
    print("\nListing files:")
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    print(files)
    
    if all_content:
        print("\nListing all directories and files recursively:")
        for root, dirs, files in os.walk(path):
            for directory in dirs:
                print(os.path.join(root, directory))
            for file in files:
                print(os.path.join(root, file))


path = "C:/Users/PC/Desktop"  
list_directories_files(path)

print("\n--------------------------------------------\n")


list_directories_files(path, all_content=True)















import os

def check_access(path):
    print(f"Checking access for path: {path}")
    
    
    if os.path.exists(path):
        print("Path exists.")
    else:
        print("Path does not exist.")
        return
    
    
    if os.access(path, os.R_OK):
        print("Path is readable.")
    else:
        print("Path is not readable.")
    
    
    if os.access(path, os.W_OK):
        print("Path is writable.")
    else:
        print("Path is not writable.")
    
    
    if os.access(path, os.X_OK):
        print("Path is executable.")
    else:
        print("Path is not executable.")


path = "example.txt"  
check_access(path)















import os

def analyze_path(path):
    if os.path.exists(path):
        print("Path exists.")
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        print("Filename:", filename)
        print("Directory:", directory)
    else:
        print("Path does not exist.")

path = "C:/Users/PC/Desktop/example.txt"  

analyze_path(path)













def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            line_count = sum(1 for line in file)
        return line_count
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return -1


filename = "example.txt"  
line_count = count_lines(filename)
if line_count != -1:
    print(f"The number of lines in '{filename}' is: {line_count}")












def write_list_to_file(filename, input_list):
    try:
        with open(filename, 'w') as file:
            for item in input_list:
                file.write(str(item) + '\n')
        print(f"List has been written to '{filename}' successfully.")
    except Exception as e:
        print(f"Error occurred while writing to '{filename}': {e}")


filename = "output.txt"  
my_list = ['apple', 'banana', 'orange', 'grape']
write_list_to_file(filename, my_list)














import string

def generate_files():
    for letter in string.ascii_uppercase:
        filename = letter + ".txt"
        with open(filename, 'w') as file:
            pass  


generate_files()



















def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                destination.write(source.read())
        print(f"Contents of '{source_file}' copied to '{destination_file}' successfully.")
    except Exception as e:
        print(f"Error occurred while copying contents: {e}")


source_file = "source.txt"  
destination_file = "destination.txt"  
copy_file(source_file, destination_file)

















import os

def delete_file(path):
    
    if os.path.exists(path):
        print(f"Path '{path}' exists.")
        
        if os.access(path, os.F_OK | os.R_OK | os.W_OK | os.X_OK):
            print("Access check passed.")
            try:
                # Delete the file
                os.remove(path)
                print(f"File '{path}' has been deleted successfully.")
            except Exception as e:
                print(f"Error occurred while deleting file: {e}")
        else:
            print(f"Access denied to file '{path}'.")
    else:
        print(f"Error: File '{path}' does not exist.")


file_path = "example.txt"  
delete_file(file_path)



