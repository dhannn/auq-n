import time
test = """set counter, 0
set max, 10

loop:
    add counter, 0
    add counter, 0
    breathe.
    add counter, 1
    print counter
    breathe.
    compare counter, max, loop
"""

lines = [x.strip() for x in test.splitlines()]

labels = {}
_vars = {}

for num, line in enumerate(lines): 
    if line.endswith(':'):
        labels[line.strip(':')] = num

stress_table = {
    'set': (6, 'Responsibility.'),
    'add': (8, 'Too much effort.'),
    'sub': (8, 'Too much effort.'),
    'mul': (15, 'Cognitive overload.'),
    'div': (15, 'Cognitive overload.'),
    'compare': (12, 'Overthinking.'),
    'jump': (10, 'Commitment.'),
    'print': (3, 'Mild strain.'),
    'breathe.': (-20, 'Self-care.'),
    'rejuv!': (-40, 'Hard reset.')
}

exec_time = {
    'set': 0.1,
    'add': 0.15,
    'sub': 0.15,
    'mul': 0.25,
    'div': 0.25,
    'compare': 0.2,
    'jump': 0.18,
    'print': 0.08,
    'breathe.': 1.0,
    'rejuv!': 1.8
}

pc = 0
sc = 0
MAX_STRESS = 50
MIN_PRODUCTIVITY = 2.5
instructions_executed = 0
started = time.time()

successful = True

while pc < len(lines):
    old_pc = pc
    line = lines[pc]

    if line.endswith(':') or line.strip() == '':
        pc += 1
        continue

    opcode, *tail = line.split()
    args = [arg.strip(',') for arg in tail]
    match opcode:
        case 'set':
            var = args[0]
            init_val = float(args[1])
            _vars[var] = init_val
            
        case 'add':
            var = float(_vars[args[0]])

            if args[1] in _vars.keys():
                operand = float(_vars[args[1]])
            else:
                operand = float(args[1])
            
            _vars[args[0]] = var + operand
            
        case 'sub':
            var = float(_vars[args[0]])

            if args[1] in _vars.keys():
                operand = float(_vars[args[1]])
            else:
                operand = float(args[1])
            
            _vars[args[0]] = var - operand
            
        case 'mul':
            var = float(_vars[args[0]])

            if args[1] in _vars.keys():
                operand = float(_vars[args[1]])
            else:
                operand = float(args[1])
            
            _vars[args[0]] = var * operand
            
        case 'div':
            var = float(_vars[args[0]])

            if args[1] in _vars.keys():
                operand = float(_vars[args[1]])
            else:
                operand = float(args[1])
            
            _vars[args[0]] = var / operand
        case 'compare':

            if args[0] in _vars.keys():
                lhs = float(_vars[args[0]])
            else:
                lhs = float(args[0])

            if args[1] in _vars.keys():
                rhs = float(_vars[args[1]])
            else:
                rhs = float(args[1])
            
            if lhs < rhs:
                pc = labels[args[2]]
            else:
                if len(args) == 4:
                    pc = labels[args[3]]
        case 'jump':
            pc = labels[args[0]]
        case 'print':

            if args[0] in _vars.keys():
                val = float(_vars[args[0]])
            else:
                val = float(args[0])

            print(val)
            
        case 'breathe.':
            pass
        case 'rejuv!':
            pass
        case not_found:
            print(f'[auq n!] ⁉️  wtf is this?? at line {old_pc}')
            print(f'            idk what to do with this instruction: "{line}"\n')
            print(f'            This is either:')
            print(f'                (a) a typo (skill issue btw)')
            print(f'                (b) a feature request (not our problem)')
            print(f'                (c) you\'re trying to be creative (stop that)')
            print(f'            Consider: stop being stupid.')
            successful = False
            break
    
    time.sleep(exec_time[opcode])
    instructions_executed += 1
    elapsed = time.time() - started

    productivity = instructions_executed / elapsed

    stress_lvl, reason = stress_table[opcode]
    sc += stress_lvl

    if sc >= MAX_STRESS:
        print(f'[auq n!] 💀 BURNOUT at line {old_pc}\n')
        print(f'            Reason: {reason}')
        print(f'            Last thought: "{line.strip()}"')
        print(f'            Final stress level: {sc} / {MAX_STRESS}\n')
        print(f'            You could\'ve prevented this... stupid mf.')
        print(f'            Consider: working smarter, not harder.\n')
        successful = False
        break
    
    if productivity < MIN_PRODUCTIVITY:
        print(f'[auq n!] 📉 FIRED!!! at line {old_pc}\n')
        print(f'            Last thought: "{line.strip()}"')
        print(f'            Productivity: {productivity:.3f} instructions/sec')
        print(f'            Company minimum: {MIN_PRODUCTIVITY} instructions/sec\n')
        print(f'            Such a lazy bum. Pack your variables and exit.')
        print(f'            Consider: working harder, not smarter.\n')
        successful = False
        break

    pc += 1

if successful:
    print(f'[ge lng] ✅ Program completed successfully\n')
    print(f'            Final stress: {sc} / {MAX_STRESS}')
    print(f'            Final productivity: {productivity:.3f} instructions/sec\n')
    print(f'            Congratulations on surviving your job!')
    print(f'            Your reward: another job to run. These processes ain\'t gonna run themselves!\n')

input('[Press any key to continue...]\n')
