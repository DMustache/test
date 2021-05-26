#region Мешает части предложения между собой
letter = 'Если плоскость проходит через данную прямую, параллельную другой плоскости, и пересекает эту плоскость, то прямая пересечения плоскостей параллельна данной прямой'

import random
def chunk(st, lns):
    mv = st.split()
    mv = [' '.join(mv[x:x+lns]) for x in range(0, len(mv), lns)]
    return ' '.join(random.sample(mv, len(mv)))

print(chunk(letter, 3))
#endregion

#region autocmplete
import readline

def completer(text, state):
    options = [i for i in commands if i.startswith(text)]
    if state < len(options):
        return options[state]
    else:
        return None

readline.parse_and_bind('tab: complete')
readline.set_completer(completer)
#endregion