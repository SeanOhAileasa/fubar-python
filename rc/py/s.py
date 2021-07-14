"""s <Plain text file intended to be directly executed.>"""

# a_S_tandard_L_ibrary-imports
from sys import path as aSLsp
# module sys - name path alias aSLsp - modify
aSLsp.append(r"c:/Users/E6985/L8733/src/pro/par/pyt")

# c_L_ocal_A_pplication-imports
import cMod

# f_function definitions
def main():
    """s.main"""
    print("<docstring> : {}".format(main.__doc__,end=""))
    print("    <scope> : {}".format(__name__))

# special attribute - __name__
if __name__=="__main__": # evaluate current module
    print(" <__name__> : {}".format(__name__))
    print("<docstring> : {}".format(__doc__,end=""))
    # function main - call
    main()
