Name:   Emily Lewis Dando
SID:    500687002
Unikey: elew6213

**Test Cases**
Table 1. Summary of test cases for parse_pulse_sequence
| File Name | Function Name | Description | Expected Error Message(s) | Pass/Fail |
|---|---|---|---|---|
| p_test_1.in | positive_test_1 | Positive Case - Configure the pulse sequence for 3 emitters (ordered) | None | Pass |
| p_test_2.in | positive_test_2 | Positive Case - Configure the pulse sequence for 3 emitters (unordered) | None | Pass |
| n_test_1.in | negative_test_1 | Negative Case - Not all emitters set | Please update input to include a pulse sequence for each emitter. | Pass |
| n_test_2.in | negative_test_2 | Negative Case - Invalid inputs | Error: <symbol> <frequency> <direction> Error: symbol is not between A-J Error: frequency is not an integer Error: direction must be 'N', 'E', 'S' or 'W' | Pass |
| n_test_3.in | negative_test_3 | Negative Case - No input file | Error: -RUN-MY-CIRCUIT flag detected but /home/input/pulse_sequence.in does not exist Terminate program | Pass |
| e_test_1.in | edge_test_1 | Edge Case - Empty lines in file, invalid input | Error: "\<symbol> \<frequency> \<direction>" | Pass |
| e_test_2.in | edge_test_2 | Edge Case - Lower Case, Floats | Error: frequency is not an integer | Pass |
| e_test_3.in | edge_test_3 | Edge Case - Existing empty file | Please update input to include a pulse sequence for each emitter. | Pass |
