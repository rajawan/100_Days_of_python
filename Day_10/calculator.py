#Add
def add(n1,n2):
   return n1+n2 

#subtract
def subtract(n1,n2):
    return n1-n2

#multiply
def multiply(n1,n2):
    return n1*n2

#division
def division(n1,n2):
    return n1/n2

operation={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":division
}
def calculator():
    num1=float(input("Enter First number: "))
    for symbol in operation:
        print(symbol)
    finished=False
    while not finished:
        sign=input("Type Which operation you want from the above list: ")
        num2=float(input("Enter Seocend number: "))
        claculation_function=operation[sign]
        answer=claculation_function(num1,num2)
        print(f"{num1} {sign} {num2} = {answer}")
        if input("Type 'y' if you want to continue with this answer or type 'n' to start from first : ") == 'y':
            num1=answer
        else:
            finished=True
            calculator()
calculator()           
