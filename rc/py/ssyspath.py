"""	<ssyspath> Directory containing script used to invoke interpreter.
"""

# a_S_tandard_L_ibrary-imports
from sys import path as aSLsyspath

# f_function definitions
def main():
	"""	<ssyspath.main>
"""
	# module sys - name path - call alias
	print(aSLsyspath[0])

# special attribute - __name__
if __name__=="__main__": # evaluate current module
	# function main - call
	main()