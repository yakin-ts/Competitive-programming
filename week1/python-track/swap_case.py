def swap_case(s):
    res =''
    for item in s:
        if item.islower():
            res += item.upper()
        elif item.isupper():
            res+= item.lower()
        else:
            res+= item
    return res

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)