import os

# A dictionary to maintain variable history across code blocks
variable_history = {}

# Function to execute code in a specific language (currently only Python)
def execute_code(language, code, variables):
    if language == 'Python':
        # Inject the variables into the code
        for var in variables:
            code = code.replace(f"${var}$", str(variables[var]))

        try:
            # Execute the Python code in the context of the variable history
            exec(code, globals(), variable_history)
        except Exception as e:
            print(f"Error executing {language} code: {e}")

# Function to parse and execute the program
def execute(program):
    # Reading the program file
    with open(program, 'r') as file:
        code = file.read()

    # Splitting the code at a line level
    lines = code.split('\n')

    # Parsing and executing each line
    for line in lines:
        line = line.strip()
        
        if line.startswith('[') and line.endswith(']'):
            # It's a simple statement
            statement = line[1:-1]
            print(f"Statement: {statement}")

        elif '(' in line and '{' in line and ')' in line and '}' in line:
            # It's a code block in a specific language
            lang_start = line.index('(') + 1
            lang_end = line.index(')')
            code_start = line.index('{') + 1
            code_end = line.index('}')

            language = line[lang_start:lang_end]
            code_block = line[code_start:code_end]

            # Identify variables marked with $
            variables = {}
            while '$' in code_block:
                var_start = code_block.index('$') + 1
                var_end = code_block.index('$', var_start)
                var_name = code_block[var_start:var_end]
                
                # Prompt for variable input if not already in history
                if var_name not in variable_history:
                    variable_value = input(f"Enter value for {var_name}: ")
                    variable_history[var_name] = variable_value

                variables[var_name] = variable_history[var_name]
                code_block = code_block.replace(f"${var_name}$", str(variable_history[var_name]))

            # Execute the code block
            execute_code(language, code_block, variable_history)

# Example usage
execute('./test.code')
