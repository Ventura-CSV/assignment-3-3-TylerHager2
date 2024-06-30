def main():
    email = input('Enter your email: ')
    """
    ########################################
    Code Your Program here
    ########################################
    """
    length = len(email)
    
    if email[0].isalpha():
        if 5 < length < 30:
            result = True
    else:
        result = False
        
    print (result)
    print (length)
    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
