def find_max(lst):
    if not lst:
        raise ValueError("Cannot find max of an empty list")
    return max(lst)

def remove_duplicates(lst):
    return list(dict.fromkeys(lst))

def sum_even_numbers(lst):
    return sum(num for num in lst if num % 2 == 0)