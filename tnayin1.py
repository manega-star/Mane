def write_netlist(file_path, transistors, resistors):

    with open(file_path, 'w') as file:

        for transistor in transistors:

            file.write(f"{transistor['name']} {transistor['parameters']}\n")

        for resistor in resistors:

            file.write(f"{resistor['name']} {resistor['parameters']}\n")

def parse_netlist(file_path):

    transistors = []

    resistors = []

    with open(file_path, 'r') as file:

        for line in file:

            line = line.strip()

            if line.startswith("*") or not line:

                continue

            if line.startswith("M"):

                parts = line.split()

                transistors.append({"name": parts[0], "parameters": " ".join(parts[1:])})

            elif line.startswith("R"):

                parts = line.split()

                resistors.append({"name": parts[0], "parameters": " ".join(parts[1:])})

    return transistors, resistors

file_path = "hsp.txt"

transistors, resistors = parse_netlist(file_path)

print("Parsed Transistors:", transistors)

print("Parsed Resistors:", resistors)

write_netlist("output_netlist.txt", transistors, resistors)

print("Netlist saved to output_netlist.txt") 
