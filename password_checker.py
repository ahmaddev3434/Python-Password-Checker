def strong_password(password) :
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
        'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
        'u', 'v', 'w', 'x', 'y', 'z'
    ]
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=']
    letters2 = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
        'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
        'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    lower = False
    upper = False
    number = False
    symbol = False
    Length = False
    if(len(password) > 8) :
        Length = True
    for pas in password :
        if(pas in letters) :
            lower = True
        elif (pas in numbers) :
            number = True
        elif(pas in symbols) :
            symbol = True
        elif(pas in letters2) :
            upper = True
        if(lower == True and upper == True and number == True and symbol == True and Length == True) :
            message = f"{password} is a strong password"
        else :
            message = f"{password} is not a strong password"
    return message
            
            
print(strong_password("Ahmad123!"))
print(strong_password("ahmad123!"))
print(strong_password("AHMAD123!"))
print(strong_password("Ahmad!!!!"))
print(strong_password("Ahmad123"))
print(strong_password("A1a!"))
