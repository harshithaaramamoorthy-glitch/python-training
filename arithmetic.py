def calc(oper,*args):
    result=0
    if oper == "add":
        result=sum(args)
    elif oper == "sub":
        for num in args[1:]:
            result-=num
    elif oper == "mul":
        result=1
        for num in args[1:]:
            result*=num
    elif oper == "div":
        for num in args[1:]:
            if num !=0:
                result /= num
    return result
print("addition:",(calc("add",10,20,30)))
print("subtraction:",(calc("sub",100,40,50)))
print("multiplication:",(calc("mul",2,3,4)))
print("division:",(calc("div",100,2,3)))
    
        