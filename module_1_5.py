immutable_var = 1, True, "3"
print (immutable_var)
#immutable_var [0] = "Ghost" - Кортеж неизменяем. То есть мы не можем изменить этот объект.
# print (immutable_var)
mutable_list = ["Artem", "Anastasia", "Maria"]
print (mutable_list)
mutable_list [0] = "Andrey"
print (mutable_list)
mutable_list .extend("Artem")
print (mutable_list)
mutable_list .remove("Maria")
print (mutable_list)


