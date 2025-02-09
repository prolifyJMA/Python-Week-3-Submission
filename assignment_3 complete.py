# Objective: Write a program that takes a list of numbers and prints out the sum, average, and largest number in the list.

while True:
    try:
        # Take input
        inputNum = input("Please enter numbers separated by spaces: ")
        array = inputNum.split()
        array = [int(x) for x in array]
        
        # Math input and output
        inputMath = input("Would you like to sum, average, or find the largest number? or all? ").lower()

        if inputMath == "sum":
            print("Sum:", sum(array))
        elif inputMath == "average":
            print("Average:", sum(array) / len(array))
        elif inputMath == "largest" or inputMath == "largest number":
            print("Largest:", max(array))
        elif inputMath == "all":
            print("Sum:", sum(array))
            print("Average:", sum(array) / len(array))
            print("Largest:", max(array))
        else:
            print("Invalid input. Please choose 'sum', 'average', 'largest', 'largest number', or 'all'.")
            continue

        # Cleaned up code by only asking this once :)
        print("Would you like to do another operation? (yes/no)")
        anotherOperation = input().lower()
        if anotherOperation == "no":
            break

    except ValueError:
        print("Invalid input, please try again! :)")
