from cryptography.fernet import Fernet
import os, pickle, secrets, sys

class PasswordManager:

    def __init__(self):
        """
        `__init__()` 
        if `sum.bin` or `PID.bin` not in current directory then,
        will create file(s) and store the require data.
        and run the Initial code.
        """
        if ("sum.bin" not in os.listdir()):
            self.__generate_sum()
            
        self.__get_sum_key()

        if ("PID.bin" not in os.listdir()):
            self.__create_pin()

        self.__get_pin()

        while True:
            
            __welcome = input("\nWelcome, would you like to write or read a password today?\nPlease type 'W' for write and 'R' for read\n- ").lower()

            # if user entered wrong input
            while not ((__welcome[0] in "wy") or (__welcome[0] == "r")):
                print("Incorrect Input!")
                __welcome = input("\nWelcome, would you like to write or read a password today?\nPlease type 'W' for write and 'R' for read\n- ").lower()
            
            if (__welcome[0] in "wy"):
                self.__store_details()
            elif (__welcome[0] == "r"):
                self.__print_details()
            
            # If user want to do more work

            more = input("Want to do more operations (y/n)?- ").lower()
            if (more[0] != "y"):
                print("Program Closed!")
                break
        
    def __generate_sum(self) -> None:
        """
        `generate_sum()`
        generate the sum key and store it in `sum.key` file.
        """

        __sum_key = Fernet.generate_key()

        with open("sum.bin", "wb") as __sum_file:
            pickle.dump(__sum_key, __sum_file)
        
    def __create_pin(self) -> None:
        """
        `create_pin()`
        creates the pin and encode it and encrypt it in `PID.key` file.
        """

        __pin = input("Enter your pin, please save this pin in a physical location: ")
        __encrypted_key = self.__fer.encrypt(__pin.encode())

        with open("PID.bin", "wb") as __pid_file:
            
            pickle.dump(__encrypted_key, __pid_file)
    
    def __get_sum_key(self) -> None:
        """
        `get_sum_key()`
        loads the key from `sum.bin` 
        and assigns the value of key to `self.__fer`.
        """

        with open("sum.bin", "rb") as __sum_file:
            __key = pickle.load(__sum_file)

        self.__fer = Fernet(__key)

    def __get_pin(self) -> None:
        """
        get_pin()
        takes pin from user in string format
        and loads the pin from `PID.bin` file,
        and if user entered pin wrong pin then ask again
        total of 3 times.
        """
        __attempt = 3
        __pin = input("Please enter your pin here: ")

        with open("PID.bin", "rb") as __pid_file:
            __saved_pin = self.__fer.decrypt(pickle.load(__pid_file)).decode()

        while (__pin != __saved_pin):
            __attempt -= 1
            if (__attempt <= 0):
                print("Your chances are over!")
                print("Program Closed!")
                sys.exit()
            
            print("You entered wrong pin!")
            print(f"You have only {__attempt} attempts left!")
            __pin = input("Please enter your pin here: ")


    def __store_details(self) -> None:
        """
        `store_details()`
        input username, password, website_name, email from the user
        and if password is not generated then it can generate the password also
        and encrypt all the details and store it in `Sign.bin` binary file.
        """

        __username = input("Enter your username here: ")
        __password = input("Enter your password here, you can type 'generate' to get one: ")

        # if user wanted to make password
        if (__password.lower() == "generate" or __password.lower() == "generates"):
            self._ASCIIs = [f"{chr(i)}" for i in range(31, 127)]
            __password = "".join([secrets.choice(self._ASCIIs) for _ in range(12)])
            print("Password created Successfully!\n")

        __website_name = input("Enter the website here: ")
        __email = input("Enter the email here: ")

        __details = [__username, __password, __website_name, __email]

        # encrypting the details
        __encrypted_stuff = [self.__fer.encrypt(i.encode()) for i in __details]

        # storing the details
        with open("Sign.bin", "ab") as __sign_file:
            pickle.dump(__encrypted_stuff, __sign_file)
        
        print("\nPassword successfully stored and encrypted.")
    
    def __print_details(self) -> None:
        """
        `print_details()`
        will laod the encrypted details from `Sign.bin` binary file
        and decrypt and print them.
        """
        try:
            __sign_file = open("Sign.bin", "rb")
        except FileNotFoundError:
            print("No details are stored yet!")
            return
        except Exception as __e:
          print(f"Unkown Error occured:\n{__e}")

        try:
            while True:
                # Loading the encrypted details
                __encrypted_details = pickle.load(__sign_file)

                __names = ["Name", "Password", "Email", "Website"]
                
                __details = [self.__fer.decrypt(i).decode() for i in __encrypted_details]
                
                # printing the details
                print(f"{'-'*40}\n{'New group':^40}\n{'-'*40}")
                
                for __name, __detail in zip(__names, __details):
                    print(f"{__name:^15} : {__detail:^15}")
                print("-"*60)
        except EOFError:    # if file ends
            __sign_file.close()
            print("End of Details")
        except Exception as __e:
          print(f"Unkown Error occured:\n{__e}")


if __name__ == "__main__":
    p = PasswordManager()
