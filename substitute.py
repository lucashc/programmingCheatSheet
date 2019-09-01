#!/bin/env python
import sys
from os import listdir
from os.path import isfile, join

# Get files in directory
algorithm_dir = sys.argv[1]
filelist = [f for f in listdir(algorithm_dir) if isfile(join(algorithm_dir, f))]

def get_lang(f):
    if f[-3:] == ".py": return "python"
    elif f[-5:] == ".java": return "java"
    elif f[-4:] == ".cpp": return "cpp"
    else: return "java"

inclusion = ""
for f in filelist:
    with open(join(algorithm_dir, f)) as file:
            data = file.read()
            title = data.splitlines()[0][2:].strip()
            extra_info = "\n\\\\".join([i.strip()[3:] for i in data.splitlines()[1:] if i.startswith("##")])
            inclusion += r"""
\subsection*{%TITLE%}
%EXTRA%
\begin{lstlisting}[language=%LANGUAGE%]
%FILE%
\end{lstlisting}
""".replace("%LANGUAGE%", get_lang(f)).replace("%FILE%", data.partition('\n')[2]).replace("%TITLE%", title).replace("%EXTRA%", extra_info)

with open("main.tex") as infile:
    print("Writing to file")
    data = infile.read().replace("%PLACEHOLDER%", inclusion)
    if "%PLACEHOLDER" in data: print("fail")
    with open("main_mod.tex", 'w') as out:
        out.write(data)

