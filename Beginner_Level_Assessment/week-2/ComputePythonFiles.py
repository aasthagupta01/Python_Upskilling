import os
"""a function to count number of python files present in a directory
returns count of files"""
def count_python_files(path:str)-> int:
    count = 0
    for file in os.listdir(path):
        # check for python files
        if file.endswith('.py'):
            count += 1

    return count

if __name__ == "__main__":
    path = "/Users/aastha.gupta/PycharmProjects/pythonUpskilling/assignment2"
    print(f'number of python files in this directory is {count_python_files(path)}')