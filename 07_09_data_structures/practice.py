cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps():
    """
    return a comma separated string of jeep models (original order)
    """
    mystring = ', '.join(cars['Jeep'])
    return mystring


def get_first_model_each_manufacturer():
    """return a list of matching models (original ordering)"""
    first_model = [models[0] for models in cars.values()]
    return first_model


def get_all_matching_models(grep='trail'):
    """
    return a list of all models containing the case insensitive 'grep' string
    which defaults to 'trail' for this exercise, sort the resulting sequence
    alphabetically"""
    grep = grep.lower()
    models = sum(cars.values(), [])  # flatten list of lists
    matching_models = [model for model in models if grep in model.lower()]
    return sorted(matching_models)
#    matches = []
#    for models in cars.values():
#        for model in models:
#            if grep.lower() in model.lower():
#                matches.append(model)
#    matches.sort()
#    return matches


def sort_car_models():
    """
    sort the car models(values) and return the resulting cars dict
    """
    return {manufacturer: sorted(models)
            for manufacturer, models in cars.items()}
#    for key, value in cars.items():
#        value.sort()
#        cars[key] = value
#    return cars


# Here is the test results:
a = get_all_jeeps()
print(a)

b = get_first_model_each_manufacturer()
print(b)

c = get_all_matching_models(grep='trail')
print(c)

d = sort_car_models()
print(d)

models = sum(cars.values(), [])
print(models)
