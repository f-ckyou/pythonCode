'''
- Profiling is an analytical process that gathers statistics on a program's behavior, for ex: the number and duration of function calls ..... 
- It tells you exactly what parts of a program are taking the most time or memory.
- The most common way to run cProfile is directly in the interpreter. This lets you dump your output to a text file and view it with a web viewer.
'''
import cProfile
import pallingrams
cProfile.run('pallingrams.find_pallingrams()')