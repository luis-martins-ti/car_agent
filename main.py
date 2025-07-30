from car_agent.agent.mcp import MCPContext
from car_agent.agent.prompt_engine import ask_llm
from car_agent.search.filters import buscar_veiculos
from rich import print


def main():
    print("[bold cyan]Bem-vindo ao assistente de veículos![/bold cyan]")

    context = MCPContext()
    context.interactions.clear()
    while True:
        user_input = input("Você: ").strip()

        if user_input.lower() in ["sair", "exit", "quit"]:
            print("[bold red]Encerrando o assistente. Até logo![/bold red]")
            break

        context.add_interaction(user_input)
        prompt = context.build_prompt()
        filtros = ask_llm(prompt)

        if filtros:
            print(f"[green]Filtros detectados:[/green] {filtros}")
            veiculos = buscar_veiculos(filtros)

            if veiculos:
                print("\n[bold yellow]Carros encontrados:[/bold yellow]")
                for v in veiculos:
                    print(
                        f"- {v.marca} {v.modelo} ({v.ano}), {v.cor}, {v.km} km, R$ {v.preco}"
                    )
            else:
                print("[red]Nenhum carro encontrado com esses filtros.[/red]")

            while True:
                print("\n[bold]O que deseja fazer agora?[/bold]")
                print("1 - Adicionar novos filtros")
                print("2 - Fazer uma nova busca")
                print("3 - Sair")

                opcao = input("Escolha uma opção (1/2/3): ").strip()

                if opcao == "1":
                    # Mantém contexto e continua loop externo
                    break
                elif opcao == "2":
                    # Reseta o contexto para nova busca
                    context = MCPContext()
                    context.interactions.clear()
                    break
                elif opcao == "3":
                    print("[bold red]Encerrando o assistente. Até logo![/bold red]")
                    return
                else:
                    print("[red]Opção inválida. Tente novamente.[/red]")
        else:
            print(
                "[italic]Ainda não consegui identificar tudo. Pode me dar mais detalhes?[/italic]"
            )


if __name__ == "__main__":
    main()
