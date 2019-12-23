# A script that works in Python 3 (v3.6)
#
# The script returns names for a random gift exchange where
# each recipient is neither the giver nor the giver's partner.
#
# User(s) enter names in the command line, then 'stop'.
# The script then instructs users to look at the screen
# one-at-a-time to recieve their recipient.

import random, os

def unique_name(name_list, partner_of=''):
    '''
    function compares input name to current name_list to check that the entry is unique

    name_list  : list of names already entered

    partner_of : name of person's partner, if specified
    '''

    # create flat list of all names
    list_list = [item if isinstance(item, list) else [item] for item in name_list]
    name_list_flat = [item for sublist in list_list for item in sublist]

    # is this person someone's partner?
    if partner_of == '':
        is_partner = False
    else:
        is_partner = True


    while True:

        # take input name
        if is_partner: 
            input_name = str(input("Enter the name of %s's partner.\n>>> " % partner_of))
        else: 
            input_name = str(input("\nEnter a name (or 'stop').\n>>> "))

        # only take a name input that isn't already in our list
        if input_name in name_list_flat:
            print("Sorry, %s is already in the list. Please enter unique names." % input_name)
            continue
        else: 
            break

    return input_name


def exchange_names(name_list):
    '''
    function returns a dictionary matching givers to recipients

    name_list : a list of names and/or pairs of names to be exchanged
    '''

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



def display_exchange(exchange_dictionary):
    '''
    function displays results of exchange to users

    exchange_dictionary : dictionary where keys are givers and items are recipients
    '''

    clear = lambda: os.system('clear')
    for key in exchange_dictionary.keys():

        clear()
        nothing  = input("\nPrepared to show %s's recipient. Press ENTER when ready.\n"%(key))
        print("*** %s, your recipient is %s. ***\n"%(key, exchange_dictionary[key]))
        nothing = input("Press ENTER to clear the terminal for the next person.")

    clear()
    print("The exchange is complete.")

print("ENTER names below. ENTER 'stop' to stop.\n")

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

print("\nThese people will be exchanging names: \n", input_list)

exchange_dictionary = exchange_names(input_list)

display_exchange(exchange_dictionary)
