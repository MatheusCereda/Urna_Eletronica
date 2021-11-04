# -*- coding: utf-8 -*-
nomePres1 = 'Naruto'
nomePres2 = 'Sasuke'
nomePres3 = 'Sakura'
nomePres4 = 'Itachi'
nomePres5 = 'Kakashi'

nomeGov1 = 'Shikamaru'
nomeGov2 = 'Ino'
nomeGov3 = 'Tsunade'
nomeGov4 = 'Minato'
nomeGov5 = 'Neji'

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

op = 0
votoPresNulo = 0
votoPresBranco = 0
votoGovNulo = 0
votoGovBranco = 0

def numCand(nome, voto):
    confirmar = input(f'\n>>> Confirmar o voto no candidato {nome}? (s ou n) ')

    while (confirmar != 's') and (confirmar != 'n'):
        confirmar = input(f'\n[!] Opção Inválida\n\n>>> Confirmar o voto no candidato {nome}? (s ou n) ')
    if confirmar == 's':
        voto += 1
        print('\n[*] Voto Confirmado!')
        return voto
    else:
        confirmar == 'n'
        print('\n[!] Voto Cancelado! ')

def votoBranco(branco):
    confirmar = input('\n>>> Confirmar voto em branco? (s ou n) ')
        
    while (confirmar != 's') and (confirmar != 'n'):
        confirmar = input('\n[!] Opção Inválida\n\n>>> Confirmar voto em branco? (s ou n) ')
    if confirmar == 's':
        branco += 1
        print('\n[*] Voto em branco Confirmado!')
        return branco
    elif confirmar == 'n':
        print('\n[!] Voto Cancelado')

def anular(nulo):
    confirmar = input('\n>>> Anular voto? (s ou n) ')
        
    while (confirmar != 's') and (confirmar != 'n'):
        confirmar = input('\n[!] Opção Inválida\n\n>>> Anular voto? (s ou n) ')
    if confirmar == 's':
        nulo += 1
        print('\n[*] Voto Anulado!')
        return nulo
    elif confirmar == 'n':
        print('\n[!] Voto Cancelado')

while op != 4:
    
    print("\n\n+----------- Urna Eletrônica 3.0 -----------+\n\
        \r|                                           |\n\
        \r| [1] Listar candidatos.                    |\n\
        \r| [2] Iniciar votação.                      |\n\
        \r| [3] Apurar votos.                         |\n\
        \r| [4] Desligar a urna.                      |\n\
        \r|                                           |\n\
        \r+-------------------------------------------+\n\
        \r|\
    ")

    op = int(input('+--> Digite a sua opção: '))

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
        numCandGov = input('\n>>> Informe o número de seu candidato a governador (ou b para branco): ')

        if numCandGov == '1':
            votoGov1 = numCand(nomeGov1, votoGov1)
        elif numCandGov == '2':
            votoGov2 = numCand(nomeGov2, votoGov2)
        elif numCandGov == '3':
            votoGov3 = numCand(nomeGov3, votoGov3)
        elif numCandGov == '4':
            votoGov4 = numCand(nomeGov4, votoGov4)
        elif numCandGov == '5':
            votoGov5 = numCand(nomeGov5, votoGov5)
        elif (numCandGov == 'b') or (numCandGov == 'B'):
            votoGovBranco = votoBranco(votoGovBranco)
        else:
            votoGovNulo = anular(votoGovNulo)

        numCandPres = input('\n>>> Informe o número de seu candidato a presidente (ou b para branco): ')
    
        if numCandPres == '1':
            votoPres1 = numCand(nomePres1, votoPres1)
        elif numCandPres == '2':
            votoPres2 = numCand(nomePres2, votoPres2)
        elif numCandPres == '3':
            votoPres3 = numCand(nomePres3, votoPres3)
        elif numCandPres == '4':
            votoPres4 = numCand(nomePres4, votoPres4)
        elif numCandPres == '5':
            votoPres5 = numCand(nomePres5, votoPres5)
        elif (numCandPres == 'b') or (numCandPres == 'B'):
            votoPresBranco = votoBranco(votoPresBranco)
        else:
            votoPresNulo = anular(votoPresNulo)
    
    elif op == 3:
        print(f"\n\n\
            \r             Apuração de votos\n\
            \r\n * Candidatos a governador:\n\
            \r   Votos do(a) candidato(a) {nomeGov1}: {votoGov1}\n\
            \r   Votos do(a) candidato(a) {nomeGov2}: {votoGov2}\n\
            \r   Votos do(a) candidato(a) {nomeGov3}: {votoGov3}\n\
            \r   Votos do(a) candidato(a) {nomeGov4}: {votoGov4}\n\
            \r   Votos do(a) candidato(a) {nomeGov5}: {votoGov5}\n\
            \r   Votos em branco: {votoGovBranco}\n\
            \r   Votos nulos: {votoGovNulo}\n\
            \r\n * Candidatos a presidente:\n\
            \r   Votos do(a) candidato(a) {nomePres1}: {votoPres1}\n\
            \r   Votos do(a) candidato(a) {nomePres2}: {votoPres2}\n\
            \r   Votos do(a) candidato(a) {nomePres3}: {votoPres3}\n\
            \r   Votos do(a) candidato(a) {nomePres4}: {votoPres4}\n\
            \r   Votos do(a) candidato(a) {nomePres5}: {votoPres5}\n\
            \r   Votos em branco: {votoPresBranco}\n\
            \r   Votos nulos: {votoPresNulo}\n\
        ")

    else:
        print('\n [!] Opção Inválida!')

print('\n[*] Obrigado por utilizar a urna eletrônica!')