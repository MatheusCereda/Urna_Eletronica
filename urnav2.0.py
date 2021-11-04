# -*- coding: utf-8 -*-
nomePres1 = "PRESIDENTE-1"
nomePres2 = "PRESIDENTE-2"
nomePres3 = "PRESIDENTE-3"
nomePres4 = "PRESIDENTE-4"
nomePres5 = "PRESIDENTE-5"

nomeGov1 = "GOVERNADOR-1"
nomeGov2 = "GOVERNADOR-2"
nomeGov3 = "GOVERNADOR-3"
nomeGov4 = "GOVERNADOR-4"
nomeGov5 = "GOVERNADOR-5"

votoPres1 = 0
votoPres2 = 0
votoPres3 = 0
votoPres4 = 0
votoPres5 = 0

votoGov1 = 0
votoGov2 = 0
votoGov3 = 0
votoGov4 = 0
votoGov5 = 0

votoPresNulo = 0
votoPresBranco = 0
votoGovNulo = 0
votoGovBranco = 0

print("\n\n+----------- Urna Eletrônica 2.0 -----------+\n\
    \r|                                           |\n\
    \r| [1] Listar candidatos.                    |\n\
    \r| [2] Iniciar votação.                      |\n\
    \r| [3] Apurar votos.                         |\n\
    \r| [4] Desligar a urna.                      |\n\
    \r|                                           |\n\
    \r+-------------------------------------------+\n\
    \r|\
")

op = int(input("+--> Digite a sua opção: "))

while 0 < op <= 4:
    if op == 1:
        print(f"\n\n\
            \r * Lista de candidatos a governador:\n\
            \r   Candidato(a) 1: {nomeGov1}\n\
            \r   Candidato(a) 2: {nomeGov2}\n\
            \r   Candidato(a) 3: {nomeGov3}\n\
            \r   Candidato(a) 4: {nomeGov4}\n\
            \r   Candidato(a) 5: {nomeGov5}\n\
            \n\
            \r * Lista de candidatos à presidência:\n\
            \r   Candidato(a) 1: {nomePres1}\n\
            \r   Candidato(a) 2: {nomePres2}\n\
            \r   Candidato(a) 3: {nomePres3}\n\
            \r   Candidato(a) 4: {nomePres4}\n\
            \r   Candidato(a) 5: {nomePres5}\n\
        ")

    elif op == 2:
        numCandGov = int(input('\n>>> Informe o número de seu candidato a governador: '))
        
        while True:
            if numCandGov == 1:
                print(f"\n\
                    \r Nome: {nomeGov1}\n\
                    \r+-----------------------+\n\
                    \r|                       |\n\
                    \r| [1] Confirmar voto.   |\n\
                    \r| [2] Votar em branco.  |\n\
                    \r| [3] Anular voto.      |\n\
                    \r|                       |\n\
                    \r+-----------------------+\n\
                    \r|\
                ")

                op = int(input("+--> Digite a sua opção: "))

                while True:
                    if 1 <= op <= 3:
                        if op == 1:
                            votoGov1 += 1
                            print('\n[*] Voto confirmado!')
                            break

                        elif op == 2:
                            votoGovBranco += 1
                            print('\n[*] Voto em branco confirmado!')
                            break
                        
                        elif op == 3:
                            votoGovNulo += 1
                            print("\n[*] Voto anulado!")
                            break

                    else:
                        anular = input("\n>>> Deseja anular o voto? (s ou n): ")
                        if anular == 's':
                            votoGovNulo += 1
                            print("\n[*] Voto anulado!")
                            break

                        elif anular == 'n':
                            print(f"\n\
                                \r Nome: {nomeGov1}\n\
                                \r+-----------------------+\n\
                                \r|                       |\n\
                                \r| [1] Confirmar voto.   |\n\
                                \r| [2] Votar em branco.  |\n\
                                \r| [3] Anular voto.      |\n\
                                \r|                       |\n\
                                \r+-----------------------+\n\
                                \r|\
                            ")
                            
                            op = int(input("+--> Digite a sua opção: "))

                        else:
                            print("\n[!] Opção inválida.")

                break

            elif numCandGov == 2:
                print(f"\n\
                    \r Nome: {nomeGov2}\n\
                    \r+-----------------------+\n\
                    \r|                       |\n\
                    \r| [1] Confirmar voto.   |\n\
                    \r| [2] Votar em branco.  |\n\
                    \r| [3] Anular voto.      |\n\
                    \r|                       |\n\
                    \r+-----------------------+\n\
                    \r|\
                ")

                op = int(input("+--> Digite a sua opção: "))

                while True:
                    if 1 <= op <= 3:
                        if op == 1:
                            votoGov2 += 1
                            print('\n[*] Voto confirmado!')
                            break

                        elif op == 2:
                            votoGovBranco += 1
                            print('\n[*] Voto em branco confirmado!')
                            break
                        
                        elif op == 3:
                            votoGovNulo += 1
                            print("\n[*] Voto anulado!")
                            break

                    else:
                        anular = input("\n>>> Deseja anular o voto? (s ou n): ")
                        if anular == 's':
                            votoGovNulo += 1
                            print("\n[*] Voto anulado!")
                            break

                        elif anular == 'n':
                            print(f"\n\
                                \r Nome: {nomeGov2}\n\
                                \r+-----------------------+\n\
                                \r|                       |\n\
                                \r| [1] Confirmar voto.   |\n\
                                \r| [2] Votar em branco.  |\n\
                                \r| [3] Anular voto.      |\n\
                                \r|                       |\n\
                                \r+-----------------------+\n\
                                \r|\
                            ")
                            
                            op = int(input("+--> Digite a sua opção: "))

                        else:
                            print("\n[!] Opção inválida.")

                break

            elif numCandGov == 3:
                print(f"\n\
                    \r Nome: {nomeGov3}\n\
                    \r+-----------------------+\n\
                    \r|                       |\n\
                    \r| [1] Confirmar voto.   |\n\
                    \r| [2] Votar em branco.  |\n\
                    \r| [3] Anular voto.      |\n\
                    \r|                       |\n\
                    \r+-----------------------+\n\
                    \r|\
                ")

                op = int(input("+--> Digite a sua opção: "))

                while True:
                    if 1 <= op <= 3:
                        if op == 1:
                            votoGov3 += 1
                            print('\n[*] Voto confirmado!')
                            break

                        elif op == 2:
                            votoGovBranco += 1
                            print('\n[*] Voto em branco confirmado!')
                            break
                        
                        elif op == 3:
                            votoGovNulo += 1
                            print("\n[*] Voto anulado!")
                            break

                    else:
                        anular = input("\n>>> Deseja anular o voto? (s ou n): ")
                        if anular == 's':
                            votoGovNulo += 1
                            print("\n[*] Voto anulado!")
                            break

                        elif anular == 'n':
                            print(f"\n\
                                \r Nome: {nomeGov3}\n\
                                \r+-----------------------+\n\
                                \r|                       |\n\
                                \r| [1] Confirmar voto.   |\n\
                                \r| [2] Votar em branco.  |\n\
                                \r| [3] Anular voto.      |\n\
                                \r|                       |\n\
                                \r+-----------------------+\n\
                                \r|\
                            ")
                            
                            op = int(input("+--> Digite a sua opção: "))

                        else:
                            print("\n[!] Opção inválida.")

                break

            elif numCandGov == 4:
                print(f"\n\
                    \r Nome: {nomeGov4}\n\
                    \r+-----------------------+\n\
                    \r|                       |\n\
                    \r| [1] Confirmar voto.   |\n\
                    \r| [2] Votar em branco.  |\n\
                    \r| [3] Anular voto.      |\n\
                    \r|                       |\n\
                    \r+-----------------------+\n\
                    \r|\
                ")

                op = int(input("+--> Digite a sua opção: "))

                while True:
                    if 1 <= op <= 3:
                        if op == 1:
                            votoGov4 += 1
                            print('\n[*] Voto confirmado!')
                            break

                        elif op == 2:
                            votoGovBranco += 1
                            print('\n[*] Voto em branco confirmado!')
                            break
                        
                        elif op == 3:
                            votoGovNulo += 1
                            print("\n[*] Voto anulado!")
                            break

                    else:
                        anular = input("\n>>> Deseja anular o voto? (s ou n): ")
                        if anular == 's':
                            votoGovNulo += 1
                            print("\n[*] Voto anulado!")
                            break

                        elif anular == 'n':
                            print(f"\n\
                                \r Nome: {nomeGov4}\n\
                                \r+-----------------------+\n\
                                \r|                       |\n\
                                \r| [1] Confirmar voto.   |\n\
                                \r| [2] Votar em branco.  |\n\
                                \r| [3] Anular voto.      |\n\
                                \r|                       |\n\
                                \r+-----------------------+\n\
                                \r|\
                            ")

                            op = int(input("+--> Digite a sua opção: "))

                        else:
                            print("\n[!] Opção inválida.")

                break

            elif numCandGov == 5:
                print(f"\n\
                    \r Nome: {nomeGov5}\n\
                    \r+-----------------------+\n\
                    \r|                       |\n\
                    \r| [1] Confirmar voto.   |\n\
                    \r| [2] Votar em branco.  |\n\
                    \r| [3] Anular voto.      |\n\
                    \r|                       |\n\
                    \r+-----------------------+\n\
                    \r|\
                ")

                op = int(input("+--> Digite a sua opção: "))

                while True:
                    if 1 <= op <= 3:
                        if op == 1:
                            votoGov5 += 1
                            print('\n[*] Voto confirmado!')
                            break

                        elif op == 2:
                            votoGovBranco += 1
                            print('\n[*] Voto em branco confirmado!')
                            break
                        
                        elif op == 3:
                            votoGovNulo += 1
                            print("\n[*] Voto anulado!")
                            break

                    else:
                        anular = input("\n>>> Deseja anular o voto? (s ou n): ")
                        if anular == 's':
                            votoGovNulo += 1
                            print("\n[*] Voto anulado!")
                            break

                        elif anular == 'n':
                            print(f"\n\
                                \r Nome: {nomeGov5}\n\
                                \r+-----------------------+\n\
                                \r|                       |\n\
                                \r| [1] Confirmar voto.   |\n\
                                \r| [2] Votar em branco.  |\n\
                                \r| [3] Anular voto.      |\n\
                                \r|                       |\n\
                                \r+-----------------------+\n\
                                \r|\
                            ")
                            
                            op = int(input("+--> Digite a sua opção: "))

                        else:
                            print("\n[!] Opção inválida.")

                break
            
            else:
                print('\n[!] Opção Inválida.')

                numCandGov = int(input('\n>>> Informe o número de seu candidato a governador: '))

        numCandPres = int(input('\n>>> Informe o número de seu candidato a presidente: '))

        while True:
            if numCandPres == 1:
                print(f"\n\
                    \r Nome: {nomePres1}\n\
                    \r+-----------------------+\n\
                    \r|                       |\n\
                    \r| [1] Confirmar voto.   |\n\
                    \r| [2] Votar em branco.  |\n\
                    \r| [3] Anular voto.      |\n\
                    \r|                       |\n\
                    \r+-----------------------+\n\
                    \r|\
                ")

                op = int(input("+--> Digite a sua opção: "))

                while True:
                    if 1 <= op <= 3:
                        if op == 1:
                            votoPres1 += 1
                            print('\n[*] Voto confirmado!')
                            break

                        elif op == 2:
                            votoPresBranco += 1
                            print('\n[*] Voto em branco confirmado!')
                            break
                        
                        elif op == 3:
                            votoPresNulo += 1
                            print("\n[*] Voto anulado!")
                            break

                    else:
                        anular = input("\n>>> Deseja anular o voto? (s ou n): ")
                        if anular == 's':
                            votoPresNulo += 1
                            print("\n[*] Voto anulado!")
                            break

                        elif anular == 'n':
                            print(f"\n\
                                \r Nome: {nomePres1}\n\
                                \r+-----------------------+\n\
                                \r|                       |\n\
                                \r| [1] Confirmar voto.   |\n\
                                \r| [2] Votar em branco.  |\n\
                                \r| [3] Anular voto.      |\n\
                                \r|                       |\n\
                                \r+-----------------------+\n\
                                \r|\
                            ")
                            
                            op = int(input("+--> Digite a sua opção: "))

                        else:
                            print("\n[!] Opção inválida.")

                break

            elif numCandPres == 2:
                print(f"\n\
                    \r Nome: {nomePres2}\n\
                    \r+-----------------------+\n\
                    \r|                       |\n\
                    \r| [1] Confirmar voto.   |\n\
                    \r| [2] Votar em branco.  |\n\
                    \r| [3] Anular voto.      |\n\
                    \r|                       |\n\
                    \r+-----------------------+\n\
                    \r|\
                ")

                op = int(input("+--> Digite a sua opção: "))

                while True:
                    if 1 <= op <= 3:
                        if op == 1:
                            votoPres2 += 1
                            print('\n[*] Voto confirmado!')
                            break

                        elif op == 2:
                            votoPresBranco += 1
                            print('\n[*] Voto em branco confirmado!')
                            break
                        
                        elif op == 3:
                            votoPresNulo += 1
                            print("\n[*] Voto anulado!")
                            break

                    else:
                        anular = input("\n>>> Deseja anular o voto? (s ou n): ")
                        if anular == 's':
                            votoPresNulo += 1
                            print("\n[*] Voto anulado!")
                            break

                        elif anular == 'n':
                            print(f"\n\
                                \r Nome: {nomePres2}\n\
                                \r+-----------------------+\n\
                                \r|                       |\n\
                                \r| [1] Confirmar voto.   |\n\
                                \r| [2] Votar em branco.  |\n\
                                \r| [3] Anular voto.      |\n\
                                \r|                       |\n\
                                \r+-----------------------+\n\
                                \r|\
                            ")
                            
                            op = int(input("+--> Digite a sua opção: "))

                        else:
                            print("\n[!] Opção inválida.")

                break

            elif numCandPres == 3:
                print(f"\n\
                    \r Nome: {nomePres3}\n\
                    \r+-----------------------+\n\
                    \r|                       |\n\
                    \r| [1] Confirmar voto.   |\n\
                    \r| [2] Votar em branco.  |\n\
                    \r| [3] Anular voto.      |\n\
                    \r|                       |\n\
                    \r+-----------------------+\n\
                    \r|\
                ")

                op = int(input("+--> Digite a sua opção: "))

                while True:
                    if 1 <= op <= 3:
                        if op == 1:
                            votoPres3 += 1
                            print('\n[*] Voto confirmado!')
                            break

                        elif op == 2:
                            votoPresBranco += 1
                            print('\n[*] Voto em branco confirmado!')
                            break
                        
                        elif op == 3:
                            votoPresNulo += 1
                            print("\n[*] Voto anulado!")
                            break

                    else:
                        anular = input("\n>>> Deseja anular o voto? (s ou n): ")
                        if anular == 's':
                            votoPresNulo += 1
                            print("\n[*] Voto anulado!")
                            break

                        elif anular == 'n':
                            print(f"\n\
                                \r Nome: {nomePres3}\n\
                                \r+-----------------------+\n\
                                \r|                       |\n\
                                \r| [1] Confirmar voto.   |\n\
                                \r| [2] Votar em branco.  |\n\
                                \r| [3] Anular voto.      |\n\
                                \r|                       |\n\
                                \r+-----------------------+\n\
                                \r|\
                            ")
                            
                            op = int(input("+--> Digite a sua opção: "))

                        else:
                            print("\n[!] Opção inválida.")

                break

            elif numCandPres == 4:
                print(f"\n\
                    \r Nome: {nomePres4}\n\
                    \r+-----------------------+\n\
                    \r|                       |\n\
                    \r| [1] Confirmar voto.   |\n\
                    \r| [2] Votar em branco.  |\n\
                    \r| [3] Anular voto.      |\n\
                    \r|                       |\n\
                    \r+-----------------------+\n\
                    \r|\
                ")

                op = int(input("+--> Digite a sua opção: "))

                while True:
                    if 1 <= op <= 3:
                        if op == 1:
                            votoPres4 += 1
                            print('\n[*] Voto confirmado!')
                            break

                        elif op == 2:
                            votoPresBranco += 1
                            print('\n[*] Voto em branco confirmado!')
                            break
                        
                        elif op == 3:
                            votoPresNulo += 1
                            print("\n[*] Voto anulado!")
                            break

                    else:
                        anular = input("\n>>> Deseja anular o voto? (s ou n): ")
                        if anular == 's':
                            votoPresNulo += 1
                            print("\n[*] Voto anulado!")
                            break

                        elif anular == 'n':
                            print(f"\n\
                                \r Nome: {nomePres4}\n\
                                \r+-----------------------+\n\
                                \r|                       |\n\
                                \r| [1] Confirmar voto.   |\n\
                                \r| [2] Votar em branco.  |\n\
                                \r| [3] Anular voto.      |\n\
                                \r|                       |\n\
                                \r+-----------------------+\n\
                                \r|\
                            ")
                            
                            op = int(input("+--> Digite a sua opção: "))

                        else:
                            print("\n[!] Opção inválida.")

                break

            elif numCandPres == 5:
                print(f"\n\
                    \r Nome: {nomePres5}\n\
                    \r+-----------------------+\n\
                    \r|                       |\n\
                    \r| [1] Confirmar voto.   |\n\
                    \r| [2] Votar em branco.  |\n\
                    \r| [3] Anular voto.      |\n\
                    \r|                       |\n\
                    \r+-----------------------+\n\
                    \r|\
                ")

                op = int(input("+--> Digite a sua opção: "))

                while True:
                    if 1 <= op <= 3:
                        if op == 1:
                            votoPres5 += 1
                            print('\n[*] Voto confirmado!')
                            break

                        elif op == 2:
                            votoPresBranco += 1
                            print('\n[*] Voto em branco confirmado!')
                            break
                        
                        elif op == 3:
                            votoPresNulo += 1
                            print("\n[*] Voto anulado!")
                            break

                    else:
                        anular = input("\n>>> Deseja anular o voto? (s ou n): ")
                        if anular == 's':
                            votoPresNulo += 1
                            print("\n[*] Voto anulado!")
                            break

                        elif anular == 'n':
                            print(f"\n\
                                \r Nome: {nomePres5}\n\
                                \r+-----------------------+\n\
                                \r|                       |\n\
                                \r| [1] Confirmar voto.   |\n\
                                \r| [2] Votar em branco.  |\n\
                                \r| [3] Anular voto.      |\n\
                                \r|                       |\n\
                                \r+-----------------------+\n\
                                \r|\
                            ")
                            
                            op = int(input("+--> Digite a sua opção: "))

                        else:
                            print("\n[!] Opção inválida.")

                break
            
            else:
                print('\n[!] Opção Inválida.')

                numCandPres = int(input('\n>>> Informe o número de seu candidato a presidente: '))

    
    elif op == 3:
        print(f"\n\n\
            \r             Apuração de votos\n\
            \r\n * Candidatos a governador:\n\
            \r   Votos do(a) candidato(a) {nomeGov1}:  {votoGov1}\n\
            \r   Votos do(a) candidato(a) {nomeGov2}:  {votoGov2}\n\
            \r   Votos do(a) candidato(a) {nomeGov3}:  {votoGov3}\n\
            \r   Votos do(a) candidato(a) {nomeGov4}:  {votoGov4}\n\
            \r   Votos do(a) candidato(a) {nomeGov5}:  {votoGov5}\n\
            \r   Votos em branco: {votoGovBranco}\n\
            \r   Votos nulos: {votoGovNulo}\n\
            \r\n * Candidatos a presidente:\n\
            \r   Votos do(a) candidato(a) {nomePres1}:  {votoPres1}\n\
            \r   Votos do(a) candidato(a) {nomePres2}:  {votoPres2}\n\
            \r   Votos do(a) candidato(a) {nomePres3}:  {votoPres3}\n\
            \r   Votos do(a) candidato(a) {nomePres4}:  {votoPres4}\n\
            \r   Votos do(a) candidato(a) {nomePres5}:  {votoPres5}\n\
            \r   Votos em branco: {votoPresBranco}\n\
            \r   Votos nulos: {votoPresNulo}\n\
        ")

    elif op == 4:
        print('\n[*] Obrigado por utilizar a urna eletrônica!')
        exit()

    print("\n\n+----------- Urna Eletrônica 2.0 -----------+\n\
        \r|                                           |\n\
        \r| [1] Listar candidatos.                    |\n\
        \r| [2] Iniciar votação.                      |\n\
        \r| [3] Apurar votos.                         |\n\
        \r| [4] Desligar a urna.                      |\n\
        \r|                                           |\n\
        \r+-------------------------------------------+\n\
        \r|\
    ")

    op = int(input("+--> Digite a sua opção: "))

else:
    print("\n[!] Opção inválida.")
    print('[*] Obrigado por utilizar a urna eletrônica!')