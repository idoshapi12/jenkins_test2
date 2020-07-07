import random as rand
import sys

# this rand does not include 0. it's can be either 1 or 2
a = rand.randint(0, 3)
b = rand.randint(0, 2)
def main():
	print (str(sys.argv[3]))
	if str(sys.argv[3]) == "test_inputs":
		print (str(sys.argv[1]))
		print (str(sys.argv[2]))
		if int(str(sys.argv[1])) + int(str(sys.argv[2])) <= 2:
			sys.exit("sum is smaller than 3")
	elif str(sys.argv[3]) == "test_rand":
		if a + b <= 2:
			print(a, b)
			sys.exit("sum is smaller than 3")


main()