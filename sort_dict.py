# Goal is to reorder the dict based on the values in the key-value pairs
# Author: Constantine Zahariev, April 2025


def sort_dict(input_dict, time_years):

    # Loop through the number of years for which we have data
    # Number of years = number of list rows for each key the dictionary
    for t in range(1, time_years+1):

        # We need to reset the data structures below with each loop iteration
        # Otherwise they get bigger, but we want to return 3-keys and 3-values with each loop
        new_dict_keys_and_totals = {}
        curr_year_lists = []
        keys_list = []

        year_index = t-1    # Year index for accessing list elements etc

        # Checking the years are evaluated sequentially
        print(f"Year {t}, values index {year_index}")

        # For every key, extract the current year's list of data
        for key, value in input_dict.items():

            # Access current year list
            current_list = value[year_index]

            # Check current list
            # print(f"Current year's list: {current_list}")

            # Sum of current year list rounded
            curr_list_sum = round(sum(current_list), 3)

            # Put the sums into a new dictionary that we can sort
            new_dict_keys_and_totals[key] = curr_list_sum

            # Next, we should sort the dict above by the sums
            sorted_sums = dict(sorted(new_dict_keys_and_totals.items(),
                                      key=lambda item: item[1], reverse=True))

        # Checking the intermediate dictionary
        print("New dict of keys and sums", new_dict_keys_and_totals)
        print("Sorted sums dict", sorted_sums)

        for k in list(sorted_sums.keys()):
            # Verification of output
            # print(f"The year is {t} and the country is {k}")
            print(f"{k}, year {t}")

            # We need to reset 'curr_year_lists' with every iteration of the years loop
            # Append the keys and the corresponding value lists
            # to their own lists before zipping
            curr_year_lists.append(input_dict[k][year_index])
            keys_list.append(k)

            # We can print the lists for the current year
            # print(curr_year_lists)
            # We can also print the ordered keys
            # print(k)

            # Use the 'zip' function to combine the keys and lists from
            # the current year in the loop

    # At the end of the years loop we can create the sorted dictionary
    sorted_dict = dict(zip(keys_list, curr_year_lists))
    print(sorted_dict)

    return sorted_dict


# Call our function (testing)
# sort_dict(test_dict, 6)
