
def pivot_sort(arr):
    """
    Sorts a list in ascending order using a pivot sort algorithm.
    
    Parameters:
    arr (list): The list to be sorted.
    
    Returns:
    None: The list is sorted in place.
    """
    if len(arr) <= 1:
        return

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    arr[:] = left + middle + right
    pivot_sort(left)
    pivot_sort(right)
