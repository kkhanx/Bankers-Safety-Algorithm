from input_handler import read_input, validate_input, format_processes, write_output

def test_all():
    print("- TESTING INPUT HANDLER -")

    #read input and print out the data in input.json
    data = read_input("input.json")
    print("Read Input:", data)

    #validate input
    try:
        validate_input(data)
        print("Validation: PASSED")
    except Exception as e:
        print("Validation: FAILED", e)
        return

    #format processes
    processes = format_processes(data["processes"])
    print("Formatted Processes:", processes)

    #output (fake example result btw and only prints when there are no basic errors)
    #we still need to code the actual deadlock and safe logic i think
    result = {
        "state": "SAFE",
        "safe_sequence": processes
    }
   
   #code for the deadlock example 
    """
    result = {
    "state": "DEADLOCK" ,
    "deadlocked_process": [" P2 " , " P3 "]
    }
    """
    
    #write output to the output.json file
    write_output("output.json", result)
    print("Output written to output.json: \n",result)

if __name__ == "__main__":
    test_all()