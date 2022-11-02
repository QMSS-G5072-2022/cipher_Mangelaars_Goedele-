def cipher(text, shift, encrypt=True):
    '''The cipher function takes a string and shifts it by a number of letters defined by the shift parameter.
    
    Inputs:
    text: A string that needs to be encrypted
    shift: the numberical value of the number by which you want to encrypt the string parameter
    
    Output: 
    The output will be an encrypted string, where the letters of the string have been shifted by the value defined in the shift input.

    Example: 
    Input: Hello 
        cipher(Hello, 1)
    Output: Ifmmp

    A great use case for this is sending encrypted messages over a messaging service. 
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text
