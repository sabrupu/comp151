# Input : [2, 4, 6, 8, 10]
# Output: [4, 8, 12, 16, 20]

def double_list(list):
    doubled_list = []

    for i in list:
        doubled_list.append(i * 2)

    return doubled_list

