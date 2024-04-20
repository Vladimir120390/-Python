immutable_var_ = 1, 2 , "str", "int"
print(immutable_var_)
immutable_var_ [0] = 100
print(immutable_var_)# кортеж не поддерживает назначение элементов
mutable_list = ['1', '2' , "str", "int"]
mutable_list [0] = 100
print(mutable_list)
