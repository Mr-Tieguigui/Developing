# 库有问题

import polyglot
from polyglot.text import Text, Word
# 词性标记
text = Text(u"O primeiro uso de desobediência civil em massa ocorreu em setembro de 1906.")

print("{:<16}{}".format("Word", "POS Tag")+"\n"+"-"*30)
print(text.pos_tags)
for word, tag in text.pos_tags:
    print(u"{:<16}{:>2}".format(word, tag))