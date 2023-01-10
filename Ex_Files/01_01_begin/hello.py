NAME = "Lorenza"
MIDNAME = "Monserrat"
SURNAME = "Perez"
GREET = "Hola, "
FULL_GREET = GREET + NAME #concatenate strings using + sign
INTRUPUTION = f"Bienvenida, {NAME} " #string interpolation
Greet_format = "Me llamo {} {} {}"
FORMATTED = Greet_format.format(NAME, MIDNAME,SURNAME) #Tempalete for formatting 
print(FULL_GREET)
print(INTRUPUTION, FORMATTED) #Printing two strings in same line
#print(FORMATTED)
print(FORMATTED.upper()) #utilities
print(FORMATTED.replace(NAME,"Pancho")) #utilities

