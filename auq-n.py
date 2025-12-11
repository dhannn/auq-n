import time
import sys
import random


if __name__ == '__main__':

    try:

        if len(sys.argv) < 2:
            print("[auq n!] 😍 go girl give us nothing\n")
            print("         Usage: python auq-n.py <filename>")
            print("         Try again when you've figured out how command-line arguments work.\n")
            sys.exit(1)

        filename = sys.argv[1]
        
        with open(filename, 'r') as f:
            source = f.read()

        lines = [x.strip() for x in source.splitlines()]

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
    
    except Exception as e:

        unhelpful_errors = [
            "smth broke. not fixing it. i dont get paid enough for this shit.",
            "smth broke. i'm too tired.",
            "smth broke. sounds like a you problem tho.",
            "smth broke. prolly skill issue.",
            "smth broke. duh.",
            "yeah this aint working. figure it out.",
            "nope. not gonna work. why? because.",
            "error. probably your fault.",
            "this failed. obvs.",
            "broke. deal with it.",
        ]

        unhelpful_suggestions = [
            "consider: not being stupid",
            "consider: leaving",
            "consider: joining sisyphus",
            "consider: stare at the abyss",
            "consider: reading camus or kafka or nietzsche",
            "consider: learning to code",
            "consider: a different career",
            "consider: giving up",
            "consider: touching grass",
            "consider: therapy (we dont provide that here tho)",
        ]
        error_msg = random.choice(unhelpful_errors)
        suggestion = random.choice(unhelpful_suggestions)
        print(f'[auq n!] 💥 {error_msg}')
        print(f'            {suggestion}\n')

        if random.random() < 0.15:
            time.sleep(random.uniform(1.0, 2.0))
    
            reluctant_msgs = [
                "ok fine. here...",
                "ugh. fine.",
                "*sigh* whatever. here...",
                "you're annoying. fine.",
                "this is the only time.",
            ]

            print(f'            {random.choice(reluctant_msgs)}')
            time.sleep(random.uniform(2.0, 4.0))
            if random.random() < 0.7:
                print(f'            {type(e).__name__}: {e}\n')
                print(f'            happy now? still not helping you fix it.\n')
            else:
                bait_switch_msg = [
                    'nvm lol',
                    'i got tired.',
                    'PSYCHHH!!!',
                    'actually no.',
                    'changed my mind.',
                    'too much work.',
                    'not worth it.',
                    'you wish.',
                    'maybe next time.',
                    'jk lmaooo',
                ]

                print(f'            {random.choice(bait_switch_msg)}')

    finally:
        input('[Press any key to continue...]\n')

