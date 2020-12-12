=begin You can do this, or start each line in
a multi-line comment with the # character.
=end

# In Ruby, (almost) everything is an object.
# This includes numbers...
3.class #=> Integer

# ...and strings...
"Hello".class #=> String

# ...and even methods!
"Hello".method(:class).class #=> Method

# Some basic arithmetic
1 + 1 #=> 2
8 - 1 #=> 7
10 * 2 #=> 20
35 / 5 #=> 7
2 ** 5 #=> 32
5 % 3 #=> 2
