# Stupidsort
# Petri Kemppinen

# Implementing a really stupid sorting algorithm.

from random import shuffle


def stupidsort(old_list):
    new_list = shuffle(old_list)
    return new_list


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

    print("Ready to sort.")

    is_sorted = False
    perms = 0
    not_unsorted = []

    while is_sorted is False:
        not_unsorted = stupidsort(unsorted)
        perms += 1
        print("Permutation", perms, "completed.")

        if not_unsorted == unsorted.sort():
            is_sorted = True

    print("List has been bogosorted. It took", perms, "permutations to "
                                                      "complete.")
    for item in not_unsorted:
        print(item)


main()
