from functools import singledispatch

@singledispatch
def append_one(obj):
    print("I will be called if not matched from other definitions")

# for type list
@append_one.register(list)
def _(obj):
    return obj + [1]

# for type set
@append_one.register(set)
def _(obj):
    return obj.union({1})

# for type set
@append_one.register(str)
def _(obj):
    return obj + "1"

print('append_one([1,2,3]): ', append_one([1,2,3]))
print('append_one({2,3,4}): ', append_one({2,3,4}))
print('append_one("234"): ', append_one("234"))