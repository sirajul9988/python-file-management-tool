import os
import shutil

def list_files(path="."):
    print("Files and directories:")
    for item in os.listdir(path):
        print("-", item)

def create_directory(name):
    if not os.path.exists(name):
        os.mkdir(name)
        print(f"Directory '{name}' created")
    else:
        print("Directory already exists")

def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f"File '{filename}' deleted")
    else:
        print("File not found")

def main():
    print("Python File Management Tool")
    print("1. List files")
    print("2. Create directory")
    print("3. Delete file")

    choice = input("Enter choice: ")

    if choice == "1":
        list_files()
    elif choice == "2":
        name = input("Directory name: ")
        create_directory(name)
    elif choice == "3":
        filename = input("File name: ")
        delete_file(filename)
    else:
        print("Invalid option")

if __name__ == "__main__":
    main()
