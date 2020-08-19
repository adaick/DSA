string  = input()
def stringvalid(string) : 
    stack = [] 
    invalid=0
    for i in range(len(string)):
        if string[i]=="{" or string[i]=="(" or string[i]=="[":
            stack.append(string[i])
        elif string[i]=="}" and stack[-1]=="{":
            stack.pop()
        elif string[i]==")" and stack[-1]=="(":
            stack.pop()
        elif string[i]=="]" and stack[-1]=="[":
            stack.pop()
        elif string[i]=="}" or string[i]=="]" or string[i]==")":
            invalid=i
    
    if stack:
        print(invalid+1)
    else:
        print("Sucess")
        
output=stringvalid(string)