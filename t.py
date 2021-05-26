#region Мешает части предложения между собой
def too():
    letter = 'Если плоскость проходит через данную прямую, параллельную другой плоскости, и пересекает эту плоскость, то прямая пересечения плоскостей параллельна данной прямой'

    import random
    def chunk(st, lns):
        mv = st.split()
        mv = [' '.join(mv[x:x+lns]) for x in range(0, len(mv), lns)]
        return ' '.join(random.sample(mv, len(mv)))

    print(chunk(letter, 3))
#endregion

#region autocmplete
#endregion