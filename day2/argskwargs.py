def myfunc(arg1,*args,**kwargs):
    print("-- Hi !",arg1)
    print("--My name is ",arg1)
    for arg in args:
        print(arg)
    print("-" * 40)
    for kwa in kwargs:
        print(kwa, ":",kwargs[kwa])
myfunc("People")
myfunc("aishu",work="cts",role="dev")