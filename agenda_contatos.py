"""Agenda de Contatos - aplicação de terminal em Python.

Funcionalidades:
1. Menu com lista de opções; o usuário digita uma escolha
2. Adicionar contato (Nome, Telefone, Email, Favorito)
3. Visualizar lista de contatos cadastrados
4. Editar contato existente
5. Marcar/desmarcar contato como favorito
6. Visualizar lista de contatos favoritos
7. Apagar contato
"""

contatos = []


def mostrar_menu():
    print("\n===== AGENDA DE CONTATOS =====")
    print("1 - Adicionar contato")
    print("2 - Ver todos os contatos")
    print("3 - Editar contato")
    print("4 - Marcar/desmarcar favorito")
    print("5 - Ver contatos favoritos")
    print("6 - Apagar contato")
    print("0 - Sair")


def formatar_contato(indice, contato):
    estrela = "★" if contato["favorito"] else "☆"
    return (
        f"{indice}. {estrela} {contato['nome']} | "
        f"Tel: {contato['telefone']} | Email: {contato['email']}"
    )


def listar_contatos(lista, titulo):
    print(f"\n--- {titulo} ---")
    if not lista:
        print("Nenhum contato encontrado.")
        return
    for i, contato in enumerate(lista, start=1):
        print(formatar_contato(i, contato))


def escolher_contato(acao):
    """Mostra os contatos e retorna o contato escolhido (ou None)."""
    if not contatos:
        print("Nenhum contato cadastrado.")
        return None

    listar_contatos(contatos, "CONTATOS")
    escolha = input(f"\nNúmero do contato que deseja {acao}: ").strip()

    if not escolha.isdigit() or not (1 <= int(escolha) <= len(contatos)):
        print("Número inválido.")
        return None
    return contatos[int(escolha) - 1]


def adicionar_contato():
    print("\n--- NOVO CONTATO ---")
    nome = input("Nome: ").strip()
    if not nome:
        print("O nome é obrigatório.")
        return
    telefone = input("Telefone: ").strip()
    email = input("Email: ").strip()
    favorito = input("Favorito? (s/n): ").strip().lower() == "s"

    contatos.append(
        {"nome": nome, "telefone": telefone, "email": email, "favorito": favorito}
    )
    print(f"Contato '{nome}' adicionado com sucesso!")


def editar_contato():
    contato = escolher_contato("editar")
    if contato is None:
        return

    print("\nDeixe em branco para manter o valor atual.")
    nome = input(f"Nome [{contato['nome']}]: ").strip()
    telefone = input(f"Telefone [{contato['telefone']}]: ").strip()
    email = input(f"Email [{contato['email']}]: ").strip()

    if nome:
        contato["nome"] = nome
    if telefone:
        contato["telefone"] = telefone
    if email:
        contato["email"] = email
    print("Contato atualizado com sucesso!")


def alternar_favorito():
    contato = escolher_contato("marcar/desmarcar como favorito")
    if contato is None:
        return

    contato["favorito"] = not contato["favorito"]
    if contato["favorito"]:
        print(f"'{contato['nome']}' agora é favorito!")
    else:
        print(f"'{contato['nome']}' não é mais favorito.")


def listar_favoritos():
    favoritos = [c for c in contatos if c["favorito"]]
    listar_contatos(favoritos, "CONTATOS FAVORITOS")


def apagar_contato():
    contato = escolher_contato("apagar")
    if contato is None:
        return

    confirmar = input(f"Apagar '{contato['nome']}'? (s/n): ").strip().lower()
    if confirmar == "s":
        contatos.remove(contato)
        print("Contato apagado com sucesso!")
    else:
        print("Operação cancelada.")


def main():
    acoes = {
        "1": adicionar_contato,
        "2": lambda: listar_contatos(contatos, "TODOS OS CONTATOS"),
        "3": editar_contato,
        "4": alternar_favorito,
        "5": listar_favoritos,
        "6": apagar_contato,
    }

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "0":
            print("Até logo!")
            break
        acao = acoes.get(opcao)
        if acao:
            acao()
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
