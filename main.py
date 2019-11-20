from json import dump
from messages import *
from intervals import *
from utils import *

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
