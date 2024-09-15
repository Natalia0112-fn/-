immutable_var = ["1", "2", "a", "b"]
print(immutable_var)
immutable_var = 1, 2, "a", "b"
print(tuple(immutable_var))
immutable_var_1 = (1, 2, "a", "b")
print(tuple(immutable_var_1))
immutable_var_2 = tuple ([1, 2, "a", "b"])
print(immutable_var_2)

mutable_list = [1, 2, "a", "b"]
print(mutable_list[2])
mutable_list[2] = "apple"
print(mutable_list)


