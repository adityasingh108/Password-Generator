def password_generator():
    
    
    """
     This function genrate the random
     Letter,number, or mixture of these number.
    """
    import random
    from datetime import datetime

    lenght = int(input("enter the password Lengh:")) # Enter the lenght of password

    time = datetime.now()
    lower = "abcdefghijklmnopqrstuvwxyz" #lower case
    uper = lower.upper() # upper case
    symbol ="~!@#$%^&*(~!@#$%^&*()"# symbol
    number="`1234567890" #number
    pass_manager = lower+uper+symbol+number
    password =''.join(random.sample(pass_manager,lenght))
    with open("password.txt",'a')as f:
        f.write(f"({password}) ({time})\n")
    print(password)
if __name__ == '__main__':
    password_generator()