"""	<sb> Plain text file intended to be directly executed. 
"""

# c_L_ocal_A_pplication-imports
import ma as cLAma

# f_function definitions
def main():
	"""	<sb.main>
"""
	print(main.__doc__,end="")
	print("<scope> : {}".format(__name__))

# special attribute - __name__
if __name__=="__main__": # evaluate current module
	print("<__name__> : {}".format(__name__))
	print(__doc__,end="")
	# function main - call
	main()
else:
	print("<__name__> : {}".format(__name__))
	print(__doc__,end="")
	print("<scope> : {}".format(__name__))