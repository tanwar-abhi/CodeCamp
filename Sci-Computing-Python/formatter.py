
# The arithmatic formater (for children) project of freeCodeCamp.org python course


def checkAllExceptions(arithmaticList):
    '''
    Parameters
    ----------
    arithmaticList : TYPE = List of strings
        List of problems to be formatted, each element of list is a string

    Returns
    -------
    allDigits : TYPE = List of (list of int)
        Containing all digits of the the arithmatic operations to be performed
    allOperators : TYPE = List of string
        List of all operation to be perforemed
    digitSpace : TYPE = List of ints
        List containing spaces for uniform formatting
    '''
    
    allOperators = []
    allDigits = []
    digitSpace = []
    ct = 0

    for i in arithmaticList:
        ct += 1

        if ct > 5:
            raise Exception("Error: Too many problems.")

        arithmetic = i.split()
        operator = arithmetic[1]
        if operator != "-" and operator != "+":
            raise Exception("Error: Operator must be '+' or '-'.")
        
        allOperators.append(operator)
        arithmetic.remove(operator)
        if len(arithmetic[0]) > 4 or len(arithmetic[1]) > 4:
            raise Exception("Error: Numbers cannot be more than four digits.")        

        allDigits.append(arithmetic)
        
        maxDig = max([len(arithmetic[i]) for i in range(len(arithmetic))])
        digitSpace.append([maxDig+2-len(arithmetic[0]), maxDig+1-len(arithmetic[1])])
            
        
        try:
            arithmetic = [int(arithmetic[i]) for i in range(len(arithmetic))]
        except:
            raise ValueError("Error: Numbers must only contain digits.")
        
    
    return allDigits, allOperators, digitSpace



# Function to provide aesthetic formating for young students
def arithmatic_arranger(arithmaticList, showSolution):
    '''
    Parameters
    ----------
    arithmaticList : TYPE = List/tuple
        List containing all arithmatic operations requested by user for formatting
        all elements of the list are in string format.
    showSolution : TYPE = boolean
        A boolean variable that instructs the code to solve the arithmatic problems or not.

    Returns
    -------
    None.
    '''

    
    allDigits, allOperators, digitSpace = checkAllExceptions(arithmaticList)

    solution = []
    ct = 0
    for nums in allDigits:
        if allOperators[ct] == "+":
            solution.append(int(nums[0]) + int(nums[1]))
        else:
            solution.append(int(nums[0]) - int(nums[1]))
        ct += 1

    for i in range(len(allDigits)):
        print(" "*digitSpace[i][0] + allDigits[i][0], end=" "*4)
    
    print("")
    for i in range(len(allDigits)):
        print(allOperators[i]+" "*digitSpace[i][1] + allDigits[i][1], end=" "*4)

    print("")
    totalSpace = []
    for i in range(len(allDigits)):
        maxDigLen = max([len(allDigits[i][j]) for j in range(len(allDigits[i]))])
        print("-"*(maxDigLen+2), end=" "*4)
        totalSpace.append(maxDigLen+2)
    
    print("")    
    if showSolution == True:
        for i in range(len(solution)):
            print(" "*(totalSpace[i]-len(str(solution[i]))) + str(solution[i]), end =" "*4)
        
    
    
    #print(allDigits)
    #print(allOperators)
    #print(digitSpace)

    return



def main():
    '''
    The main function that will be make call to other subfunctions
    '''
    arithmatic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)

    return



if __name__ == "__main__":
    main()
else:
    print("imported otherplace")
    #arithmatic_arranger(["32 + 8", "1 - 3801", "999129 + 9999", "523 - 49"], True)

