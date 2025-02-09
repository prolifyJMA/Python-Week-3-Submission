#%%
#

'''

Welcome to week 3!

Please review and run the following code to see how conditionals and loops work!

You can play around with the value(s) to have hte program show different branches!

'''

#%%
# Looping Function

def loop_function(x):

    # Here is an example of a "for" loop
    for i in range(x):

        # Here is an example of a conditional statement
        # If hte remainder of i divided by 2 is 0, then it is an even number
        if i % 2 == 0:
            print(i, "is even!")
        else:
            print(i, "is an odd number!")

    print("Done!")


number_of_loops = 10

loop_function(number_of_loops)