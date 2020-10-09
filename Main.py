from Students import Student, HighSchool, Graduation

Student = Student (1, 'Laura', 88801)
StudentHG = HighSchool (2, 'Eduardo', 88802, 2019)
StudentG = Graduation (3, 'Joana', 88803, 4)

opcao = "" 
while( opcao != "0" ):
    print("\n----------------------")
    print("1 - Student")
    print("2 - Student High School")
    print("3 - Student Graduation")
    print("0 - Sair")
    print("\n----------------------")

    opcao = input("Digite uma opção: ")

    if opcao == "1":
        Student.printStudent()
        print ('-'*20)
        break

    if opcao == "2":
        StudentHG.printHighSchool()
        print ('-'*20)
        break

    if opcao == "3":
        StudentG.printGraduation()
        print ('-'*20)
        break
