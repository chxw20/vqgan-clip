import os
import sys
from nltk.tokenize import sent_tokenize

#fnames = ["Cinderella.txt"]
dname = "children"
fnames = os.listdir(dname)
for fname in fnames:
    title = fname.replace(".txt", '')
    print(title)
    print("=============================================")
    lines = open(f"{dname}/{fname}").read().splitlines()
    sents = []
    for line in lines:
        if line == '' or line[0] == '=' or line == '\n':
            continue
        tokenized = sent_tokenize(line)
        tokenized = [tok for tok in tokenized if len(tok.split()) > 7]
        sents.extend(tokenized)

    if not os.path.exists(f"output/{title}"):
        os.makedirs(f"output/{title}")
    f_out = open(f"output/{title}.txt", 'w')
    print(len(sents))
    for (i, sent) in enumerate(sents):
        f_out.write(sent + '\n')
        print(f"[{i+1}/{len(sents)}] {sent}")
        print("------------------------")
        sent = sent.replace('"', "'")
        os.system(f'python generate.py -p "{sent}" -o "output/{title}/{i+1}.png" -cd cuda:1')
