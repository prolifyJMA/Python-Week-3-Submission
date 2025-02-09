
# Objective: Write a program that takes a list of numbers and prints out the sum, average, and largest number in the list.
#%%
while True:
    try:
        # Take input
        inputNum = input("Please enter numbers separated by spaces: ")
        array = inputNum.split()
        array = [int(x) for x in array]
        
        # Math input and output (is there a better way to do this without all the else ifs?)
        inputMath = input("Would you like to sum, average, or find the largest number? or all? ").lower()

        if inputMath == "sum":
            print("Sum:", sum(array))

            print("would you like to do another operation? (yes/no)")
            another_operation = input().lower()
            if another_operation == "no":
                break
        elif inputMath == "average":
            print("Average:", sum(array) / len(array))
            
            print("would you like to do another operation? (yes/no)")
            another_operation = input().lower()
            if another_operation == "no":
                break

        elif inputMath == "largest" or inputMath == "largest number":
            print("Largest:", max(array))
            
            print("would you like to do another operation? (yes/no)")
            another_operation = input().lower()
            if another_operation == "no":
                break

        elif inputMath == "all":
            print("Sum:", sum(array))
            print("Average:", sum(array) / len(array))
            print("Largest:", max(array))
            
            print("would you like to do another operation? (yes/no)")
            another_operation = input().lower()
            if another_operation == "no":
                break

        else:
            print("Invalid input. Please choose 'sum', 'average', 'largest', 'largest number', or 'all'.")
    except ValueError:
        print("Invalid input, please try again! :)")
# %%
