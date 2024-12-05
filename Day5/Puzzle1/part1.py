def parse_input(input_data):
    rules_section, updates_section = input_data.strip().split("\n\n")
    rules = [tuple(map(int, rule.split("|"))) for rule in rules_section.splitlines()]
    updates = [list(map(int, update.split(","))) for update in updates_section.splitlines()]
    return rules, updates

def is_correct_order(update, rules):
    # Build a map of precedence for the current update
    update_set = set(update)
    precedence = {x: [] for x in update}
    for x, y in rules:
        if x in update_set and y in update_set:
            precedence[y].append(x)
    
    # Validate ordering
    seen = set()
    for page in update:
        for req in precedence[page]:
            if req not in seen:
                return False
        seen.add(page)
    return True

def find_middle(update):
    return update[len(update) // 2]

def solve(input_data):
    rules, updates = parse_input(input_data)
    middle_sum = 0

    for update in updates:
        if is_correct_order(update, rules):
            middle_sum += find_middle(update)
    
    return middle_sum

if __name__ == "__main__":
    print("Paste your input data and press Enter, then Ctrl+D (or Ctrl+Z on Windows) to finish:")
    import sys
    input_data = sys.stdin.read()
    result = solve(input_data)
    print(f"Sum of middle pages of correctly ordered updates: {result}")
