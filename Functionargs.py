# Function definition is here
def printmer( str ):
 "This prints a passed string into this function"
 print(str)
 return;
# Now you can call printme function
#printmer("apple");

def printinfo( name, age ):
 "This prints a passed info into this function"
 print ("Name: ", name)
 print ("Age ", age)
 return;
# Now you can call printinfo function
#printinfo( age=50, name="miki" );

def printinfod( name, age = 35 ):
 "This prints a passed info into this function"
 print ("Name: ", name)
 print ("Age ", age)
 return;
# Now you can call printinfo function
printinfod( age=50, name="miki" );
printinfod( name="miki" );


def printinfov( arg1, *vartuple ):
 "This prints a variable passed arguments"
 print ("Output is: ")
 print (arg1)
 print (vartuple)
 for var in vartuple:
    print(var)
 return
# Now you can call printinfo function
#printinfov( 10 );
printinfov( 70, 60, 50 );
