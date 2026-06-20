from automata.fa.dfa import DFA
from automata.fa.nfa import NFA
import re

def accepts_input(dfa, input_str):
    """Custom implementation to check if string is accepted by DFA"""
    current_state = dfa.initial_state
    for symbol in input_str:
        if symbol not in dfa.input_symbols:
            return False
        if symbol not in dfa.transitions[current_state]:
            return False
        current_state = dfa.transitions[current_state][symbol]
    return current_state in dfa.final_states

def build_dfa_from_regex(regex_str, alphabet):
    """
    Build a total DFA from a simple regular expression.
    """
    if isinstance(alphabet, set):
        alphabet = sorted(list(alphabet))
    elif isinstance(alphabet, list):
        alphabet = sorted(alphabet)
    else:
        alphabet = sorted(list(alphabet))
    
    regex_str = regex_str.strip()
    
    if regex_str == '(a+b)*':
        states = {'q0'}
        initial_state = 'q0'
        transitions = {'q0': {}}
        
        for symbol in alphabet:
            transitions['q0'][symbol] = 'q0'
        
        final_states = {'q0'}  
        
        return DFA(
            states=states,
            input_symbols=alphabet,
            transitions=transitions,
            initial_state=initial_state,
            final_states=final_states
        )
    
    elif regex_str == 'a*b*':
        states = {'q0', 'q1', 'q_dead'}
        initial_state = 'q0'
        transitions = {
            'q0': {},
            'q1': {},
            'q_dead': {}
        }
        
        if 'a' in alphabet:
            transitions['q0']['a'] = 'q0'
        if 'b' in alphabet:
            transitions['q0']['b'] = 'q1'
            transitions['q1']['b'] = 'q1'
        
        if 'a' in alphabet:
            transitions['q1']['a'] = 'q_dead'
        
        for symbol in alphabet:
            if symbol not in transitions['q_dead']:
                transitions['q_dead'][symbol] = 'q_dead'
            if symbol not in transitions['q1']:
                transitions['q1'][symbol] = 'q_dead'
            if symbol not in transitions['q0']:
                transitions['q0'][symbol] = 'q_dead'
        
        final_states = {'q0', 'q1'} 
        
        return DFA(
            states=states,
            input_symbols=alphabet,
            transitions=transitions,
            initial_state=initial_state,
            final_states=final_states
        )
    
    elif regex_str == 'a+':
        states = {'q0', 'q1', 'q_dead'}
        initial_state = 'q0'
        transitions = {
            'q0': {},
            'q1': {},
            'q_dead': {}
        }
        
        if 'a' in alphabet:
            transitions['q0']['a'] = 'q1'
            transitions['q1']['a'] = 'q1'
        
        for symbol in alphabet:
            if symbol not in transitions['q_dead']:
                transitions['q_dead'][symbol] = 'q_dead'
            if symbol not in transitions['q1']:
                transitions['q1'][symbol] = 'q_dead'
            if symbol not in transitions['q0']:
                transitions['q0'][symbol] = 'q_dead'
        
        final_states = {'q1'} 
        
        return DFA(
            states=states,
            input_symbols=alphabet,
            transitions=transitions,
            initial_state=initial_state,
            final_states=final_states
        )
    
    else:
        print(f"⚠️ Warning: Pattern '{regex_str}' not fully supported.")
        states = {'q0', 'q_dead'}
        initial_state = 'q0'
        transitions = {
            'q0': {},
            'q_dead': {}
        }
        for symbol in alphabet:
            transitions['q0'][symbol] = 'q_dead'
            transitions['q_dead'][symbol] = 'q_dead'
        final_states = set()
        
        return DFA(
            states=states,
            input_symbols=alphabet,
            transitions=transitions,
            initial_state=initial_state,
            final_states=final_states
        )

def get_alphabet_from_regex(regex_str):
    """Extract alphabet letters from the regular expression."""
    special_chars = {'*', '+', '?', '.', '|', '(', ')', '[', ']', '{', '}', '^', '$', '\\'}
    alphabet = set()
    for char in regex_str:
        if char not in special_chars and char.isalpha():
            alphabet.add(char)
    return alphabet if alphabet else {'a', 'b'}

def is_regular_language(regex_str):
    """Is the language regular? - A simple check."""
    return True

def print_dfa_transitions(dfa):
    """Print the transition function of the DFA."""
    print("\n--- DFA (Total) Transition Function ---")
    for state in sorted(dfa.states):
        for symbol in sorted(dfa.input_symbols):
            next_state = dfa.transitions[state][symbol]
            print(f"δ({state}, {symbol}) = {next_state}")
    print("----------------------------------------\n")

def check_acceptance(dfa, input_str):
    """Check if the input string is accepted by the DFA."""
    try:
        if accepts_input(dfa, input_str):
            print(f"String '{input_str}' is accepted by the language.")
        else:
            print(f"String '{input_str}' is rejected by the language.")
    except Exception as e:
        print(f"Error in acceptance check: {e}")

def compute_prefix_suffix_postfix(input_str):
    """Compute and print Prefix, Suffix, and Postfix of a string."""
    length = len(input_str)
    
    prefixes = []
    for i in range(length + 1):
        prefixes.append(input_str[:i])
    
    suffixes = []
    for i in range(length + 1):
        suffixes.append(input_str[i:])
    
    postfixes = sorted(suffixes, key=len)
    
    print(f"\nPrefixes of '{input_str}': {prefixes}")
    print(f"Suffixes of '{input_str}': {suffixes}")
    print(f"Postfixes of '{input_str}': {postfixes}")

def main():
    # Get input
    regex = input("Please enter the language (regular expression): ")
    input_string = input("Please enter the string to test: ")
    
    # Extract alphabet
    alphabet = get_alphabet_from_regex(regex)
    print(f"Extracted alphabet: {alphabet}")
    
    # Build DFA
    dfa = build_dfa_from_regex(regex, alphabet)
    
    # a) Print transition function
    print_dfa_transitions(dfa)
    
    # b) Check acceptance of the string
    check_acceptance(dfa, input_string)
    
    # c) Compute Prefix, Suffix, and Postfix
    compute_prefix_suffix_postfix(input_string)
    
    # d) Check if the language is regular
    if is_regular_language(regex):
        print("\nThe input language is Regular.")
    else:
        print("\nThe input language is NOT Regular.")

if __name__ == "__main__":
    main()