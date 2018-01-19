import time
import random


def main():
    mult_choice, div_choice = choices()

    if mult_choice:
        mult_questions = list()

        print("\n\nIf you wish to stop entering what you want to practise input 'stop'")
        while True:
            timestable = input("Please input a timestable you want to practise: ").lower()
            if timestable == "stop":
                if len(mult_questions) < 1:
                    print("\nYou must have entered at least one timestable you wish to practise")
                else:
                    break
            else:
                if len(timestable) > 2:
                    print("\nPlease do not input more than 2 digits")
                else:
                    check = check_numbers(timestable)
                    if check:
                        timestable = int(timestable)
                        if timestable not in mult_questions:
                            mult_questions.append(timestable)
                        else:
                            print("\nYou have already input this timestable")
                    else:
                        print("\nPlease input a number or 'stop' if you want to stop entering timestables")

        while True:
            high_mult = input("\nPlease input the highest multiple you want to practise with: ")
            if len(high_mult) > 2:
                print("\nPlease do not input more than 2 digits")
            else:
                check = check_numbers(high_mult)
                if check:
                    high_mult = int(high_mult)
                    if high_mult < 2:
                        print("\nPlease do not input a number less than 2")
                    else:
                        break
                else:
                    print("\nPlease input a number greater than 2")

        while True:
            low_mult = input("\nPlease input the lowest multiple you want to practise with: ")
            check = check_numbers(low_mult)
            if check:
                low_mult = int(low_mult)
                if low_mult < 0:
                    print("\nPlease do not input a number less than zero")
                elif low_mult >= high_mult:
                    print("\nThis number has to be smaller than the highest number which is ", high_mult)
                else:
                    break
            else:
                print("\nPlease input a number greater than 0")

    if div_choice:
        div_questions = list()

        print("\n\nIf you wish to stop entering what you want to practise please input 'stop'")
        while True:
            divisor = input("Please input a divisor with which you want to practise: ").lower()
            if divisor == "stop":
                if len(div_questions) < 1:
                    print("\nYou must have entered at least one divisor before ending")
                else:
                    break
            if len(divisor) > 2:
                print("\nPlease do not input more than 2 digits")
            else:
                check = check_numbers(divisor)
                if check:
                    divisor = int(divisor)
                    if divisor not in div_questions:
                        div_questions.append(divisor)
                    else:
                        print("\nYou have already entered this divisor")
                else:
                    print("\nPlease input a number with up to 2 digits")

        while True:
            high_div = input("\nPlease input the highest multiple of the divisors with which you want to practise: ")
            if len(high_div) > 2:
                print("\nPlease do not input more than 2 digits")
            else:
                check = check_numbers(high_div)
                if check:
                    high_div = int(high_div)
                    if high_div < 2:
                        print("\nPlease input a number greater than 1")
                    else:
                        break
                else:
                    print("\nPlease input a number with up to 2 digits")

        while True:
            low_div = input("\nPlease input the lowest multiple of the divisors with which you want to practise: ")
            check = check_numbers(low_div)
            if check:
                low_div = int(low_div)
                if low_div < 1:
                    print("\nPlease input a number greater than 0")
                elif low_div >= high_div:
                    print("\nThis number must be less than the highest number which is ", str(high_div))
                else:
                    break
            else:
                print("\nPlease input a number with up to 2 digits greater than 0")

    print("\nYou can either do a number of questions or try to do as many questions as you can within a time limit")
    while True:
        choice = input("Please input yes if you wish to be timed, otherwise input no to specify the number of questions you want").lower()
        check = check_numbers(choice)
        if not check:
            choice = str(choice)
            if choice == "yes":
                timed = True
                break
            elif choice == "no":
                timed = False
                break

    if timed:
        while True:
            time_limit = input("How many minutes do you want?")
            check = check_numbers(time_limit)
            if check:
                time_limit = int(time_limit)
                if time_limit == "0":
                    print("Please input a number greater than 0")
                else:
                    time_limit *= 60
                    question_number = 1
                    break
            else:
                print("Please input a number")

    else:
        while True:
            question_number = input("How many questions do you want?")
            check = check_numbers(question_number)
            if not check:
                print("Please input a number greater than 0")
            if check:
                question_number = int(question_number)
                if question_number == 0:
                    print("Please input a number greater than 0")
                else:
                    break
            else:
                print("Please input a number")

    wrong_answers = list()
    correct_answers = list()
    # gets the start time if its needed
    if timed:
        start_time = int(time.clock())
    while question_number > 0:
        # if the user wants to do both multiplication and division
        if mult_choice and div_choice:
            type_choice = random.randint(1, 100)
            # if the number is less than 50 then the question is for multiplication
            if type_choice < 51:
                question, answer = multiplication_question(mult_questions, low_mult, high_mult)
            # otherwise its a division question
            else:
                question, answer = division_question(div_questions, low_div, high_div)
        # if the user only wants multiplication
        elif mult_choice:
            question, answer = multiplication_question(mult_questions, low_mult, high_mult)
        # otherwise the user wants division
        elif div_choice:
            question, answer = division_question(div_questions, low_div, high_div)
        # user only receives 3 chances
        chances = 3
        while chances > 0:
            # gets the user input
            response = input("What is  " + question + "?")
            check = check_numbers(response)
            if check:
                response = int(response)
                answer = int(answer)
                question_answer = question + " = " + str(answer)
                if response == answer:
                    print("Correct")
                    if question_answer not in correct_answers:
                        correct_answers.append(question_answer)
                    chances = 0
                else:
                    print("Incorrect")
                    if question_answer not in wrong_answers:
                        wrong_answers.append(question_answer)
                        chances -= 1
            else:
                print("Please input a number")
        if timed:
            current_time = int(time.clock())
            if current_time - start_time > time_limit:
                question_number = 0
        else:
            question_number -= 1

    while True:
        print("If you wish to see what you got correct input 1")
        print("If you wish to see what you got wrong input 2")
        print("If you wish to exit the program input 3")
        choice = input("Please input your choice here: ")
        check = check_numbers(choice)
        if check:
            choice = int(choice)
            if choice == 1:
                for question in correct_answers:
                    print(question)
                    time.sleep(0.1)
            elif choice == 2:
                for question in wrong_answers:
                    print(question)
                    time.sleep(0.1)
            elif choice == 3:
                break
            else:
                print("Please input 1,2 or 3")

        else:
            print("Please input 1, 2 or 3")


def multiplication_question(mult_questions, low_mult, high_mult):
    first_num = random.randint(low_mult, high_mult)
    second_num = random.choice(mult_questions)
    answer = first_num * second_num
    question = str(first_num) + " * " + str(second_num)
    return question, answer


def division_question(div_questions, low_div, high_div):
    first_num = random.randint(low_div, high_div)
    second_num = random.choice(div_questions)
    multiple = first_num * second_num
    question = str(multiple) + " / " + str(second_num)
    return question, first_num


def choices():
    while True:
        while True:
            m_choice = input("\nDo you want to practise multiplication?\n").lower()
            if m_choice == "yes":
                multiplication = True
                break
            elif m_choice == "no":
                multiplication = False
                break
            else:
                print("\nPlease input either yes or no")
        while True:
            d_choice = input("\nDo you want to practise division?\n").lower()
            if d_choice == "yes":
                division = True
                break
            elif d_choice == "no":
                division = False
                break
            else:
                print("\nPlease input either yes or no")
        if multiplication or division:
            break
        else:
            print("You must choose to do either multiplication or division")
    return multiplication, division


def check_numbers(inputs):
    for character in inputs:
        ascii = ord(character)
        if not 47 < ascii < 58:
            return False
    return True

main()
