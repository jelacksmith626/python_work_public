import string, random
from random import sample

def upletter():
    if __name__=='__main__':
        letter = random.choice(string.ascii_letters)
        password.append(letter)
def lowletter():
    if __name__ == '__main__':
        letter = random.choice(string.ascii_letters)
        password.append(letter.lower())
def number():
    rand_number = ['0','1','2','3','4','5','6'
                   ,'7','8','9']
    number = random.choice(rand_number)
    password.append(number)
pass_gen = ['number','upletter']
password = []
password_length = input('Give me a password length: ')
try:
    password_length = int(password_length)
except ValueError:
    print("You can't have a letter as a number!")
    
else:
    while len(password) < password_length:
        pass_gen_choice = random.choice(pass_gen)
        if pass_gen_choice == 'upletter':
            upletter()
        elif pass_gen_choice == 'number':
            number()
        elif pass_gen_choice == 'lowletter':
            lowletter()

    
password = ''.join(password)
print(password)