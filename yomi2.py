import sys
from Kana import Kana

kana_table = []

if len(sys.argv) != 2:
    print("Usage: " + sys.argv[0] + " [pinyin]")
    exit(1)

with open('kanji.txt', 'r', encoding='utf-16') as f:
    lines = f.readlines()
    for line in lines:
        token = line.strip('\n').split('\t')
        k = Kana(token[0], token[1], token[2])
        kana_table.append(k)
f.close()

for k in kana_table:
    if k.is_match(sys.argv[1]):
        k.print_kana()
