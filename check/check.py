# testing that we can import a local build

import slowda

a = slowda.MyStruct(x=1, y=2)
b = slowda.MyStruct(x=3, y=4)

result = slowda.add_structs(a, b)
print("result", result)
