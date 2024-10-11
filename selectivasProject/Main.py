#condicion de estructura simple

a = 3
b= 200
if b > a:
    print(b, " es mayor que ",a)


# Condicion de estructura doble
a = 200
b = 333
if a > b:
    print(a, "es mayor que ",b )
else:
    print(a, "no es mayor que",b)

# Condicion de estructura multiple
a = 200
b = 207
if a > b:
    print(a,"es mayor que",b)
elif a < b:
    print(a,"es mayor que ",b)
else:
    print(a,"es igual que ",b)

# Condicion enlazadas
x = 28
if x > 10:
    print("por encima de diez,")
    if x > 20:
        print("y tambien por encima de 20!")
    else:
        print("pero no por encima de 20.")

# parametros end y sep
print("estudiar los sabados",end=' ') # con and pasa o hace el salto de linea dandole continuidad
print("es genial")

#parametro sep
print("Daniela","Luis","Carlos","Camila")# Agrega un espacio por defecto
print("Daniela","Luis","Carlos","Camila",sep="")# Quita el espacio
print("Daniela","Luis","Carlos","Camila",sep=",")#Agrega una coma

print("Daniela","Luis","Carlos","Camila", sep = "_",end="_curso-python")# Implementacion end y sep

