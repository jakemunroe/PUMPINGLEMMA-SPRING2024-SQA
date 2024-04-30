# File that will be used to fuzz 5 methods of our choice.
# Will be executed automatically from GitHub actions.
# Simple change
import traceback

# Import your functions here; ensure the module paths and names are correct
from empirical.report import reportDensity, reportProp
from mining.mining import checkPythonFile, getPythonFileCount
from empirical.frequency import reportEventDensity

def fuzz():
    func_names = [
        reportDensity,
        reportProp,
        checkPythonFile,
        getPythonFileCount,
        reportEventDensity
    ]

    # Provide sample arguments suitable for each function; update as needed based on actual parameters these functions accept
    func_args = [
        ["----saa", 422422, False, None],
        ["@@@@#@$@", "[][][]", True, None],
        ["/user/Documents", "admin_domain", 21421421512421, None],
        ["password", False, None, "_hash"],
        [None, True, "mykey", "adminkey", 2141424]
    ]
    
    index = 0

    for func in func_names:
        args = func_args[index]
        for arg in args:
            try:
                result = func(arg)
                if result is not None:
                    print(f"Result returned is {result} for arguments {arg}")
            except Exception as e:
                print(f"{func.__name__} has an issue with arguments {arg}")
                traceback.print_exc()  # Prints the traceback of the exception
            else:
                print(f"{func.__name__} passed with arguments {arg}")
        index += 1

fuzz()
