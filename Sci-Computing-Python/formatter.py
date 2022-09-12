
# The arithmatic formater (for children) project of freeCodeCamp.org python course


def checkAllErrors(arithmaticList):
    '''
    Parameters
    ----------
    arithmaticList : TYPE
        DESCRIPTION.

    Returns
    -------
    allDigits : TYPE = List of (list of int)
        Containing all digits of the the arithmatic operations to be performed
    allOperators : TYPE = List of string
        List of all operation to be perforemed
    digitSpace : TYPE = List of ints
        List containing all 

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
        digitSpace.append(max([len(arithmetic[i]) for i in range(len(arithmetic))]) + 2)
        
        try:
            arithmetic = [int(arithmetic[i]) for i in range(len(arithmetic))]
        except :
            raise ValueError("Error: Numbers must only contain digits.")
    
    return allDigits, allOperators, digitSpace



def arithmatic_arranger(arithmaticList, getSolution):
    '''
    Parameters
    ----------
    arithmaticList : TYPE = List/tuple
        List containing all arithmatic operations requested by user for formatting
        all elements of the list are in string format.
    getSolution : TYPE = boolean
        A boolean variable that instructs the code to solve the arithmatic problems or not.

    Returns
    -------
    None.
    '''

    
    allDigits, allOperators, digitSpace = checkAllErrors(arithmaticList)
    
    print(allDigits)
    print(allOperators)
    print(digitSpace)
    
            
    return



def main():
    '''
    The main function that will be make call to other subfunctions
    '''
    arithmatic_arranger(["32 + 8", "1 - 801", "5234 - 49"], False)

    return



if __name__ == "__main__":
    main()
else:
    print("imported otherplace")
    #arithmatic_arranger(["32 + 8", "1 - 3801", "999129 + 9999", "523 - 49"], True)

