import os
script_dir = os.path.dirname(__file__)
rel_path = "messier.txt"
abs_file_path = os.path.join(script_dir, rel_path)

for line in open(abs_file_path, encoding='latin_1'):
    if not (line.startswith("M")):
        pass
    else:
        M = (line[0:6]).rstrip()
        N = (line[6:40]).rstrip()
        if N == "":
            N = "no name"
        Cl = (line[40:64]).rstrip()
        G = line[64:].rstrip()
        print(f"|{M}|{N}|{Cl}|{G}|")
