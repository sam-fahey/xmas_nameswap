import random

def unique_name(name_list, partner_of=''):

    list_list = [item if isinstance(item, list) else [item] for item in name_list]
    name_list_flat = [item for sublist in list_list for item in sublist]

    if partner_of == '':
        is_partner = False
    else:
        is_partner = True


    while True:

        if is_partner: 
            input_name = str(input("Enter the name of %s's partner.\n>>> " % partner_of))
        else: 
            input_name = str(input("\nEnter a name.\n>>> "))

        if input_name in name_list_flat:
            print("Sorry, %s is already in the list. Please enter unique names." % input_name)
            continue
        else: 
            break

    return input_name

def exchange_names(name_list):

    failures = 0
    while True:

        try:
            giving_dict = {}
            list_list = [item if isinstance(item, list) else [item] for item in name_list]
            names_to_give = [item for sublist in list_list for item in sublist]
            for name in name_list:
            
                if isinstance(name, list):
                    
                    partner1 = name[0]
                    partner2 = name[1]

                    print(partner1, partner2, names_to_give)
                    names_to_give1 = names_to_give.copy()
                    try: names_to_give1.remove(partner1)
                    except ValueError: pass
                    try: names_to_give1.remove(partner2)
                    except ValueError: pass
                    give_to_1 = random.choice(names_to_give1)
                    names_to_give.remove(give_to_1)
                    giving_dict[partner1] = give_to_1

                    names_to_give2 = names_to_give.copy()
                    try: names_to_give2.remove(partner2)
                    except ValueError: pass
                    try: names_to_give2.remove(partner1)
                    except ValueError: pass
                    give_to_2 = random.choice(names_to_give2)
                    names_to_give.remove(give_to_2)
                    giving_dict[partner2] = give_to_2

                else:

                    names_to_give_ = names_to_give.copy()
                    try: names_to_give_.remove(name)
                    except ValueError: pass
                    give_to = random.choice(names_to_give_)
                    names_to_give.remove(give_to)
                    giving_dict[name] = give_to
                
            break

        except IndexError:
            failures += 1
            if failures > 1000: 
                print("Failed 1000 times. Are you sure it is possible to assign recipients under the 'Not Partner' criterion?")
                break
            continue

    return giving_dict


print("Add names here, pressing <enter> after each. Enter 'stop' to stop.\n")

input_list = []

input_name = ""
while input_name != "stop":

    input_name = unique_name(input_list)
    if input_name == "stop":
        break

    while True:
        partner = str(input("Does this person have a partner? (y/n) >>> "))
        if partner not in ['y', 'n']:
            print("Please enter 'y' or 'n'.")
            continue
        else:
            break

    if partner == 'y':
        partner_name = unique_name(input_list, input_name)
        input_list.append([input_name, partner_name])
    elif partner == "n":
        input_list.append(input_name)

print("These people will be exchanging names:\n", input_list)

exchange_dictionary = exchange_names(input_list)

print(exchange_dictionary)
