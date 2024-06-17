import typing as t
from laser_circuit import LaserCircuit
from circuit_for_testing import get_my_lasercircuit
from run import set_pulse_sequence

'''
Name:   Emily Lewis Dando
SID:    500687002
Unikey: elew6213

This test program checks if the set_pulse_sequence function is implemented
correctly.

You can modify this scaffold as needed (changing function names, parameters, 
or implementations...), however, DO NOT ALTER the code in circuit_for_testing 
file, which provides the circuit. The circuit can be retrieved by calling 
get_my_lasercircuit(), and it should be used as an argument for the 
set_pulse_sequence function when testing.

Make sure to create at least six functions for testing: two for positive cases,
two for negative cases, and two for edge cases. Each function should take
different input files.

NOTE: Whenever we use ... in the code, this is a placeholder for you to
replace it with relevant code.
'''

def positive_test_1(my_circuit: LaserCircuit, pulse_file_path: str) -> None:
    '''
    Positive test case to verify that all emitters are set.

    Parameters
    ----------
    my_circuit      - the circuit instance for testing
    pulse_file_path - path to the pulse sequence file

    Expected Error Message:
    -----------------------
    None
    '''   

    print("----------------------------")
    print("Positive Test 1: Start\n")

    #Run function
    set_pulse_sequence(my_circuit, pulse_file_path)

    # Simplify emitter names for my_circuit
    a = my_circuit.emitters[0]
    b = my_circuit.emitters[1]
    c = my_circuit.emitters[2]

    # Check all emitters are set
    i = 0
    while i < len(my_circuit.emitters):
        assert my_circuit.emitters[i].pulse_sequence_set == True, "Error: all emitters should be set"
        i += 1

    #Check values of all emitters
    assert a.frequency == 32 and a.direction == 'E', "Pulse Sequence for 'A' should be 32, 'E'."
    assert b.frequency == 97 and b.direction == 'W', "Pulse Sequence for 'B' should be 97, 'W'."
    assert c.frequency == 1 and c.direction == 'N', "Pulse Sequence for 'C' should be 1, 'N'."

    print("\nPositive Test 1: Passed!")
    print("----------------------------\n")

def positive_test_2(my_circuit: LaserCircuit, pulse_file_path: str) -> None: #completed
    '''
    Positive test case to verify that all emitters are set, even when inputs are given out of order

    Parameters
    ----------
    my_circuit      - the circuit instance for testing
    pulse_file_path - path to the pulse sequence file

    Expected Error Message:
    -----------------------
    None
    '''   

    print("----------------------------")
    print("Positive Test 2: Start\n")

    #Run function
    set_pulse_sequence(my_circuit, pulse_file_path)

    # Simplify emitter names for my_circuit
    a = my_circuit.emitters[0]
    b = my_circuit.emitters[1]
    c = my_circuit.emitters[2]

    # Check all emitters are set
    i = 0
    while i < len(my_circuit.emitters):
        assert my_circuit.emitters[i].pulse_sequence_set == True, "Error: all emitters should be set"
        i += 1

    #Check values of all emitters
    assert a.frequency == 56 and a.direction == 'S', "Pulse Sequence for 'A' should be 56, 'S'."
    assert b.frequency == 555 and b.direction == 'E', "Pulse Sequence for 'B' should be 555, 'E'."
    assert c.frequency == 109 and c.direction == 'W', "Pulse Sequence for 'C' should be 109, 'W'."

    print("\nPositive Test 2: Passed!")
    print("----------------------------\n")

def negative_test_1(my_circuit: LaserCircuit, pulse_file_path: str) -> None: #completed
    '''
    Negative test case to verify the set_pulse_sequence function will print a warning when not all emitters are set.

    Parameters
    ----------
    my_circuit      - the circuit instance for testing
    pulse_file_path - path to the pulse sequence file

    Expected Error Message:
    -----------------------
    "Please update input to include a pulse sequence for each emitter."
    '''
    print("----------------------------")
    print("Negative Test 1: Start\n")

    #Run function
    set_pulse_sequence(my_circuit, pulse_file_path)

    # Simplify emitter names for my_circuit
    a = my_circuit.emitters[0]
    b = my_circuit.emitters[1]
    c = my_circuit.emitters[2]

    # Check if emitters' pulse sequence are set, and set correctly.

    # Check Emitter 'A'
    assert a.pulse_sequence_set == True, "Emitter 'A' should be set."
    assert a.frequency == 100 and a.direction == 'S', "Pulse Sequence for 'A' should be 100, 'S'."

    # Check Emitter 'B'
    assert b.pulse_sequence_set == True, "Emitter 'B' should be set."
    assert b.frequency == 256 and b.direction == 'E', "Pulse Sequence for 'B' should be 256, 'E'."

    # Check Emitter 'C' - not set
    assert c.pulse_sequence_set == False, "Emitter 'C' should not be set."
    assert c.frequency == 0 and c.direction is None, "Pulse Sequence for 'C' should be 0, 'None'."

    print("\n***To pass, expected error message must print***")
    print("\nNegative Test 1: Complete!")
    print("----------------------------\n")

def negative_test_2(my_circuit: LaserCircuit, pulse_file_path: str) -> None: #completed
    '''
    Negative test case to verify expected invalid pulse sequences will 
    print necessary warnings in the correct order.

    Parameters
    ----------
    my_circuit      - the circuit instance for testing
    pulse_file_path - path to the pulse sequence file
    
    Expected Error Message:
    -----------------------
    Error: <symbol> <frequency> <direction>
    Error: symbol is not between A-J
    Error: frequency is not an integer
    Error: direction must be 'N', 'E', 'S' or 'W'
    '''

    print("----------------------------")
    print("Negative Test 2: Start\n")

    #Run function
    set_pulse_sequence(my_circuit, pulse_file_path)

    print("\n***To pass, your terminal must print the expected error messages in the correct order.***")
    print("Negative Test 2: Complete!")
    print("----------------------------\n")

def negative_test_3(my_circuit: LaserCircuit, pulse_file_path: str) -> None: #completed
    '''
    Negative test case to verify that the program will terminate if a non-existing
    file is parsed as pulse_file_path

    Parameters
    ----------
    my_circuit      - the circuit instance for testing
    pulse_file_path - path to the pulse sequence file

    Expected Error Message:
    -----------------------
    "Error: -RUN-MY-CIRCUIT flag detected but /home/input/pulse_sequence.in does not exist"
    '''

    print("----------------------------")
    print("Negative Test 3: Start\n")
    print("***To pass, your terminal must print the expected error message and terminate.***")
    print("\nNegative Test 3: Complete!")
    print("----------------------------")

    #Run function
    set_pulse_sequence(my_circuit, pulse_file_path)

def edge_test_1(my_circuit: LaserCircuit, pulse_file_path: str) -> None: #completed
    '''
    Edge test case to verify behaviour when there are empty lines in an input file
    Program should ignore empty lines and continue.
    
    Parameters
    ----------
    my_circuit      - the circuit instance for testing
    pulse_file_path - path to the pulse sequence file 

    Expected Errors:
    ----------------
    <symbol> <frequency> <direction>
    '''

    print("----------------------------")
    print("Edge Test 1: Start\n")

    #Run function
    set_pulse_sequence(my_circuit, pulse_file_path)

    # Simplify emitter names for my_circuit
    a = my_circuit.emitters[0]
    b = my_circuit.emitters[1]
    c = my_circuit.emitters[2]
    
    #Check values of all emitters
    assert a.frequency == 18 and a.direction == 'S', "Pulse Sequence for 'A' should be 18, 'S'."
    assert b.frequency == 22 and b.direction == 'E', "Pulse Sequence for 'B' should be 22, 'E'."
    assert c.frequency == 55 and c.direction == 'W', "Pulse Sequence for 'C' should be 55, 'W'."

    #Check that blank lines are not added to count
    
    print('''\n***To pass, your program must print only 4 lines from input
and produced only expected error messages.***''')
    print("\nEdge Case 1: Complete!")
    print("----------------------------\n")

def edge_test_2(my_circuit: LaserCircuit, pulse_file_path: str) -> None: #completed
    '''
    Edge test case to verify that symbols and directions in lower case 
    can be successfully inputted and returned as upper case. Verify
    that floats are not permissible.
    
    Parameters
    ----------
    my_circuit      - the circuit instance for testing
    pulse_file_path - path to the pulse sequence file 

    Expected Error Message:
    -----------------------
    Error: frequency is not an integer
    '''

    print("----------------------------")
    print("Edge Test 2: Start\n")

    #Run function
    set_pulse_sequence(my_circuit, pulse_file_path)

    # Simplify emitter names for my_circuit
    a = my_circuit.emitters[0]
    b = my_circuit.emitters[1]
    c = my_circuit.emitters[2]

    #Check the name is correct
    assert a.symbol == 'A', 'Symbol must be uppercase'
    assert b.symbol == 'B', 'Symbol must be uppercase'
    assert c.symbol == 'C', 'Symbol must be uppercase'

    #Check the frequencies are correct
    assert a.frequency == 66 and a.direction == 'S', "Pulse Sequence for 'A' should be 66, 'S'."
    assert b.frequency == 77 and b.direction == 'W', "Pulse Sequence for 'B' should be 77, 'W'."
    assert c.frequency == 0 and c.direction == None, "Pulse Sequence for 'C' should be 0, None."

    print("\n***To pass, your terminal must print the expected error message***")
    print("\nEdge Test 2: Complete!")
    print("----------------------------\n")

def edge_test_3(my_circuit: LaserCircuit, pulse_file_path: str) -> None: #completed
    '''
    Edge test to verify behaviour when parsing in an empty file.
    
    Parameters
    ----------
    my_circuit      - the circuit instance for testing
    pulse_file_path - path to the pulse sequence file 

    Expected Error Message:
    ------------------------
    Please update input to include a pulse sequence for each emitter.

    '''
    print("----------------------------")
    print("Edge Test 3: Start\n")

    #Run function
    set_pulse_sequence(my_circuit, pulse_file_path)

    print("\n***To pass, your terminal must print the expected error message***")
    print("\nEdge Test 3: Complete!")
    print("----------------------------\n")

if __name__ == '__main__':
    #Run each function for testing
    positive_test_1(get_my_lasercircuit(), '/home/input/p_test_1.in')
    positive_test_2(get_my_lasercircuit(), '/home/input/p_test_2.in')
    negative_test_1(get_my_lasercircuit(), '/home/input/n_test_1.in')
    negative_test_2(get_my_lasercircuit(), '/home/input/n_test_2.in')
    edge_test_1(get_my_lasercircuit(), '/home/input/e_test_1.in')
    edge_test_2(get_my_lasercircuit(), '/home/input/e_test_2.in')
    edge_test_3(get_my_lasercircuit(), '/home/input/e_test_3.in')
    negative_test_3(get_my_lasercircuit(), 'hello') #terminates program



