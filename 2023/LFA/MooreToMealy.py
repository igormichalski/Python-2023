def moore_to_mealy():
    # Entrada de informações do usuário
    num_states = int(input("Quantidade de Estados: "))
    states = input("Estados (separados por espaço): ").split()
    alphabet = input("Alfabeto (separado por espaço): ").split()
    moore_outputs = input("Saída de cada estado (no formato 'Estado=Saída', separados por espaço): ").split()
    transitions = []
    print("Transições (digite 'fim' para encerrar):")
    while True:
        transition = input()
        if transition == 'fim':
            break
        transitions.append(tuple(transition.split(',')))
    initial_state = input("Estado Inicial: ")

    # Inicialização da máquina de Mealy
    mealy_states = states
    mealy_transitions = []
    mealy_initial_state = initial_state

    for transition in transitions:
        from_state, input_symbol, to_state = transition
        output_symbol = next(output.split('=')[1] for output in moore_outputs if output.split('=')[0] == to_state)
        mealy_transitions.append((from_state, f"{input_symbol}/{output_symbol}", to_state))

    # Saída da máquina de Mealy
    print("\nMealy Machine (convertido)")
    print(f"Quantidade de Estados = {num_states}")
    print(f"Estados = {' '.join(mealy_states)}")
    print(f"Alfabeto = {' '.join(alphabet)}")
    print("Transições:")
    for transition in mealy_transitions:
        print(f"{transition[0]},{transition[1]},{transition[2]}")  # Corrigi a formatação aqui
    print(f"Estado Inicial = {mealy_initial_state}")

#loop para aceitar mais casosa
while True:
    moore_to_mealy()
    x = int(input("Digite 0 para outra conversão!"))
    if(x):
        break
