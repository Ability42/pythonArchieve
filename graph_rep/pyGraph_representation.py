# graph representation
# set(imagine) (a=0, b=0,...)

# - LIKE SETS

a, b, c, d, e, f, g, h = range(8)
N = [
	set(b, c, d, e, f) # a
	set(c, e), # b
	set(d), # c
	set(e), # d
	set(f), # e
	set(c, g, h), # f
	set(f, h), # g
	set(f, g) # h
]

# >>> b in N[a] # adjacent?
# True
# >>> len(N[f]) # power
# 3
# ok....

# - LIKE ADJACENT LISTS





