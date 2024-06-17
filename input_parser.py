from emitter import Emitter
from receiver import Receiver
from mirror import Mirror

'''
Name:   Emily Lewis Dando
SID:    500687002
Unikey: elew6213

input_parser - A module that parses the inputs of the program. 
We define parsing as checking the validity of what has been entered 
to determine if it's valid. If it's not valid, an appropriate message 
should be printed. Whenever we retrieve input in the program, we 
should be using functions from this module to validate it.

You are free to add more functions, as long as you aren't modifying the
existing scaffold.
'''


def parse_size(user_input: str) -> tuple[int, int] | None:
    # only requires implementation once you reach GET-MY-INPUTS
    '''
    Checks if user_input is a valid input for the size of the circuit board by
    performing the following checks:
      1)  user_input contains exactly 2 tokens. If there are 2 tokens, we
          interpret the first token as width and the second token as height for
          the remaining checks.
      2)  width is an integer.
      3)  height is an integer.
      4)  width is greater than zero.
      5)  height is greater than zero.

    Parameters
    ----------
    user_input - the user input for the circuit's board size

    Returns
    -------
    If all checks pass, returns a tuple containing the width and height of
    the circuit board.
    Else, if at any point a check fails, prints an error message stating the cause
    of the error and returns None, skipping any further checks.

    Example 1:
    >>> size = parse_size('18 0')
    Error: height must be greater than zero
    >>> size
    None

    Example 2:
    >>> size = parse_size('18 6')
    >>> size
    (18, 6)
    '''

    if len(user_input.split()) == 2:
        width = user_input.split()[0] 
        height = user_input.split()[1]

        if width.strip("-").isnumeric() == True:
            width = int(width)
            if height.strip("-").isnumeric() == True:
                height = int(height)
                if width > 0:
                    if height > 0:
                        return (width, height)
                    else:
                        print("Error: height must be greater than zero")
                else:
                    print("Error: width must be greater than zero")
            else:
                print("Error: height is not an integer")
        else:
            print("Error: width is not an integer")
    else:
        print("Error: <width> <height>")

def valid_emitter_symbol(symbol):
    #Determines if users symbol is valid
    accepted = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    i = 0
    while i < len(accepted):
        if symbol == accepted[i]:
            return True
        else:
            i += 1
    return False

def parse_emitter(user_input: str) -> Emitter | None:
    # only requires implementation once you reach GET-MY-INPUTS
    '''
    Checks if user_input is a valid input for creating an emitter by
    performing the following checks in order for any errors: 
      1)  user_input contains exactly 3 tokens. If there are 3 tokens, we 
          interpret the first token  as symbol, the second token as x and the 
          third token as y for the remaining checks.
      2)  symbol is a character between 'A' to 'J'. 
      3)  x is an integer.
      4)  y is an integer.
      5)  x is greater than 0.
      6)  y is greater than 0

    Parameters
    ----------
    user_input - the user input for creating a new emitter

    Returns
    -------
    If all checks pass, returns a new Emitter instance with the specified
    symbol, x and y position set.
    Else, if at any point a check fails, prints an error message stating the cause
    of the error and returns None, skipping any further checks.
    '''
    if len(user_input.split()) == 3:
        symbol = user_input.split()[0].upper()
        x = user_input.split()[1]
        y = user_input.split()[2]
        if valid_emitter_symbol(symbol) == True:
            #what abt floats?
            if x.strip("-").isnumeric() == True:
                x = int(x)
                if y.strip("-").isnumeric() == True:
                    y = int(y)
                    if x >= 0:
                        if y >= 0:
                            return Emitter(symbol, x, y)
                        else:
                            print("Error: y cannot be negative")
                    else:
                        print("Error: x cannot be negative")
                else:
                    print("Error: y is not an integer")
            else: 
                print("Error: x is not an integer")
        else:
            print("Error: symbol is not between 'A'-'J'")
    else:
        print("Error: <symbol> <x> <y>")
    return None
    
def valid_receiver_symbol(symbol):
    accepted = ['R0', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9']
    i = 0
    while i < len(accepted):
        if symbol == accepted[i]:
            return True
        else:
            i += 1
    return False

def parse_receiver(user_input: str) -> Receiver | None:
    # only requires implementation once you reach GET-MY-INPUTS
    '''
    Identical to parse_emitter, with the only differences being
    that the symbol must be between 'R0' to 'R9', and that a new Receiver
    instance is returned if all checks pass.

    Parameters
    ----------
    user_input - the user input for creating a new receiver

    Returns
    -------
    If all checks pass, returns a new Receiver instance with the specified
    symbol, x and y position set.
    Else, if at any point a check fails, prints an error message stating the cause
    of the error and returns None, skipping any further checks.    
    '''
    if len(user_input.split()) == 3:
        symbol = user_input.split()[0]
        x = user_input.split()[1]
        y = user_input.split()[2]
        if valid_receiver_symbol(symbol) == True:
            #what abt floats?
            if x.strip("-").isnumeric() == True:
                x = int(x)
                if y.strip("-").isnumeric() == True:
                    y = int(y)
                    if x >= 0:
                        if y >= 0:
                            return Receiver(symbol, x, y)
                        else:
                            print("Error: y cannot be negative")
                    else:
                        print("Error: x cannot be negative")
                else:
                    print("Error: y is not an integer")
            else: 
                print("Error: x is not an integer")
        else:
            print("Error: symbol is not between R0-R9")
    else:
        print("Error: <symbol> <x> <y>")
    return None


def parse_pulse_sequence(line: str) -> tuple[str, int, str] | None:
    # only requires implementation once you reach RUN-MY-CIRCUIT
    '''
    Checks if line is valid for setting the pulse sequence of an emitter by
    performing the following checks in order for any errors:
      1)  line contains exactly 3 tokens.
          If there are 3 tokens, we interpret the first token as symbol, the
          second token as frequency and the third token as direction for the
          remaining checks.
      2)  symbol is a character between 'A' to 'J'.
      3)  frequency is an integer.
      4)  frequency is greater than zero.
      5)  direction is either 'N', 'E', 'S' or 'W'.

    Parameters
    ----------
    line -- a line from the pulse_sequence.in file

    Returns
    -------
    If all checks pass, returns a tuple containing the specified symbol,
    frequency and direction which can be used for setting the pulse sequence
    of the emitter.
    Else, if at any point a check fails, prints an error message stating the cause
    of the error and returns None, skipping any further checks.    
    '''
    if len(line.split())  == 3:
        symbol = line.split()[0].upper()
        frequency = line.split()[1] 
        direction = line.split()[2]
        if valid_emitter_symbol(symbol) == True:
            if frequency.strip("-").isnumeric() == True:
                frequency =  int(frequency)
                if frequency > 0:
                    if direction.upper() == 'N' or direction.upper() == 'S' or direction.upper() == 'W' or direction.upper() == 'E':
                        return  (symbol, frequency, direction.upper())
                    else:
                        print("Error: direction must be 'N', 'E', 'S' or 'W'")
                else:
                    print("Error: frequency must be greater than zero")
            else:
                print("Error: frequency is not an integer")
        else:
            print("Error: symbol is not between A-J")
    else:
        print("Error: <symbol> <frequency> <direction>")



def parse_mirror(user_input: str) -> Mirror | None:
    # only requires implementation once you reach ADD-MY-MIRRORS
    '''
    Checks if user_input is a valid input for creating a mirror by performing
    the following checks in order for any errors:
      1)  user_input contains exactly 3 tokens. If there are 3 tokens, we
          interpret the first token  as symbol, the second token as x and the
          third token as y for the remaining checks.
      2)  symbol is either '/', '\', '>', '<', '^', or 'v'.
      3)  x is an integer.
      4)  y is an integer.
      5)  x is greater than 0.
      6)  y is greater than 0.

    Parameters
    ----------
    user_input - the user input for creating a mirror

    Returns
    -------
    If all checks pass, returns a new Mirror instance with the specified
    symbol, x and y position set.
    Else, if at any point a check fails, prints an error message stating the cause
    of the error and returns None, skipping any further checks.    
    '''
    if len(user_input.split()) == 3:
        symbol = user_input.split()[0]
        x = user_input.split()[1]
        y = user_input.split()[2]
        if symbol == '/' or symbol == '\\' or symbol == '<' or symbol == '>' or symbol == '^' or symbol == 'v':
            if x.strip('-').isnumeric() == True:
                x = int(x)
                if y.strip('-').isnumeric() == True:
                    y = int(y)
                    if x >= 0:
                        if y >= 0:
                            return Mirror(symbol, x, y)
                        else:
                            print("Error: y cannot be negative")
                    else:
                        print("Error: x cannot be negative")
                else:
                    print("Error: y is not an integer")
            else:
                print("Error: x is not an integer")
        else:
            print("Error: symbol must be '/', '\\', '>', '<', '^' or 'v'")
    else:
        print("Error: <symbol> <x> <y>")
    return None
