def starts_with(string_one, string_two):
    ''' Function taking two strings and returning true if the first argument starts with the second one.'''
    return string_one.startswith(string_two)

def ends_with(string_one, string_two):
    '''Function taking two strings and returning true if the first argument ends with the second one.'''
    return string_one.endswith(string_two)

def swap_strings(string_one, string_two):
    '''Function taking two strings and swapping their values.'''
    return string_two, string_one

def find_last_not_of(string, character):
    '''Function taking a string and a character
    sequence as its arguments. The function returns the last character equal
      to none of the characters in the given character sequence.'''
    result = string.rfind(character)
    if result == -1:
        return None
    return string[result]

def convert_to_int(string):
    try:
        result = int(string)
        return result
    except ValueError:
        print('Conversion is not possible')

def rotate_by(string, number):
        '''function taking an integer array and
        a number as its arguments. The function returns the array
        rotated by the specified number of positions (given by the second argument).'''
        return string[number:] + string[:number]
