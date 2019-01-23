# Stupidsort
# Petri Kemppinen

# Implementing a really stupid sorting algorithm.
# It's basically a bogosort implemented using random's shuffle function.

from random import shuffle


# Print all items in a list.
def print_list(the_list):
    for item in the_list:
        print(item)
    return


def main():
    # Creating a sortable list
    unsorted = []
    new_item = 1

    while new_item != '0':
        new_item = input("Add integer for list, input 0 to stop: ")
        try:
            new_int = int(new_item)
            unsorted.append(new_int)
        except ValueError:
            print("Not an integer, try again.")

    # List has been created.
    print("Ready to sort.")

    is_sorted = False
    # Counting the permutations for the stupid sort.
    perms = 0
    unsorted.sort()

    # Performing the actual stupid sort.
    while is_sorted is False:
        not_unsorted = unsorted.copy()
        shuffle(not_unsorted)
        perms += 1
        print("Permutation", perms, "completed.")

        if not_unsorted == unsorted:
            is_sorted = True

    # List has been bogosorted.
    print("List has been bogosorted. It took", perms, "permutations to "
                                                      "complete.")

    return


main()
