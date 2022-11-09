def main(list1):
    """
    A list of several elements is given. Return this list by adding the reverse.
    Args:
        list1(list): parameter
    Returns:
        list: return answer.
    """
    return list1 + list1[::-1]
print(main(['a', 'b', 'c', 'd']))
print(main([0, 1, 2]))
