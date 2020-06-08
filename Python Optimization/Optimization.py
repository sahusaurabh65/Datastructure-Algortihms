"""Topic :  Differnt kinds, ways and levels  for  optimizaion of Python code """

"""
1   Count element in a list
2   Filter the list
3   Permission or Forgivness?
4   Membership Testing
5   Removing Duplicates 
6   Sorting the elements of list 
7   1000 operation and 1 function
8   Checking for true 
9   Checking for false
10  Checking for Empty list
11  Def vs Lambda 
12  Variable lookup
"""


import timeit
from numpy import random


class Py_Optmize_example:
    def __init__(self,Million_numbers):
        Million_numbers = [random() for _ in range(1000000)]
        self.Million_numbers = Million_numbers

    """ Task 1: count element in a list """
    def count_elements (self):
        how_many  = 0
        for element in self.Million_numbers:
            how_many +=1
        print(how_many)                 # slower

        """approx 68 builtin function try to use it e.g 'len' """
        print (len(self.Million_numbers))   # useful to use builtin function for optimization


    """ Task 2: Filter the list """
    def filter_list(self):
        output = []
        # approach 2.1
        for element  in self.Million_numbers :
            if element % 2:
                output.append(element)  # slower

        #approach 2.2:
        filt_slow = list (filter (lambda x:x %2,self.Million_numbers))     # slower

        # approach 2.3:
        """use list comprehension insted of builtin function
           Result   75% faster than for loop """
        filt_fast = [item for item in self.Million_numbers if item %2]    # faster to use list comprehension


    """ Task 3 : Permission or Forgivness?"""
    def Permission_Forgiveness(self):
    #""" A -> Begging for Permission """
        class  Foo(object):
            hello  = "World"
        foo = Foo()

        # approach 3.1:
        if hasattr(foo,"hello"):     # slower
            foo.hello

        # approach 3.2 :             # faster to use
        """ 3.5 times faster """
        try :
            foo.hello
        except AttributeError:
            pass

        """Lets try it on more condition"""
        # approach3.3
        if (hasattr(foo, "foo") and hasattr(foo,"bar") and hasattr(foo,"baz")):        # slower
            foo.foo
            foo.bar
            foo.baz

        # approach 3.4
        """ 3.64 times faster than approach 3.3 """
        try:
            foo.foo
            foo.bar
            foo.baz
        except AttributeError:
            pass

    #""" B -> Asking for permission """
        """ Sometimes begging for forgivness is expensive than asking for permission 
        
         Conclucion : 
            Rule 1  When you expect that your code will work most of time use try-except as show in appaorach 3.2 and 3.4
            Rule 2  When you likely know that attribute  will be missing and can get some error or can you can predict some 
                    of such attribute  as shown in approach 3.5 and 3.6"""

        # approach 3.5
        class Bar(object):
            pass
        bar = Bar()

        if hasattr(bar,'hello'):                                # faster as compare with 3.6
            bar.hello

        # approach 3.6
            try:                                                #slower as compare to 3.5
                bar.hello
            except AttributeError:
                pass



    """ task 4 : Membership Testing """
    def check_number(self):

        number = 9999999
        for item in self.Million_numbers:
            if item  == number:
                return  True
        return False
        """
        % timeit check_number(5000)
        
        5000 in Million_numbers
        """
        Million_numbers = set (self.Million_numbers)
        print (Million_numbers)

    """    %timeit 100 in Million_numbers                # 33 times faster( vs list )
           %timeit 9999999 in Million_numbers            #2480000 times faster (vs list)
           
        Caution:
           %timeit  set(Million_numbers)          #  But conversion from list to set take longer times than any of the above
                                                         iteration
                                                     (Suggesiton : try to use set than list as much as possible )  
    """


    """task 5: Removing Duplicates"""
    def remove_duplicates(self):
        # APPROACH 5.1
        unique = []
        for element in self.Million_numbers:      # slower approach
            if element not in unique:
                unique.append(element)

        # approach 5.2
        """ Set doesn't contains duplicates but order disturbes 
        If order of elements really matter than try to use OrderDict"""
        set(self.Million_numbers)                # 400 times faster



    """ task 6: Sorting the list elements"""
    def sorting_list(self):
        # approach 6.1
        sorted(self.Million_numbers)      # slower appraoch

        # approach 6.2
        self.Million_numbers.sort()      # 6 times faster


    """task 7: 1000 operation and 1 function """
    def one_function(self):
        def square(number):                         # Slower
            return number**2
        squares  = [square(i) for i in range (1000)]

        def compute_squares():                       # 27 % faster
            return [i**2 for i in range (10000)]



    """ Task 8  Checking for true """
    def True_faster(self):
        """
        approach 1  - >   if variable ==True :
        approach 2  - >  if variable is True :
        approach 3 - >   if variable :                      # faster approach
        """
        print("if Variable : " +"is 73% faster")

    """ Task 9: Checking for false """
    def false_faster(self):
        """
        approach 1  - >   if variable == False :
        approach 2  - >  if variable is False :
        approach 3 - >   if not variable :                   # faster approach
        """
        print("if not Variable : " + "is 77% faster ")

    """ Task 10: Checking for Empty list """
    def check_empty_list(self):
        """
        approach 1  - >   if len(a_list) == 0:
        approach 2  - >  if a_list == [] :
        approach 3 - >   if not  a_list:                # faster approach
        """


    """ Task11 : Def vs Lambada """
    def def_vs_lambda(name):
        """Result: Both below approach will take work equally same amount of time """
        #approach 1
        def greet(name):
            return 'Hello {}!.format(name)'

        #approach 2
        greet =  lambda name : "Hello{}!".format(name)


    """ Task 12 : variable lookup """
    def variable_lookup(self):
        """ Note : lookup for local variable is faster than global variable or builtin """

        # approach 1:
        def squares (self):
            output  = []
            for element in self.Million_numbers:
                output.append(element*element)         # SLOWER
            return output

        # approach 2:
        def square_faster(self):
            output = []
            append  = output.append()                # 35% FASTER  by storing global ".append()" into local variable "append"
            for elements in self.Million_numbers:
                append (elements * elements)
            return output

if __name__== '__main__':
    Py_Optmize_example