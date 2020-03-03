
a = 'Hello'
b = 'multiple nested braces'
c = 'more nested braces'

# how to use single and double quotes
#d = 'it's my birthday today' # this doesn't work
d  = "it's my birthday today" # double quotes works

msg = "{{{}}}, {{{{{}}}}}, {{{{{{{}}}}}}}".format(a, b, c)
print(msg)

# maybe we can make it a bit more readable
s = "{"
t = "}"

msg2 = "{}{}{}, {}{}{}{}{}, {}{}{}{}{}{}{}".format(s, a, t, s, s, b, t,
        t, s, s, s, c, t, t, t)

print(msg2)
