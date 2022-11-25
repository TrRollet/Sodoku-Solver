"""
Sodoku solver using python 3.9.13
Author: TrRollet
"""

import sys
import os

def print_soduku(soduku, file=None):
    """Print the soduku in the terminal or in a file"""
    if file == None: # Print into the terminal
        print("╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗")
        for i in range(9):
            print("║", end="")
            for j in range(9):
                if soduku[i][j] == 0:
                    print("   ", end="")
                else:
                    print(" " + str(soduku[i][j]) + " ", end="")
                if j == 2 or j == 5:
                    print("║", end="")
                elif j != 8:
                    print("│", end="")
            print("║")
            if i == 2 or i == 5:
                print("╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣")
            elif i != 8:
                print("╟───┼───┼───╫───┼───┼───╫───┼───┼───╢")
        print("╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝")
    else: # Print into a file
        file.write("╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗\n")
        for i in range(9):
            file.write("║")
            for j in range(9):
                if soduku[i][j] == 0:
                    file.write("   ")
                else:
                    file.write(" " + str(soduku[i][j]) + " ")
                if j == 2 or j == 5:
                    file.write("║")
                elif j != 8:
                    file.write("│")
            file.write("║\n")
            if i == 2 or i == 5:
                file.write("╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣\n")
            elif i != 8:
                file.write("╟───┼───┼───╫───┼───┼───╫───┼───┼───╢\n")
        file.write("╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝\n")

def check_case(soduku, i, j):
    """Return True if the case is valid else False"""
    for k in range(9):
        if k != j and soduku[i][k] == soduku[i][j]:
            return False
    for k in range(9):
        if k != i and soduku[k][j] == soduku[i][j]:
            return False
    for k in range(3):
        for l in range(3):
            if (k + 3 * (i // 3)) != i and (l + 3 * (j // 3)) != j and soduku[k + 3 * (i // 3)][l + 3 * (j // 3)] == soduku[i][j]:
                return False
    return True

def check_soduku(soduku):
    """Return True if the soduku is correct else return False"""
    for i in range(9):
        for j in range(9):
            if soduku[i][j] != 0:
                if not check_case(soduku, i, j):
                    return False
    return True

def solve_soduku(soduku):
    """Return True if the soduku is solved and fill the soduku with the solution else 
    return False if the soduku is not solvable"""
    for i in range(9):
        for j in range(9):
            if soduku[i][j] == 0:
                for k in range(1, 10):
                    soduku[i][j] = k
                    if check_case(soduku, i, j):
                        if solve_soduku(soduku):
                            return True
                soduku[i][j] = 0
                return False
    return True

def main():
    print_soduku_into_file = False # If the soduku is solved, print it into the file
    sodoku_file = "" # The file of the sodoku (if -f is used)
    print_file_name = "" # The file where the sodoku will be printed (if -p is used)
    if len(sys.argv) > 1:
        # Check if the argument -f is used
        if "-f" in sys.argv:
            index = sys.argv.index("-f")
            if index + 1 < len(sys.argv):
                sodoku_file = sys.argv[index + 1]
                if not os.path.exists(sodoku_file):
                    print("The sodoku file " + sodoku_file + " doesn't exist, please retry")
                    return
            else:
                print("Error: -f need a file name")
                return
        # Check if the argument -p is used
        if "-p" in sys.argv:
            index = sys.argv.index("-p")
            if index + 1 < len(sys.argv):
                print_file_name = sys.argv[index + 1]
                if not os.path.exists(print_file_name):
                    open(print_file_name, "w").close()
            else:
                print("Error: -p need a file name")
                return

    if sodoku_file != "":
        if not os.path.isfile(sodoku_file):
            print("Error: the sodoku file doesn't exist")
            return
        
        # Read the sodoku file and fill the sodoku
        try:
            with open(sodoku_file, "r") as file:
                soduku = [[0 for j in range(9)] for i in range(9)]
                for i in range(9):
                    line = file.readline()
                    if (i < 7 and len(line) != 10): # 9 + 1 (for the end of line)
                        print("Error: the sodoku file is not valid")
                        return
                    for j in range(9):
                        if line[j] != ".":
                            soduku[i][j] = int(line[j])

        except:
            print("Error: the sodoku file is not valid")
            return
                    
        # Print the soduku
        print("Initial sodoku:")
        print_soduku(soduku)
        print()
        
    else:
        print("Enter the case you want to change and the new value (Ex: 12 9 change the case 12 to 9) or -1 -1 to stop\n\
            Check on the github page to see the case number")
        soduku = [[0 for i in range(9)] for j in range(9)]
        while True:
            try:
                case, value = input().split()
            except ValueError: # Check if the input is valid
                print("Error: usage: <case> <value>")
                continue
            if case == "-1":
                break
            try:
                case = int(case)
                value = int(value)
            except ValueError:
                print("Error: usage: <case> <value>")
                continue
            if case < 1 or case > 81 or value < 1 or value > 9:
                print("Error: usage: <case> <value>")
                continue
            soduku[(case - 1) // 9][(case - 1) % 9] = value
            print_soduku(soduku)
            if not check_soduku(soduku):
                print("Error: the soduku is incorrect, please retry")
                # remove the last value
                soduku[(case - 1) // 9][(case - 1) % 9] = 0
                print_soduku(soduku)
                continue
        
    # Solve the soduku and print the result into the file (if -p is used) or print it into the terminal
    if solve_soduku(soduku):
        print("Solved:")
        print_soduku(soduku)
        if print_file_name != "":
            with open(print_file_name, "w") as file:
                if print_soduku_into_file:
                    print("Solved:", file=file)
    else:
        print("Error: no solution found, please retry")

if __name__ == "__main__":
    main()
