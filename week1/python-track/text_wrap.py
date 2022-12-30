import textwrap

def wrap(string, max_width):
    left = 0
    right = left + max_width
    new_str = ''
    while left <= len(string):
        if right <= len(string):
            new_str += (string[left:right] + '\n')
            left = right
            right = left + max_width
        else:
            new_str += (string[left:]) + '\n'
            left = right
    return new_str
    
    

# if __name__ == '__main__':