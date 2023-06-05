from random import randint
collors = 'ropcgy'


def no_rep_code():
    used_colors = []
    code = ''
    i = 0
    while i in range(4):
        col = collors[randint(0, 5)]
        if col not in used_colors:
            code += col
            used_colors.append(code[-1])
            i += 1
    return code


def rep_code():
    code = ''
    for i in range(4):
        code += collors[randint(0, 5)]
    return code


cypher = no_rep_code()
print(cypher)
print('Available colors: \n', list(collors))
while True:
    guess = input()
    hint = ''
    delleted = ''
    guess_used_colors = list(cypher)
    for i in range(len(guess)):
        if guess[i] == cypher[i]:
            hint += 'r'
            guess_used_colors.remove(guess[i])
            delleted += guess[i]
    for letter in delleted:
        guess = guess.replace(letter, '', 1)

    for letter in guess:
        if letter in cypher and letter in guess_used_colors:
            hint += 'w'
            guess_used_colors.remove(letter)

    if hint == 'rrrr':
        print('You Win')
        break
    else:
        print(hint)
