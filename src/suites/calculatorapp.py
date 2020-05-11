import src.scripts.calculator_ui2 as Calculator
import os


def run_suite():
    # path to inputs
    cwd_path = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(cwd_path, "..", "..", "inputs", "calculatorapp.txt")
    with open(path, 'r') as fp:
        lines = (line.rstrip() for line in fp)  # All lines including the blank ones
        lines = (line for line in lines if line)
        for line in lines:
            # only read line with a + b format
            array = line.split()
            if len(array) == 3:
                # call the script
                Calculator.run(array[0], array[1], array[2])
            else:
                continue




if __name__ == "__main__":
    run_suite()
