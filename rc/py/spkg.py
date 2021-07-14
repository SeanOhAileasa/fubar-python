"""	<spkg> Plain text file intended to be directly executed. 
"""

# c_L_ocal_A_pplication-imports
import cPkg

# f_function definitions
def main():
	"""	<spkg.main>
"""
	print(main.__doc__,end="")
	print("<scope> : {}".format(__name__))
	# package cPkg - name nName - call alias
	print(cPkg.nName)

# special attribute - __name__
if __name__=="__main__": # evaluate current module
	print(__doc__,end="")
	# function main - call
	main()