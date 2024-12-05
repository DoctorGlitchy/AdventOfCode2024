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

def correct_order(update, rules):
    # Build a graph of precedence
    update_set = set(update)
    precedence = {x: [] for x in update}
    for x, y in rules:
        if x in update_set and y in update_set:
            precedence[y].append(x)
    
    # Perform topological sort to determine correct order
    result = []
    visited = set()
    visiting = set()

    def dfs(node):
        if node in visiting:  # Cycle detection (shouldn't occur in this problem)
            raise ValueError("Cycle detected in precedence rules!")
        if node not in visited:
            visiting.add(node)
            for req in precedence[node]:
                dfs(req)
            visiting.remove(node)
            visited.add(node)
            result.append(node)

    for page in update:
        if page not in visited:
            dfs(page)

    return result[::-1]  # Reverse to get the correct order

def find_middle(update):
    return update[len(update) // 2]

def solve(input_data):
    rules, updates = parse_input(input_data)
    incorrectly_ordered_middles_sum = 0

    for update in updates:
        if not is_correct_order(update, rules):
            corrected = correct_order(update, rules)
            incorrectly_ordered_middles_sum += find_middle(corrected)
    
    return incorrectly_ordered_middles_sum

if __name__ == "__main__":
    print("Enter your input data, ending with CTRL+Z (Windows) or CTRL+D (Unix):")

    import sys
    input_lines = sys.stdin.read().strip()
    result = solve(input_lines)
    print(f"Sum of middle pages of correctly ordered incorrect updates: {result}")
