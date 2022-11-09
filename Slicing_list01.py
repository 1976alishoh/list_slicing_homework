def main(numbers):
    """
    A list called numbers is given. Return the items in the odd position.
    Args:
        numbers(list): parameter
    Returns:
        list: return answer.
    """
    i = 0
    l = []
    while i < len(numbers):
        if i % 2 ==0:
            l.append(numbers[i])
        
        i = i +1
    return l
print(main([1, 2, 3, 4, 5]))
print(main([0, 1, 2, 3, 4, 5]))
