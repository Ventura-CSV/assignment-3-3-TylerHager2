def main():
    email = input('Enter your email: ')
    """
    ########################################
    Code Your Program here
    ########################################
    """
    
    if email[0].isalpha():
        if 5 < len(email) < 30:
            if email.find('@') > 0 and email.find('.') > email.find('@'):
                result = True
            else:
                result = False    
        else:
            result = False
    else:
        result = False
        
    print(result)
    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
