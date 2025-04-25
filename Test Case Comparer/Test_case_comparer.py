def compare(expected, actual):
    with open(expected, 'r') as f1, open(actual, 'r') as f2:
        expected_lines = [line.strip().lower() for line in f1.readlines()]
        actual_lines = [line.strip().lower() for line in f2.readlines()]
    
    if len(expected_lines) != len(actual_lines):
        print("Warning: Files have different number of lines!")
    
    Flag = True
    
    for i, (expected, actual) in enumerate(zip(expected_lines, actual_lines), start=1):
        if expected == actual:
            print(f"Line {i}: Match")
        else:
            print(f"Line {i}: Mismatch (Expected: {expected}, Actual: {actual})")
            Flag = False
    
    print("\nOverall Match:", Flag)

compare('expected.txt', 'actual.txt')
