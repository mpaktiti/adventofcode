# Provided main() calls the above function using test() to check if each result is correct or not.
def main():
	print "\n\n\n"
	print "\n\tDay 1: Not Quite Lisp"
	dayOne()
	print "\n\tDay 2: I Was Told There Would Be No Math"
	dayTwo()
	print "\n\tDay 3: Perfectly Spherical Houses in a Vacuum"
	dayThree()
	print "\n\n\n"

def dayOne():
	fhandle = open("day1_inp.txt")
	inp = fhandle.read().rstrip()
	print "\t\tTo what floor do the instructions take Santa? -> " + str(int(inp.count("(")) - int(inp.count(")")))
	floor = 0
	pos = 0
	for ch in inp:
		pos += 1
		floor += 1 if ch=="(" else -1
		if floor == -1: break
	print "\t\tWhat is the position of the character that causes Santa to first enter the basement? -> " + str(pos)

def dayTwo():
	fhandle = open("day2_inp.txt")
	fcontents = fhandle.read().rstrip().split("\n")
	res = 0
	side = [0,0,0]
	ribbon = 0
	for item in fcontents:
		dimensions = map(int, item.split("x"))
		side[0] = dimensions[0] * dimensions[1]
		side[1] = dimensions[1] * dimensions[2]
		side[2] = dimensions[2] * dimensions[0]
		res += 2 * side[0] + 2 * side[1] + 2 * side[2] + min(side)
		ribbon += sorted(dimensions)[0]*2 + sorted(dimensions)[1]*2 + reduce(lambda x, y: x*y, dimensions)
	print "\t\tHow many total square feet of wrapping paper should the elves order? -> " + str(res)
	print "\t\tHow many total feet of ribbon should the elves order? -> " + str(ribbon)

def dayThree():
	x = y = i = santaX = santaY = roboX = roboY = 0
	grid = ['0,0']
	roboGrid = ['0,0']

	fhandle = open("day3_inp.txt")
	inp = fhandle.read().rstrip()
	
	for move in inp:
		i+=1
		if (move == "<"):
			x-=1
			if (i % 2 == 0):
				roboX-=1
			else:
				santaX-=1
		elif (move == ">"):
			x+=1
			if (i % 2 == 0):
				roboX+=1
			else:
				santaX+=1
		elif (move == "^"):
			y+=1
			if (i % 2 == 0):
				roboY+=1
			else:
				santaY+=1
		elif (move == "v"):
			y-=1
			if (i % 2 == 0):
				roboY-=1
			else:
				santaY-=1
		else:
			continue
		coord = str(x) + "," + str(y)
		if (i % 2 == 0):
			coordRobo = str(roboX) + "," + str(roboY)
			if (coordRobo not in roboGrid):
				roboGrid.append(coordRobo)
		else:
			coordSanta = str(santaX) + "," + str(santaY)
			if (coordSanta not in roboGrid):
				roboGrid.append(coordSanta)
		if (coord not in grid):
			grid.append(coord)	
	print "\t\tHow many houses receive at least one present by Santa? -> " + str(len(grid))
	print "\t\tHow many houses receive at least one present by Santa and Robo-Santa? -> " + str(len(roboGrid))

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()