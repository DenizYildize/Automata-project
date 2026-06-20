This program implements a Deterministic Finite Automaton (DFA) builder from regular expressions. 
It takes a regular expression and an input string as input, constructs a total DFA (including a 
dead/trap state), and performs four main analyses:

1. **Transition Table Display**: Shows the complete transition function δ(q, a) for all states and 
   alphabet symbols, ensuring the DFA is total (every state has a transition for each symbol).

2. **String Acceptance Check**: Determines whether the input string belongs to the language 
   defined by the regular expression by simulating the DFA.

3. **Prefix, Suffix, and Postfix Computation**: Calculates and displays all prefixes, suffixes, 
   and substrings (postfixes) of the input string.

4. **Regular Language Verification**: Confirms that the language described by the regular 
   expression is regular (since all regex patterns define regular languages).

The program uses the `automata-lib` library for core DFA operations and includes custom 
implementations for string acceptance and transition display. It supports common regex patterns 
like `a*b*`, `(a+b)*`, `a+`, `ab*c`, `a+b`, `a+b*`, `(ab)*`, and `a+b+c`.
