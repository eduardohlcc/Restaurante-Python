from funcoes import menu_cardapio, menu_mesas

def main():
    while True:
        print("""
============================
  SISTEMA DE RESTAURANTE
============================

1 - Cardápio
2 - Mesas
0 - Sair
              """)
        opcao = input('Escolha: ')
        if opcao == '1':
            menu_cardapio()
        elif opcao == '2':
            menu_mesas()
        elif opcao == '0':
            print('Até logo! 👋')
            break
        else:
            print('❌ Opção inválida.')

if __name__ == '__main__':
    main()