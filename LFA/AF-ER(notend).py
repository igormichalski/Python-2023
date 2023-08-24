def epsilon_closure(states, transitions):
    closure = set(states)
    stack = list(states)

    while stack:
        state = stack.pop()

        if state in transitions and '' in transitions[state]:
            new_states = transitions[state]['']

            for new_state in new_states:
                if new_state not in closure:
                    closure.add(new_state)
                    stack.append(new_state)

    return closure


def move(states, symbol, transitions):
    new_states = set()

    for state in states:
        if state in transitions and symbol in transitions[state]:
            new_states.update(transitions[state][symbol])

    return new_states

def is_afd(states, alphabet, transitions):
    for state in states:
        for symbol in alphabet:
            if state not in transitions or symbol not in transitions[state]:
                return False
    return True

def is_afn_with_epsilon(transitions):
    for state, symbols in transitions.items():
        if '' in symbols and symbols['']:
            return True
    return False


def enfa_to_dfa(enfa_states, alphabet, enfa_transitions, enfa_initial, enfa_final):
        dfa_states = []
        dfa_transitions = {}
        dfa_initial = epsilon_closure({enfa_initial}, enfa_transitions)
        dfa_final = set()

        unmarked_states = [dfa_initial]
        dfa_states.append(dfa_initial)

        while unmarked_states:
            current_states = unmarked_states.pop(0)

            for symbol in alphabet:
                next_states = set()

                for state in current_states:
                    if state in enfa_transitions and symbol in enfa_transitions[state]:
                        next_states.update(enfa_transitions[state][symbol])

                epsilon_states = epsilon_closure(next_states, enfa_transitions)

                if epsilon_states not in dfa_states:
                    dfa_states.append(epsilon_states)
                    unmarked_states.append(epsilon_states)

                dfa_transitions.setdefault(tuple(current_states), {})
                dfa_transitions[tuple(current_states)][symbol] = tuple(epsilon_states)

            dfa_final_states = set()
            for final_state in enfa_final:
                if final_state in current_states:
                    dfa_final_states.add(tuple(current_states))

            if dfa_final_states:
                dfa_final.update(dfa_final_states)

        return dfa_states, alphabet, dfa_transitions, tuple(dfa_initial), dfa_final




# Função para imprimir o DFA resultante
def print_dfa(states, alphabet, transitions, initial, final):
    print("Estados: ", states)
    print("Alfabeto: ", alphabet)
    print("Transições:")

    for state in states:
        for symbol in alphabet:
            if tuple(state) in transitions and symbol in transitions[tuple(state)]:
                next_state = transitions[tuple(state)][symbol]
                print(state, "--", symbol, "-->", next_state)

    print("Estado Inicial: ", initial)
    print("Estados Finais: ", final)


# Exemplo de utilização
enfa_states = input("Informe os estados do ENFA separados por vírgula: ").split(',')
alphabet = input("Informe o alfabeto separado por vírgula: ").split(',')
enfa_initial = input("Informe o estado inicial: ")
enfa_final = input("Informe os estados finais separados por vírgula: ").split(',')

enfa_transitions = {}
for state in enfa_states:
    enfa_transitions[state] = {}
    for symbol in alphabet:
        transition = input(
            f"Informe as transições para o estado {state} e o símbolo {symbol} (separadas por vírgula, '-' se não existir): ")
        if transition != '-':
            enfa_transitions[state][symbol] = transition.split(',')

    epsilon_transition = input(
        f"Informe as transições para o estado {state} e épsilon (separadas por vírgula, '-' se não existir): ")
    if epsilon_transition != '-':
        enfa_transitions[state][''] = epsilon_transition.split(',')


if is_afd(enfa_states, alphabet, enfa_transitions):
    print("O autômato fornecido é um AFD.")
elif is_afn_with_epsilon(enfa_transitions):
    print("O autômato fornecido é um AFN com movimentos vazios e será convertido para um AFD.")
    dfa_states, dfa_alphabet, dfa_transitions, dfa_initial, dfa_final = enfa_to_dfa(enfa_states, alphabet, enfa_transitions, enfa_initial, enfa_final)

    print("\nDFA Resultante:\n")
    print_dfa(dfa_states, dfa_alphabet, dfa_transitions, dfa_initial, dfa_final)
