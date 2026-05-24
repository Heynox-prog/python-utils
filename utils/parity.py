def parity_of_number(number):
    return number % 2 == 0

def parity_of_list(list_items, interested_number = None):
    even_number = []
    odd_number = []

    for number in list_items:
        if number % 2 == 0:
            even_number.append(number)
        else:
            odd_number.append(number)

    if interested_number == "even":
        return even_number
    elif interested_number == "odd":
        return odd_number
    else:
        return even_number, odd_number

def count_of_elements(list_items, interested_number = None):
    even_count = 0
    odd_count = 0

    if interested_number == "total":
        return len(list_items)

    for number in list_items:
        if number % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    if interested_number == "even":
        return even_count
    elif interested_number == "odd":
        return odd_count
    else:
        return even_count, odd_count