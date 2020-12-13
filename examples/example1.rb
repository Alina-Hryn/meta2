=begin You can do this, or start each line in
a multi-line comment with the # character.
=end

# In Ruby, (almost) everything is an object.
# This includes numbers...
3.class #=> Integer

# ...and strings...
"Hello world".class    #=> String

# ...and even methods!
"Hello".method(:class).class #=> Method

# Some basic arithmetic
1 + 1 #=> 2
8 - 1 #=> 7
10 * 2 #=> 20
35 / 5 #=> 7
2 ** 5 #=> 32
5 % 3 #=> 2

class Foo
  def self::some_method
  end
end

# good
class Foo
  def self.some_method1
  end
end

class AliasObject
  attr :foo
  attr_reader :bar
  attr_accessor :baz

  def prep; @foo = 3; @bar = 4; end
  def value; 5; end
  def false_value; 6; end
  def self.klass_method; 7; end
end
