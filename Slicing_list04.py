def main(list1):
    """
    A list of several elements is given. Return the three elements from the beginning.
    Args:
        list1(list): parameter
    Returns:
        list: return answer.
    """
    return list1[0:3]
print(main(['a', 'b', 'c', 'd']))
print(main(['a', 1, 'b', 2, 'c', 3, 'd', 4]))
