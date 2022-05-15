#global scope

global_var=1
def global_scope():
    global_var=2
    print(global_var)
global_scope()
print(global_var)

#local scope
def local_scope():
    local_var=3
    print(local_var)
local_scope()
#local variable cannot access outside a function
#print(local_var)