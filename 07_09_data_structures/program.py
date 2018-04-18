from data import us_state_abbrev, states_list
from collections import OrderedDict


def main():
    ordered_us_state_abbrev = convert_dict_to_orderedDict(us_state_abbrev)
    print_tenth_item(ordered_us_state_abbrev, states_list)
    print_fortyfifth_key(ordered_us_state_abbrev)
    print_fortyfifth_value(ordered_us_state_abbrev)

    print(ordered_us_state_abbrev)
    ordered_us_state_abbrev = replace_key(ordered_us_state_abbrev)
    print(ordered_us_state_abbrev)


def convert_dict_to_orderedDict(original_dict):
    list_of_tuple = [(key, value) for key, value in original_dict.items()]
    ordered_dict = OrderedDict(list_of_tuple)
    return ordered_dict


def print_tenth_item(ordered_dict, a_list):
    tenth_item_dict= list(ordered_dict.items())[9]
    tenth_item_list = a_list[9]
    print('The tenth item of the dictionary is {}'.format(tenth_item_dict))
    print('The tenth item of the list is {}'.format(tenth_item_list))


def print_fortyfifth_key(ordered_dict):
    fortyfifth_key_dict = list(ordered_dict.keys())[44]
    print(fortyfifth_key_dict)


def print_fortyfifth_value(ordered_dict):
    fortyfifth_value_dict = list(ordered_dict.values())[26]
    print(fortyfifth_value_dict)


def replace_key(ordered_dict):
    initial_key = list(ordered_dict.keys())[0]
    final_key = list(ordered_dict.keys())[1]
    ordered_dict[final_key] = ordered_dict.pop(initial_key)
    return ordered_dict




if __name__ == '__main__':
    main()
