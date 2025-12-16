def sum(arr: list) -> int:
    """
    Modify the function such that it returns the sum of all numbers within the given list.
    :param arr:
    :return:
    """
    total = 0
    for num in arr:
        try:
            total += num
        except:
            continue

    return total


def cleanData(rawData: list) -> list:
    """
    modify the function such that it takes in a list as an argument will return a new list that
    contains only the values that can be typecast to a float.
    :param rawData:
    :return:
    """
    result = []
    for item in rawData:
        try:
            float(item)
            result.append(float(item))
        except:
            continue
    return result


def unreliableCalculator(divisors: list) -> list:
    """
    Modify the function such that it takes in a list as an argument and returns a new list where each
    index is 100 divided by the values from the input list.
    If division ever causes an error instead have the value be the type of error as a string.
    Example the list [100,50,25,"5"] as an argument would return [1, 2, 4, "TypeError"]
    :param divisors:
    :return:
    """
    result = []
    for divisor in divisors:
        try:
            value = 100 / divisor
            result.append(value)
        except Exception as e:
            result.append(type(e).__name__)
    return result


def upperAll(arr: list) -> None:
    """
    Modify the function such that it uppercases all strings within the given argument list.
    The string method .upper() turns all characters in a string uppercase.
    You should modify the original list not return a new list.
    :param arr:
    :return:
    """
    for i in range(len(arr)):
        try:
            arr[i] = arr[i].upper()
        except:
            pass


def firstItems(arr: list) -> list:
    """
    Modify the function below such that given a list of values. Many of the list elements will be lists
    themselves. For any list element that is a list grab the first element from that list. If the list
    element is not a list then just grab the value itself.
    Create a new list of all the first indexes of inner lists or just values themselves.
    Example firstItems([[1,2],[3,4],[5,6],[7,8],9]) == [1,3,5,7,9]
    :param arr:
    :return:
    """
    result = []
    for item in arr:
        try:
            # Try to access the first element (assumes it's a list)
            result.append(item[0])
        except:
            # If it fails, it's not a list, so just append the item itself
            result.append(item)
    return result


