# get the ordinal numbers right
def ith(i):
    return(('th'*(10<(abs(i)%100)<14))+['st','nd','rd',*['th']*7][(abs(i)-1)%10])[0:2]


# get the input
def get_input(message, func, minimum, maximum):

    # get input until a valid input is given
    valid = False
    while(not valid):
        value = input(message)
        valid, value = check(func, value, minimum, maximum)

    return value


# check validity of the input
def check(func, value, minimum, maximum):

    # try if the input is of correct type
    try:
        value = func(value)
    # handle exception and give the expected type
    except:
        print("There is an error in the input.")
        print("The input should be a {}".format(func.__name__))
        print("Your input was {}".format(value))
        return False, 0

    # check if input whithin the correct interval
    valid = (minimum < value < maximum)
    # if not valid input explain the correct interval
    if not valid:
        print("There is an error in the input.")
        print("The input should be between {} and {}".format(minimum, maximum))
        print("Your input was {}".format(value))
    return valid, value