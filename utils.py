from strings import brands, brands_dict

# get the ordinal numbers right
def ith(i):
    return(('th'*(10<(abs(i)%100)<14))+['st','nd','rd',*['th']*7][(abs(i)-1)%10])[0:2]


# get and check the brand input
def get_brand_input(message, brands_list):

    # get input until valid input is given
    valid = False
    log = []
    while(not valid):
        value = input(message)
        log.append(value)
        if value == 'STOP':
            return -1, log

        valid = value.lower() in brands
        # check if input is actually a brand
        if not valid:
            print("I'm sorry but I don't recognize the brand {}".format(value))
        # check if this brand has already been taken care of
        elif value.lower() in brands_list:
            print("It looks like we've already taken care of {}".format(brands_dict[value.lower()]))
            print("In case you made a mistake earlier and there aren't more brands in your fleet than {}, please type STOP".format(brands_list))
            valid = False
        # transform the input in proper upper and lower case letters
        else:
                value = brands_dict[value.lower()]

    return value, log


# get and check the model input
def get_model_input(message, models_list):

    # get input until valid input is given
    valid = False
    log = []
    while(not valid):
        value = input(message)
        log.append(value)
        valid = True
        if value == 'STOP':
            return -1, log

        # check if this brand has already been taken care of
        if value.lower() in models_list:
            print("It looks like we've already taken care of {}".format(value))
            print("In case you made a mistake earlier and there aren't more models in your fleet than {}, please type STOP".format(models_list))
            valid = False

    return value, log

# get the input
def get_input(message, func, minimum, maximum):

    # get input until a valid input is given
    valid = False
    log = []
    while(not valid):
        value = input(message)
        log.append(value)
        valid, value = check(func, value, minimum, maximum)

    return value, log


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