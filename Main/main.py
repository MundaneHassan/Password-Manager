from cryptography.fernet import Fernet
from secrets import choice


def generate_sum():
    sum = Fernet.generate_key()
    with open("sum.key", "wb") as sum_file:
        sum_file.write(sum)


generate_sum()


def get_sum():
    file = open("sum.key", "rb")
    key_1 = file.read()
    file.close()
    return key_1


key = get_sum()
fer = Fernet(key)


def create_pin():
    pid = input("Enter your pin, please save this pin in a physical location:  ")
    with open("PID.key", 'wb') as pid_file:
        pid_file.write(fer.encrypt(pid.encode()))
        
        
create_pin()


'''
def get_pin(pin: str):
    with open("PID.key", "rb") as pid_file:
        for line in pid_file.readlines():
            data = bytes(line.rstrip())
            line1 = fer.decrypt(data).decode()
    if pin == line1:
        pass
    else:
        exit()


get_pin(input("Please enter your pin here :  "))


def write_password():
    username = input("Enter your username here :  ")
    password = input("Enter your password here, you can type 'generate' to get one : ")

    if password == 'generate':
        ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
        ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        digits = '0123456789'
        punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
        combined = ascii_lowercase + ascii_uppercase + digits + punctuation
        temporary = ''.join(choice(combined) for _ in range(12))
        password = temporary
    else:
        pass

    website_name = input("Enter the website here :  ")
    email_address = input("Enter the email here : ")

    with open("Sign.txt", "a") as file_write:
        file_write.write(
            fer.encrypt(username.encode()).decode() + "\n" + fer.encrypt(
                password.encode()).decode() + "\n" + fer.encrypt(
                email_address.encode()).decode() + "\n" + fer.encrypt(website_name.encode()).decode() + "\n")
    print("\nPassword successfully stored and encrypted.")

    another_password = input("Would you like to write another one?\n")
    if another_password.lower() in ['yes', 'y', 'w', 'write']:
        write_password()
    else:
        exit()

def read_password(Filename : str = "Sign.txt"):
   with open(Filename, 'rb') as file_read:
        content = file_read.readlines()
        print_counter = 0
        for i in range(len(content)):
            print(fer.decrypt(content[i]).decode())
            print_counter += 1
            if (print_counter & 3) == 0:
                print("\n\n")


welcome = input("\nWelcome, would you like to write or read a password today?\n"
                "Please type 'W' for write and 'R' for read :  \n")

if welcome == 'write' or welcome == 'w' or welcome == 'y' or welcome == 'yes':
    write_password()
elif welcome == 'read' or welcome == 'r' or welcome == 'Read' or welcome == 'R':
    read_password()
else:
    print('\nIncorrect input')
    exit()
'''
