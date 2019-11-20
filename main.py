from json import dump
from sys import maxsize


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


###
###  Messages
###
no_trucks = "Oh too bad you don't own any trucks.\n" \
    "We are a company for truck owners. So we can't help you.\n" \
    "It was nice chatting with you {}\n" \
    "Goodbye"
name = "Hello, what's your name?\n"
company = "Hello {}, what's the name of your company?\n"
great = "Great! We're happy to work for {}"
any_trucks = "Do you own any trucks?\n"
number_brands = "How many different brands do you have in your fleet?\n"
thanks = "Thank you {}. We need to go through each brand and get the different models, their engine size," \
          " their number of axles, their weight and their maximum load. This will take a bit. " \
            "But I guide you through it."
name_brand = "What is the name of the {}{} brand?\n"
number_models = "How many different models do you have of {}?\n"
name_model = "What is the name of the {}{} model?\n"
number_model = "How many trucks of the model {} of brand {} do you have?\n"
engine_size = "What is the engine size of model {} of brand {} in litres?\n"
number_axels = "How many axles does model {} of brand {} have?\n"
mass = "What's the weight of model {} of brand {}?\n"
maximum_load = "What's the max load of model {} of brand {}?\n"


###
### type, min and max of data
###
number_tmm = [int, 0, maxsize]
number_brands_tmm = [int, 0, maxsize]
nmodels_tmm = [int, 0, maxsize]
engine_tmm = [float, 0.0, 10.0]
axels_tmm = [int, 0, 6]
mass_tmm = [float, 1000.0, float('inf')]
maximum_load_tmm = [float, 1000.0, float('inf')]


def bot():
    """This bot collects data of the truck fleet and stores it in a json file called companyname_personname.json
    data collected:
    customername        name of customer
    customercompany     name of company

    For each brand and model of this brand
    brand               name of brand
    model               name of model
    number              number of trucks in the fleet of this brand and model
    engine              the engine size in litres
    axels               number of axels
    weight              the weight of the truck
    max_load            the maximum load of the truck
    """

    # get customer name and company name
    customername = input(name)
    customercompany = input(company.format(customername))

    # check if they own trucks
    print(great.format(customercompany))
    own_trucks = input(any_trucks)
    if own_trucks.lower() != 'yes':
        print(no_trucks.format(customername))
        return

    # get the number of different brands in the fleet
    number_of_brands = get_input(number_brands, *number_brands_tmm)
    # thank for input and explain that we will loop over brands
    print(thanks.format(customername))

    # initialize the dictionary for storage
    trucks = {}

    # loop over brands
    for i in range(number_of_brands):
        # get the brand name and initialize new dictionary
        brand = input(name_brand.format(i+1, ith(i+1)))
        trucks[brand] = {}

        # get the number of models
        nmodels = get_input(number_models.format(brand), *nmodels_tmm)
        # loop over the models
        for j in range(nmodels):
            # get model name
            model = input(name_model.format(j+1, ith(j+1)))
            model_brand = [model, brand]
            # get number of trucks for given model and brand
            number = get_input(number_model.format(*model_brand), *number_tmm)
            # get engine size
            engine = get_input(engine_size.format(*model_brand), *engine_tmm)
            # get number of axels
            axles = get_input(number_axels.format(*model_brand), *axels_tmm)
            # get weight of truck
            weight = get_input(mass.format(*model_brand), *mass_tmm)
            # get maximum load of truck
            max_load = get_input(maximum_load.format(*model_brand), *maximum_load_tmm)

            # save all the data in a dictionary
            trucks[brand][model] = {}
            trucks[brand][model]['number'] = number
            trucks[brand][model]['engine'] = engine
            trucks[brand][model]['axles'] = axles
            trucks[brand][model]['weight'] = weight
            trucks[brand][model]['max_load'] = max_load

    # save the dictionary to file
    f = open('{}_{}.json'.format(customercompany, customername), 'w')
    dump(trucks, f, indent=4)

if __name__ == '__main__':
    bot()
