ecuacion = "5z+6x-3y=8"
guion = "-"
newstring = ''.join([i for i in ecuacion if i.isalpha()])
var_string = guion.join(newstring)
variables_array = var_string.split("-")

print(variables_array)