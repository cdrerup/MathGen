import random
import subprocess

'''
We want to generate some basic arithmetic problems, and typeset them in Tex.

Somebody with a similar problem :
http://tex.stackexchange.com/questions/270714/automatic-document-generation-based-on-a-database
'''

def write_tex_question(n,m):
    prefix = '\\question \n \\begin{equation*} \n \\begin{array}{c} \n'
    suffix = '\\end{array} \n \\end{equation*} \n \\vspace{\\stretch{1}} \n'
    problem = "\\phantom{+9}%(TOP)s\\\\ \\underline{+\\phantom{9}%(BOTTOM)s}\\\\ \n"
    new_problem = str(problem %{"TOP":n, "BOTTOM":m})
    return prefix + new_problem + suffix

num_probs = 20

worksheet_preamble = '\\documentclass[twocolumn,fleqn]{exam} \n \\usepackage{amsmath} \n \\begin{document} \n \n \\begin{questions}\n'
worksheet_epilogue = '\\end{questions} \n \\end{document}'

TexFileName = 'RandomHomework.tex'
TexFile = open(TexFileName, 'w')

TexFile.write(worksheet_preamble)
for i in range(0,num_probs):
    n = random.randint(10,99)
    m = random.randint(10,99)
    TexFile.write(write_tex_question(n,m))
TexFile.write(worksheet_epilogue)
TexFile.close()

#And now we convert the tex file to PDF, Windows willing.
subprocess.call(['pdflatex.exe',TexFileName])

