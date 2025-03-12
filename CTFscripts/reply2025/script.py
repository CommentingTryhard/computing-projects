# The name of your input file.
file_input_name = "input.txt"
# The name of your output file.
file_output_name = "output.txt"

IGNORE_ME_file_input = open(file_input_name, 'r')
IGNORE_ME_file_output = open(file_output_name, 'w')
IGNORE_ME_file_output_storage = []

def input(ignored=None):
    if ignored != None:
        print("Reading {}".format(ignored))
    return IGNORE_ME_file_input.readline().strip()

def output(output):
    print("Writing line: {}".format(output))
    IGNORE_ME_file_output_storage.append(output + "\n")

def submit():
    IGNORE_ME_file_output_storage[-1] = IGNORE_ME_file_output_storage[-1].strip()
    IGNORE_ME_file_output.writelines(IGNORE_ME_file_output_storage)
    IGNORE_ME_file_output.close()
    print("Saved and finished! Send your output file called {}".format(file_output_name))

import math

def calculate_real_risk(nodes):
    real_risk = {node: nodes[node]["estimated_risk"] for node in nodes}
    
    changed = True
    while changed:
        changed = False
        new_risk = real_risk.copy()
        
        for node, data in nodes.items():
            max_risk = real_risk[node]
            for neighbor in data["connections"]:
                neighbor_risk = real_risk.get(neighbor, nodes[neighbor]["estimated_risk"])
                risk_value = math.ceil((nodes[node]["estimated_risk"] + neighbor_risk) / 2)
                max_risk = max(max_risk, risk_value)
            
            if max_risk > real_risk[node]:
                new_risk[node] = max_risk
                changed = True
        
        real_risk = new_risk
    
    return {node: real_risk[node] for node in nodes if node.startswith("k")}

def process_test_case(n, lines):
    nodes = {}
    for line in lines:
        parts = line.split()
        node_id = parts[0]
        estimated_risk = int(parts[1])
        connections = parts[2:] if len(parts) > 2 else []
        nodes[node_id] = {"estimated_risk": estimated_risk, "connections": connections}
    
    key_services = calculate_real_risk(nodes)
    return key_services

def main():
    strinput = input()
    test_cases = int(strinput)
    results = []
    
    for case_num in range(1, test_cases + 1):
        n = int(input())
        case_lines = input()
        
        key_services = process_test_case(n, case_lines)
        
        result = f"Case #{case_num}: {len(key_services)} " + " ".join(f"{k} {v}" for k, v in sorted(key_services.items()))
        results.append(result)
    
        output(results)
    submit()

if __name__ == "__main__":
    main()