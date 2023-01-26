def bisiesto():
  año: int = int(input("Escribe el año que quieras comprobar: "))

  if(año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)):
      print("El año es bisiesto")
  else:
      print("El año no es bisiesto")

resultado = bisiesto()
print(resultado)


