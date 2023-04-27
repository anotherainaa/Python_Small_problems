# Python_Small_problems
Personal repo improving proficiency in Python

## Notes on Python behaviour

### 2 categories of data structures

#### Primitive Data structures examples:
- Integer
- Float
- String
- Boolean

※ Note that primitive data types are immutable

#### Non-Primitive Data structure examples:
- Arrays
- Lists
- Sets
- Files

### Variable scoping rules

- global scope vs local scope
  - a variable defined in the main body is a global variable and are available to all code?
  - anything defined in a local scope are only visible to the code within the scope e.g top level variable in a function is accessible to an inner function defined within the function

### Functions

- Defined using `def` keyword
- must be called with the correct number of arguments, error thrown otherwise
- must explicitly return values using `return` keywords

### Truthiness / Falsiness

Values considered false:
- `None`
- `False`
- Zero or any numertic type referring to 0
- empty sequences
- empty mappings

Everything else is considered truthy


### Classes

- Python supports multiple inheritance
  - note the diamond problem (also present when dealing with mixins, in Ruby, the order of mixin matters)
  - say A, B, C, D
    - B and C inherits from A
    - D inherits from B and C
    - if D calls a method defined in A, and B and C has overridden the method differently, which class does it inherit from?
    - to figure out how it's resolved, learn `__mro__` in Python
- TO check the base classes of a class use `__class__.__bases__`
- To check method resolution order use `__class__.__mro__`

TODO: Fill in some basic notes on these things 

- Precendence
- common declarative style loops and how to use them
  - filter/select
  - map
  - each
- Primitive types? - mutability/ immutability
- Pointers / References? 
- printing stuff on console, formatting strings
- python style guide
