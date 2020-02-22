import random

# random password


def random_password(length):
    array = []

    # získat počty jednotlivých typů znaků
    spec_chars = random.randint(1,length//4)
    small_letters = random.randint(2, length//4)
    big_letters = random.randint(2, length//4)
    numbers = length - (spec_chars + small_letters + big_letters)
    print("Special characters\t{}\nSmall letter\t{}\nBig letters\t{}\nNumbers\t{}".format(spec_chars, small_letters, big_letters, numbers))
    for i in range(length):
        result = ""
        while len(result) == 0:
            type = which_type()
            if type == 1 and spec_chars > 0:
                spec_chars -= 1
                result += random_special_char()
            elif type == 2 and small_letters > 0:
                result += random_small_letter()
                small_letters -= 1
            elif type == 3 and big_letters > 0:
                big_letters -= 1
                result += random_big_letter()
            elif type == 4 and numbers > 0:
                result += random_number()
                numbers -= 1
        array.append(result[0])

    return array


def which_type():
    return random.randint(1,4)


def random_big_letter():
    letters = "QWERTZUIOPASDFGHJKLYXCVBNM"
    num = random.randint(0, len(letters)-1)
    return letters[num]


def random_small_letter():
    letters = "qwertzuiopasdfghjklyxcvbnm"
    num = random.randint(0,len(letters)-1)
    return letters[num]


def random_number():
    numbers = "0123456789"
    return numbers[random.randint(0, len(numbers))-1]


def random_special_char():
    special_chars = ",.-?:_!'/)([]{}\\*+&@#"
    num = random.randint(0,len(special_chars)-1)
    return special_chars[num]


def generate_count_char(length):
    pass


# user password


def user_password(length, chosen_word, chosen_num):

    if (len(chosen_num) + len(chosen_word) < length-1) and chosen_num != ".":
        return make_with_word_number(length, chosen_word, chosen_num)
    elif (len(chosen_word)< length -2) and chosen_num == ".":
        return make_with_word(length, chosen_word)
    else:
        print("Your word/numbers is too long, I'm going to you just part of it")


def make_with_word_number(length, word, num):
    word = camelize_word(word)
    spec_chars = length - len(word) - len(num)
    chars = len(word)
    actual_chars = 0
    numbers = len(num)
    actual_numbers = 0
    array = []
    for i in range(length):
        result = ""
        while len(result) == 0:
            type = which_type()
            if type == 1 and spec_chars > 0:
                spec_chars -= 1
                result += random_special_char()
            elif (type == 2 or type ==3) and chars > 0:
                result += word[actual_chars]
                actual_chars += 1
                chars -= 1
            elif type == 4 and numbers > 0:
                result += num[actual_numbers]
                actual_numbers += 1
                numbers -= 1
        array.append(result[0])
    return array


def make_with_word(length)


def camelize_word(word):
    typo = random.randint(2, 3)
    word.lower()
    upgraded_word = ""
    for i in range(len(word)):
        if i % typo == 0:
            upgraded_word += word[i].upper()
        else:
            upgraded_word += word[i]
    return upgraded_word


def make_string(array):
    password = ""
    for i in range(len(array)):
        password += array[i]
    print(password)
    return password


def main():

    # malá písmena
    # velká písmena
    # číslice
    # speciální znaky

    print("Welcome in the PasswordGenerator.")
    length = int(input("Insert the ideal length (minimal length is 8 characters): "))
    while(length < 8):
        length = int(input("Wrong input, please try again: "))
    type = input("Choose, if you want random password (random) or password made from chosen word/nums (user): ")
    while (type != "random") and (type != "user"):
        type = input("Please, insert correct choice")
    array = []
    if type == "user":
        chosen_word = input("Give me the word that you would like to use in your password: ")
        while len(chosen_word) < 2:
            chosen_word = input("Your word should have at least 3 characters. Try again: ")
        chosen_num = input("Would you like to use some favourite number for your password? Type it. If not, enter . : ")
        password = ""
        array = user_password(length, chosen_word, chosen_num)
        print("\nYour generated password is: ")
        password = make_string(array)
        answer = input("Do you like another one? Yes/No: ")
        while answer == "Yes":
            array = user_password(length, chosen_word, chosen_num)
            password = make_string(array)
            answer = input("Do you like another one? Yes/No: ")
    elif type == "random":
        array = random_password(length)
        print("Your generated password is: ")
        password = make_string(array)
        answer = input("Do you like another one? Yes/No: ")
        while answer == "Yes":
            array = random_password(length)
            password = make_string(array)
            answer = input("Do you like another one? Yes/No: ")
    return password

main()