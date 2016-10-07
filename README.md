# Advent of Code

Advent of Code is a series of small programming puzzles for a variety of skill levels. They are self-contained and are just as appropriate for an expert who wants to stay sharp as they are for a beginner who is just learning to code. Each puzzle calls upon different skills and has two parts that build on a theme. For more info click [here](http://adventofcode.com/about).

## Day 1: Not Quite Lisp

Santa was hoping for a white Christmas, but his weather machine's "snow" function is powered by stars, and he's fresh out! To save Christmas, he needs you to collect __fifty stars__ by December 25th.

Collect stars by helping Santa solve puzzles. Two puzzles will be made available on each day in the advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants __one star__. Good luck!

Here's an easy puzzle to warm you up.

Santa is trying to deliver presents in a large apartment building, but he can't find the right floor - the directions he got are a little confusing. He starts on the ground floor (floor 0) and then follows the instructions one character at a time.

An opening parenthesis, (, means he should go up one floor, and a closing parenthesis, ), means he should go down one floor.

The apartment building is very tall, and the basement is very deep; he will never find the top or bottom floors.

For example:
- `(())` and `()()` both result in floor `0`
- `(((` and `(()(()(` both result in floor `3`
- `))(((((` also results in floor `3`
- `())` and `))(` both result in floor `-1` (the first basement level)
- `)))` and `)())())` both result in floor `-3`

To what floor do the instructions take Santa?

### Part 2

Now, given the same instructions, find the __position__ of the first character that causes him to enter the basement (floor `-1`). The first character in the instructions has position `1`, the second character has position `2`, and so on.

For example:

- `)` causes him to enter the basement at character position `1`.
- `()())` causes him to enter the basement at character position `5`.

What is the position of the character that causes Santa to first enter the basement?

### Input data & solution

Puzzle input: [click](https://github.com/mpaktiti/code/blob/master/python/adventofcode/day1_inp.txt)

```python
fhandle = open("day1_inp.txt")
inp = fhandle.read().rstrip()

#part 1
print "\t\tTo what floor do the instructions take Santa? -> " + str(int(inp.count("(")) - int(inp.count(")")))

#part 2
floor = 0
pos = 0
for ch in inp:
	pos += 1
	floor += 1 if ch=="(" else -1
	if floor == -1: break
print "\t\tWhat is the position of the character that causes Santa to first enter the basement? -> " + str(pos)
```

## Day 2: I Was Told There Would Be No Math

The elves are running low on wrapping paper, and so they need to submit an order for more. They have a list of the dimensions (length `l`, width `w`, and height `h`) of each present, and only want to order exactly as much as they need.

Fortunately, every present is a box (a perfect [right rectangular prism](https://en.wikipedia.org/wiki/Cuboid#Rectangular_cuboid), which makes calculating the required wrapping paper for each gift a little easier: find the surface area of the box, which is `2*l*w + 2*w*h + 2*h*l`. The elves also need a little extra paper for each present: the area of the smallest side.

For example:

- A present with dimensions `2x3x4` requires `2*6 + 2*12 + 2*8 = 52` square feet of wrapping paper plus `6` square feet of slack, for a total of `58` square feet.
- A present with dimensions `1x1x10` requires `2*1 + 2*10 + 2*10 = 42` square feet of wrapping paper plus `1` square foot of slack, for a total of `43` square feet.

All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?

### Part 2

The elves are also running low on ribbon. Ribbon is all the same width, so they only have to worry about the length they need to order, which they would again like to be exact.

The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one face. Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present. Don't ask how they tie the bow, though; they'll never tell.

For example:
- A present with dimensions `2x3x4` requires `2+2+3+3 = 10` feet of ribbon to wrap the present plus `2*3*4 = 24` feet of ribbon for the bow, for a total of `34` feet.
- A present with dimensions `1x1x10` requires `1+1+1+1 = 4` feet of ribbon to wrap the present plus `1*1*10 = 10` feet of ribbon for the bow, for a total of `14` feet.

How many total feet of ribbon should they order?

### Input data & solution

Puzzle input: [click](https://github.com/mpaktiti/code/blob/master/python/adventofcode/day2_inp.txt)

```python
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
```

## Day 3: Perfectly Spherical Houses in a Vacuum

Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (`^`), south (`v`), east (`>`), or west (`<`). After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

For example:

- `>` delivers presents to `2` houses: one at the starting location, and one to the east.
- `^>v<` delivers presents to `4` houses in a square, including twice to the house at his starting/ending location.
- `^v^v^v^v^v` delivers a bunch of presents to some very lucky children at only `2` houses.

### Part 2

The next year, to speed up the process, Santa creates a robot version of himself, __Robo-Santa__, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

For example:

- `^v` delivers presents to `3` houses, because Santa goes north, and then Robo-Santa goes south.
- `^>v<` now delivers presents to `3` houses, and Santa and Robo-Santa end up back where they started.
- `^v^v^v^v^v` now delivers presents to `11` houses, with Santa going one direction and Robo-Santa going the other.

### Input data & solution

Puzzle input: [click](https://github.com/mpaktiti/code/blob/master/python/adventofcode/day3_inp.txt)

```python
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
```