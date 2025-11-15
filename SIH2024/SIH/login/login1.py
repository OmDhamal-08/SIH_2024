import argon2

def hashing_pass(password):
    ph = argon2.PasswordHasher() #creat the object of awrgon library
    hashed_password = ph.hash(password) #hashing password
    return hashed_password

def check_pass(password, hashed_password): # for check the hashed pass and real pass
    ph = argon2.PasswordHasher()
    try:
        ph.verify(hashed_password, password)
        print("Pass is ok")
    except Exception as e:  # to check the mismatched error
        print("Pass is not ok")

def pass_check(password, user_name): 
    if(len(user_name)==0 or len(password)==0):
        print("The username and the password is empty please enter the usename and password")
        return False

    if(len(password)<8 or len(password)>20):
        print("The password is not valid it must contain between 8 and 20 characters")
        return False

    if(password == user_name):
        print("password cant be equal to the usename")
        return False
    
    if not any(num.isdigit() for num in password):
        print("The password should have at least one digit")
        return False
        
    if not any(char.isupper() for char in password):
        print("The password should have at least one uppercase letter")
        return False
        
    if not any(char.islower() for char in password):
        print("The password should have at least one lowercase letter")
        return False
    
    if not any(not char.isalnum() for char in password):
        print("The password should have at least one special character")
        return False
    
    return True

def main():
    print("Enter the user name:")
    user_name = input()
    print("Password must contain one special character,one number,one special character,one lower and upper case letter and the legth of password must be 8")
    print("Enter the password:")
    password = input()
    valid = pass_check(password, user_name)

    if(valid==True):
        print("The password is valid")
    else:
        print("The password is not valid")

    hashed_password = hashing_pass(password)
    print(hashed_password)
    check_pass(password, hashed_password)

if(__name__=="__main__"):
    main()