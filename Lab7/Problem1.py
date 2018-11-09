def unique_elements(list):
    uni_list = []
    for e in list:
        if is_unique(e, list):
            uni_list.append(e)
    return uni_list


def is_unique(element, list):
    count = 0
    for e in list:
        if e == element:
            count += 1
            if count > 1:
                return False
    return True


def main():
    input  = ['H', 'e', 'l', 'l', 'o']
    output = unique_elements(input)

    print(output)


main()
