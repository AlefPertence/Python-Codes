
nome = input("Nome: ");
tamanhoNome = len(nome);
salario = input("Salario: ");
sexo = input("sexo m ou f: ").lower();

idade = int(input("idade: "))
estado_civil = input("Estado civil: \n s = solteiro; \n c = casado; \n v = viuvo; \n d = divorciado.")

while tamanhoNome <=3:
    print("Nome invalido. Por favor, digitar um nome com mais de 3 caracteres: \n");
    nome = input("Nome: ")
    tamanhoNome = len(nome);
   

while salario == 0:
    print("salario deve ser maior que zero.");
    salario = input("\n salario: ");

while sexo != "m" and sexo != "f":
    print("Sexo invalido! Tente novamente. ");
    sexo = input("Sexo: ").lower();
    

while idade <= 0 or idade > 150:
    print("Idade invalida! Tente novamente. ");
    idade = int(input("idade: "))

while estado_civil != "c" and estado_civil != "c" and estado_civil != "v" and estado_civil != "s":
    print("selecione uma opcao valida. \n Estado civil: \n s = solteiro; \n c = casado; \n v = viavo; \n d = divorciado.")
    estado_civil = input("Estado civil: ")
