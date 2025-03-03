def pivot_sort(arr):
    """
    Sorts a list in ascending order using a pivot sort algorithm.
    
    Parameters:
    arr (list): The list to be sorted.
    
    Returns:
    None: The list is sorted in place.
    """
    # Base case: if the list is empty or has one element, it is already sorted
    if len(arr) <= 2:
        return

    # Choose the pivot element (middle element of the list)
    pivot = arr[len(arr) // 2]

    # Partition the list into three parts: elements less than the pivot,
    # elements equal to the pivot, and elements greater than the pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Concatenate the partitions and update the original list
    arr[:] = left + middle + right

    # Recursively sort the left and right partitions
    pivot_sort(left)
    pivot_sort(right)
