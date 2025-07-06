class multipleFunctions():
        def Subfields():
            print("Sub-fields in AI are:")
            my_list=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
            for i in my_list:
                print(i)
        def OddEven():
            num=int(input("Enter a number:"))
            if ((num%2)==0):
                print(num,"is Even number")
            else:
                print(num,"is Odd number")
        def Eligible():
            gender=input("Your gender:")
            age=int(input("Your age:"))
            if gender == "Male":
                if age >= 21:
                    print("Eligible")
                else:
                    print("Not Eligible")
            else:
                if age >= 18:
                    print("Eligible")
                else:
                    print("Not Eligible")
        def percentage():
            Subject1=int(input("Subject1="))
            Subject2=int(input("Subject2="))
            Subject3=int(input("Subject3="))
            Subject4=int(input("Subject4="))
            Subject5=int(input("Subject5="))
            Total=(Subject1+Subject2+Subject3+Subject4+Subject5)
            print("Total:",Total)
            percentage=(Total/500)*100
            print("Percentage:",percentage)
        def triangle():
            Height = float(input("Height:"))
            Breadth = float(input("Breadth:"))
            print("Area formula: (Height*Breadth)/2")
            Area = (Height*Breadth)/2
            print("Area of Triangle:",Area)
            Height1 = float(input("Height1:"))
            Height2 = float(input("Height2:"))
            Breadth = float(input("Breadth:"))
            print("Perimeter formula: Height1+Height2+Breadth")
            Perimeter = (Height1+Height2+Breadth)
            print("Perimeter of Triangle:",Perimeter)

 