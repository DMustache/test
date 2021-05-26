def cutter(letter, count):
    return [[letter[i] for i in range(len(letter)) if ( i % count) == r] for r in range(count)]
letter = 'Если плоскость проходит через данную прямую, параллельную другой плоскости, и пересекает эту плоскость, то прямая пересечения плоскостей параллельна данной прямой'
letter = list(letter.split(' '))
difficulty = [3, 4, 5]
#select = int(input(f'Выберите уровень сложность:\n1 - {difficulty[0]} части.\n2 - {difficulty[0]} части.\n3 - {difficulty[0]} частей.\n'))

new = cutter(letter, 3)

print(new)