import random
import subprocess

print("Hello, world!")

'''
We want to generate some basic arithmetic problems, and typeset them in Tex.
First, let's go ahead and generate some problems : 2-digit addition, for example.
'''

n = random.randint(10,99)
m = random.randint(10,99)

'''
 print('What is ' + str(n) + ' + ' + str(m) + '?')
 Great!  Now we have know how to generate one problem.
 What if we want to generate 10 problems? 15 problems? a user-defined number?
 We use a function.
'''

def gen_problems(num_probs):
    for i in range(0,num_probs):
        n = random.randint(10,99)
        m = random.randint(10,99)
        print('What is ' + str(n) + ' + ' + str(m) + '?')

print('Printing out 10 problems : ')
gen_problems(10)
print('Printing out 20 problems : ')
gen_problems(20)

'''
This doesn't look nice, though - what good is output in a console?
We want a pdf - or at least Tex formatting.
Here's a nice simple example of somebody on the internet with a similar problem :
http://tex.stackexchange.com/questions/270714/automatic-document-generation-based-on-a-database
'''

def write_tex_question(n,m):
    prefix = '\\question \n \\begin{equation*} \n \\begin{array}{c} \n'
    suffix = '\\end{array} \n \\end{equation*} \n \\vspace{\\stretch{1}} \n'
    problem = "\\phantom{+9}%(TOP)s\\\\ \\underline{+\\phantom{9}%(BOTTOM)s}\\\\ \n"
    new_problem = str(problem %{"TOP":n, "BOTTOM":m})
    return prefix + new_problem + suffix


write_tex_question(random.randint(10,99),random.randint(10,99))

'''
Great.  Now we have a bunch of TeX on the screen.
Let's write that out to a file instead.
'''

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

