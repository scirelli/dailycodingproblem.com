#!/usr/bin/env python3

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

#/////////////// ignore above this line ////////////////////
def car(cons):
	def fnc(a, b):
		return a
	return cons(fnc)

def cdr(cons):
	def fnc(a, b):
		return b
	return cons(fnc)

fnc = cons(3, 4)
print('car: ', car(fnc))
print('cdr: ', cdr(fnc))
