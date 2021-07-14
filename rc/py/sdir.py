"""	<sdir> Return list of names in a namespace.
"""

# c_L_ocal_A_pplication-imports
import ma as cLAma

# f_function definitions
def main(nParListNames):
	"""	<sdir.main>
"""
	print(main.__doc__,end="")
	print("<scope> : {}".format(__name__))
	print("<namespace> : ",nParListNames)

# special attribute - __name__
if __name__=="__main__": # evaluate current module
	# function main - call
	main(dir(cLAma))