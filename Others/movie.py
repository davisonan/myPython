#!/usr/bin/python -tt

def fun1(input):
	p1=input.find('wiki')+7
	p2=input.find(",",p1)-1
	return input[p1:p2]

def main():
	with open('movie.txt', 'r') as f:
		for i, line in enumerate(f):
			if i > 0:
				parts = line.split('\t')
				fun1(parts[2])

if __name__ == "__main__":
    main()


import ast
def movie(input):
	l = ast.literal_eval(input)
	for item in l:
		if item['name'] == 'KgMovies':
		return item['wiki']