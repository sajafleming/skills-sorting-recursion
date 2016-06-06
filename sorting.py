#Sorting

def bubble_sort(lst):
    """returns a sorted list using a optimized bubble sort algorithm
    i.e. using a variable to track if there hasn't been a swap
        >>> bubble_sort([3, 5, 7, 2, 4, 1])
        [1, 2, 3, 4, 5, 7]
    """

    # outer loop looks at the amount of times bubble sort has been through
    # the list.
    for i in range(len(lst) - 1):
        # keep track of whether variables have been swapped for a given round
        have_swapped = False
        for j in range(len(lst) - 1 - i):
            # if the variables are not in order, swap them and assign the outer
            # swapped variable to True
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                have_swapped = True
        if not have_swapped:
            # if nothing swapped then the list is already in order
            break
    return lst


def merge_lists(list1, list2):
    """Given two sorted lists of integers, returns a single sorted list containing all
    integers in the input lists
    >>> merge_lists([1, 3, 9], [4, 7, 11])
    [1, 3, 4, 7, 9, 11]
    """

    sorted_list = []

    while len(list1) > 0 or len(list2) > 0:
        # one list will finish before the other, whichever list finished first,
        # just append the rest of the nonempty list
        if list1 == []:
            sorted_list.append(list2.pop(0))
        elif list2 == []:
            sorted_list.append(list2.pop(0))
        elif list1[0] >= list2[0]:
            # doesn't matter if the values are equal, I just chose to add 
            # the one from the second list first
            sorted_list.append(list2.pop(0))
        else:
            sorted_list.append(list1.pop(0))

    return sorted_list


##########ADVANCED##########
def merge_sort(lst):
    """
    Given a list, returns a sorted version of that list.
    Finish the merge sort algorithm by writing another function that
    that takes in a single unsorted list of integers and uses recursion and the 'merge_lists'
    function you already wrote to return a new sorted list containing all integers from
    thin input list. In other words, the new function should sort a list using merge_lists
    and recursion.
    >>> merge_sort([6, 2, 3, 9, 0, 1])
    [0, 1, 2, 3, 6, 9]
    """
    pass




#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print