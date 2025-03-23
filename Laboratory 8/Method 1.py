#Tui Form
def main():
    #Find the largest number among three numbers
    L =[]
    num1 = eval(input("Enter the first number: "))
    L.append(num1)
    num2 = eval(input("Enter the second number: "))
    L.append(num2)
    num3 = eval(input("Enter the Third number: "))
    L.append(num3)
    print("The largest among the three is: ", str(max(L)))
main()