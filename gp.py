# -*- coding: utf-8 -*-
import csv, random, os, time

def check(phrase):
    checklist = ['да','lf','ok','щл','yes','нуы']
    string = str(input(phrase)).lower()
    if string in checklist:
        return True
    else:
        return False

class phraseSaver():
    phraselist = r'letters.csv'

    def chunk(letter, lns):
        mv = letter.split()
        letter = [' '.join(mv[x:x+lns]) for x in range(0, len(mv), lns)]
        return ' '.join(random.sample(mv, len(mv)))

    def appendPhraseslist():
        with open(phraseSaver.phraselist, mode='a', encoding='utf-8') as saver:
            writer = csv.writer(saver)
            phrase = str(input('Введите фразу для заоминания: '))
            while check('Если это та фраза, напишите да или ok: ') != True: #Пока не True
                phrase = str(input('Введите фразу для заоминания: '))
            writer.writerow([phrase])

    def showPhraselist():
        with open(phraseSaver.phraselist, mode='r', encoding='utf-8') as viewer:
            reader = csv.reader(viewer)
            return list(reader)

    def selectPhrase():
        lst = phraseSaver.showPhraselist() #list of phrases from csv
        print('Если хотет сами выбрать фразу, нажмите 1.\nЕсли хотите, чтобы за вас выбрал компьютер, нажмите 2.')
        select = str(input())

        if select == '1':
            for i in range(len(phraseSaver.showPhraselist())):
                print(i + 1, *phraseSaver.showPhraselist()[i])
            return phraseSaver.showPhraselist()[int(input()) - 1][0].split(' ')

        elif select == '2':
            return list(lst[random.randint(0, len(lst) - 1 )][0].split(' '))

    def divideByDifficulty(letter, count):
        return [[letter[i] for i in range(len(letter)) if (i % count) == r] for r in range(count)]

    def startTypeLetter(): #Задача игрока написать предложения, основываясь на перемешанные между друг другом слова
        phrase = phraseSaver.selectPhrase()

        print(f'Ваша фраза для запоминания: {" ".join(phrase)}')
        str(input('Введите что либо чтобы начать игру.'))
        os.system('cls')

        shafled = phrase
        while shafled == phrase:
            shafled = random.sample(phrase, len(phrase)) #Перемешивание фразы(список)

        print(" ".join(shafled))

        Stime = time.time()

        while str(input('Введите фразу правильно: ')) != ' '.join(phrase):
            print("\033[A                                                                                                                \033[A")
            continue

        print(f'Вы правильно собрали фразу за {round(time.time() - Stime, 2)} сек.')

    def startCombineLetter():#Перемешиваются эдемнеты внутри двумерного массива, на не среди элемнтов массива
        phrase = ' '.join(phraseSaver.selectPhrase())
        print(phrase)

        difficulty = [3, 4, 5]
        difficultySelected = difficulty[int(input(f'Выберите уровень сложности:\n1 - {difficulty[0]} части.\n2 - {difficulty[1]} части.\n3 - {difficulty[2]} частей.\n')) - 1]
        print(f'Ваша фраза для запоминания: {phrase}')

        str(input('Введите что либо чтобы начать игру.'))
        os.system('cls')

        shafled = phraseSaver.chunk(phrase, difficultySelected)
        while shafled == phrase:
            shafled = phraseSaver.chunk(phrase, difficulty[difficultySelected - 1])
        print(shafled)

        Stime = time.time()
        while str(input('Введите фразу правильно: ')) != phrase:
            print("\033[A                                                                                                                \033[A")
            continue

        print(f'Вы правильно собрали фразу за {round(time.time() - Stime, 2)} сек.')

if __name__=='__main__':

    select = str(input())

    if select.lower() == '1':
        phraseSaver.appendPhraseslist()

    elif select.lower() == '2':
        phraseSaver.startTypeLetter()

    elif select.lower() == '3':
        phraseSaver.startCombineLetter()
#Функция основной игры М процентики