#CARDAPIO

cardapio = []
proximo_id = 1

def adicionar_prato():
    global proximo_id #serve pra modificar a variavel fora do def
    print ('--- Adicionar Prato ---')
    nome = input('Nome do prato: ')
    categoria = input('Categoria(lanche, bebida, sobremesa):  ')
    preco = float(input('Preço: R$ '))

    prato = {
        'id': proximo_id,
        'nome': nome,
        'categoria': categoria,
        'preco': preco,
        'disponivel': True
    }
    cardapio.append(prato)
    proximo_id += 1
    print (f' {nome} adicionado com sucesso! ✅')

def listar_pratos():
    print (' --- Cardapio --- ')
    if len(cardapio) == 0: #Mostra quantos itens tem dentro da lista
        print ('❌Nenhum prato disponivel ainda.')
        return
    for prato in cardapio:
        if prato['disponivel'] == True:
            status = '✅'
        else:
            status = '❌'
        print(f"[{prato['id']}] {status} {prato['nome']} | {prato['categoria']} | R$ {prato['preco']:.2f}")

def remover_prato():
    listar_pratos()
    if len (cardapio) == 0:
        return
    try: #Evitar o Erro
        id_escolhido = int(input('Digite o ID do prato que deseja remover: '))
        for prato in cardapio:
            if prato ['id'] == id_escolhido:
                cardapio.remove(prato)
                print ('Prato removido com sucesso')
                return
        print ('ID nao encontrado ❌')
    except ValueError: #O que fazer depois que "trava"
        print ('Digite um numero valido.')

def menu_cardapio():
    while True:
        print ('==== Cardapio ==== ')
        print ()
        print ('1 - Listar Pratos')
        print ('2 - Adicionar Pratos')
        print ('3 - Remover Pratos')
        print ('0 - Voltar')
        print ()
        
        opcao = input('Escolha uma das opções: ')
        if opcao == "1":
            listar_pratos()
        elif opcao == "2":
            adicionar_prato()
        elif opcao == "3":
            remover_prato()
        elif opcao == "0":
            break
        else:
            print ('❌ Opção Inválida.')

if __name__ == "__main__":
    menu_cardapio()

#MESAS

mesas = []

def adicionar_mesa():
    print ('--- Adicionar uma Mesa ---')
    numero = int(input('Digite o numero da mesa: '))
    capacidade = int(input('Digite a capacidade da mesa: '))

    mesa = {
        "numero": numero,
        "capacidade": capacidade,
        "Status": "livre"
    }
    mesas.append(mesa)
    print (f'mesa numero {numero} adicionada com sucesso!✅')

def listar_mesas():
    print ('-- Status das Mesas --')
    if len(mesas) == 0:
        print ('Nenhuma mesa disponivel ainda.❌')
        return
    for mesa in mesas:
        if mesa ['Status'] == "livre":
            status = '✅'
        else:
            status = '❌'
            print(f"Mesa [{mesa['numero']}] | Capacidade: {mesa['capacidade']} | {status}")
    
def abrir_mesa():
    listar_mesas()
    if len(mesas) == 0:
        return
    try:
        num_mesa = int(input('Digite o numero da mesa: '))
        for mesa in mesas:
            if mesa['numero'] == num_mesa and mesa['Status'] == 'livre':
                mesa['Status'] = 'ocupada'
                print(f'✅ Mesa {num_mesa} aberta com sucesso!')
                return
            elif mesa['numero'] == num_mesa and mesa['Status'] == 'ocupada':
                print(f'❌ Mesa {num_mesa} já está ocupada!')
                return
        print('❌ Mesa não encontrada.')
    except ValueError:
        print('❌ Digite um número válido.')

def fechar_mesa():
    listar_mesas()
    if len(mesas) == 0:
        return
    try:
        num2_mesa = int(input('Digite o numero da mesa: '))
        for mesa in mesas:
            if mesa['numero'] == num2_mesa and mesa['Status'] == 'ocupada':
                mesa['Status'] = 'livre'
                print (f'✅ {num2_mesa} fechada com sucesso!')
                return
            elif mesa['numero'] == num2_mesa and mesa ['Status'] == 'livre':
                print(f'❌ Mesa {num2_mesa} já está livre!')
                return
        print ('❌ Mesa não encontrada. ')
    except ValueError:
        print ('Digite um numero válido. ')

def menu_mesas():
    while True:
        print ('==== Menu das Mesas ==== ')
        print ()
        print ('1 - Listar Mesas')
        print ('2 - Adicionar Mesas')
        print ('3 - Abrir Mesas')
        print ('4 - Fechar Mesas')
        print ('0 - Voltar')

        escolha = input('Escolha uma das opções: ')
        if escolha == '1':
            listar_mesas()
        elif escolha == '2':
            adicionar_mesa()
        elif escolha == '3':
            abrir_mesa()
        elif escolha == '4':
            fechar_mesa()
        elif escolha == "0":
            break
        else:
            print ('❌ Opção Inválida.')    