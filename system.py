from beauty_things import text_color
from beauty_things import colors
import checkers
from quiz_questions import quiz


print(text_color('Quiz', colors['blue']).center(38))

while True:
    re_start = True
    start = checkers.yes_no('Start: [Y/N] ')
    if start:
        while True:
            result = 0
            for question in quiz:
                print('-' * 30)
                print(question['question'])
                for c, ans in enumerate(question['answers']):
                    print(f'\n{c + 1} - {ans['answer']}'.title())
                while True:
                    try:
                        user_answer = int(input('Answer: '))
                    except KeyboardInterrupt:
                        print(text_color('\nPlease answer something!', colors['yellow']))
                    except:
                        print(text_color('Please type a valid number!', colors['yellow']))
                    else:
                        if len(question['answers'])+1 > user_answer > 0:
                            break
                        else:
                            print('Please type a valid option! ')
                if question['answers'][user_answer-1]['is_correct']:
                    print(text_color('You are right!', colors['green']))
                    result += 1
                else:
                    print(text_color('You are wrong!', colors['red']))
            print('-' * 30)
            print(f'You got {result} questions right!')
            re_start = checkers.yes_no('Do you wanna do the quiz again? [Y/N] ')
            if not re_start:
                break
    elif start is None:
        print(text_color("Please type 'Y' or 'N'", colors['yellow']))
    else:
        print(text_color('User chose to not play', colors['yellow']))
        break
    if not re_start:
        break