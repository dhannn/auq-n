# auq-n: a stress-aware programming language
> ### ayoko na (Tagalog: *😩🙅"I don’t want to do this anymore"*)

A stress-aware programming language for the modern developer
## Overview

auq-n (pronounced *“ayoko na”*) is a novel programming language that introduces **stress-based resource management** as a first-class language feature. Unlike traditional languages that abstract away the cognitive and emotional costs of computation, auq-n makes these costs explicit and enforceable.

## Design Philosophy

Modern software development operates under dual constraints:

1. **Cognitive load** accumulates during development
1. **Productivity expectations** must be maintained

auq-n is the first language to formalize both constraints at the language level, creating a more **realistic computational model** that mirrors actual developer experience.

### Key Innovations

**Stress-Aware Execution Model**  
Every instruction carries an explicit stress cost, reflecting its cognitive complexity. Programs must manage accumulated stress or face termination—much like developers must manage burnout in real-world scenarios.

**Productivity Metrics**  
The runtime enforces minimum throughput requirements (2.5 instructions/second), ensuring programs maintain “acceptable” output levels. This creates a dual-constraint optimization problem unique to auq-n.

**Temporal Realism**  
Instructions execute with realistic delays proportional to their complexity. A mul operation genuinely takes longer than print, reflecting the actual cognitive overhead of mathematical operations.

-----

## Why auq-n?

Traditional programming languages ignore the human element. They assume infinite cognitive resources, unlimited focus, and sustained productivity. This is unrealistic.

auq-n addresses this gap by:

- Making cognitive costs explicit and measurable
- Enforcing resource management at the language level
- Requiring developers to balance multiple competing constraints
- Providing a more honest model of computational work

-----

## Getting Started

### Installation
```
python auq-n.py program.auq
```

### Your First Program
```
set x, 1
print x
```

Output:
```
1.0
✅ Program completed successfully
   Final stress: 9 / 50
   Final productivity: 10.33 instructions/sec
```

The program succeeds because stress remains below threshold (50) and productivity exceeds minimum requirements (2.5 inst/sec).

-----

## Core Concepts

### Stress Accumulation

Each instruction modifies the program’s stress state:

|Instruction|Stress Impact|Execution Time|
|-----------|-------------|--------------|
|`set`      |+6           |0.10s         |
|`add`      |+8           |0.15s         |
|`mul`      |+15          |0.25s         |
|`print`    |+3           |0.08s         |
|`breath.`  |-20          |1.00s         |
|`rejuv!`   |-40          |1.80s         |

Higher-complexity operations (multiplication, division) carry greater stress costs, reflecting their cognitive overhead.

### Stress Mitigation

The language provides two stress-reduction primitives:

- breath. — Moderate stress reduction with moderate time cost
- rejuv! — Significant stress reduction with significant time cost

Strategic use of these primitives is essential for program completion.

### Productivity Requirements

Programs must maintain a minimum throughput of 2.5 instructions per second. Excessive use of stress-reduction primitives can cause productivity to fall below this threshold, resulting in termination.

-----

## Getting Started: Your First Loop

### Attempt 1: Basic Loop
set counter, 0
set max, 5

loop:
    add counter, 1
    print counter
    compare counter, max, loop

Output:
1.0
2.0
3.0
💀 BURNOUT at line 7

    Reason: Overthinking.
    Last thought: "compare counter, max, loop"
    Final stress level: 54 / 50

    You could've prevented this... stupid mf.
    Consider: working smarter, not harder.

Analysis: The program burned out after 3 iterations. Too much work, not enough recovery.

-----

### Attempt 2: Adding Self-Care

*“Have you tried just… breathing?”* — Management
set counter, 0
set max, 5

loop:
    add counter, 1
    print counter
    breath.
    compare counter, max, loop

Output:
1.0
2.0
3.0
💀 BURNOUT at line 8
    Final stress level: 50 / 50

Analysis: Still burned out. One breath. wasn’t enough.

-----

### Attempt 3: More Self-Care

*“Try breathing twice! Self-care is important.”* — HR
set counter, 0
set max, 5

loop:
    add counter, 1
    print counter
    breath.
    breath.
    compare counter, max, loop

Output:
1.0
📉 FIRED!!! at line 6

    Productivity: 2.31 instructions/sec
    Company minimum: 2.5 instructions/sec

    Such a lazy bum. Pack your variables and exit.
    Consider: working harder, not smarter.

Analysis: The program was terminated for insufficient productivity. Too much rest caused throughput to fall below minimum requirements.

-----

## Advanced Techniques

### Productivity Padding

Sometimes maintaining throughput requires… creative solutions.
set counter, 0
set max, 5

loop:
    add counter, 1
    add counter, 0      # <- does nothing, but looks productive
    print counter
    breath.
    compare counter, max, loop

Output:
1.0
2.0
3.0
4.0
5.0
[auq n!] ✅ Program completed successfully

Analysis: By inserting a mathematically neutral operation (`add counter, 0`), we maintain productivity metrics while managing stress levels.

> 💡 Pro tip: Operations that don’t change program state still count toward throughput. This is not a bug—it’s by design.

## Language Reference

### Arithmetic Operations
set x, 10
add x, 5        # x = 15
sub x, 3        # x = 12
mul x, 2        # x = 24
div x, 4        # x = 6

### Control Flow
compare x, 10, less_than_label
jump always_label

less_than_label:
    print x

### Output
print x
print 42

### Stress Management
breath.         # -20 stress, 1.0s
rejuv!          # -40 stress, 1.8s

-----

## Runtime Constraints

Maximum Stress: 50  
Programs exceeding this threshold terminate with BURNOUT status.

Minimum Productivity: 2.5 instructions/second  
Programs falling below this threshold terminate with FIRED status.

Execution Model: Real-time  
Instructions execute with delays proportional to their complexity, creating temporal pressure on productivity metrics.

-----

## Design Patterns

### Throughput Optimization

When stress management requires operations that reduce productivity, consider inserting neutral operations:
add x, 0        # Neutral arithmetic
sub x, 0        # Neutral arithmetic
print x         # Low-stress communication

These operations maintain throughput without adding functional side effects.

### Strategic Recovery

rejuv! operations carry high time costs. Use sparingly and only when stress approaches critical thresholds:
# Instead of:
breath.
breath.

# Consider:
rejuv!

### Stress Budgeting

Complex operations (`mul`, `div`) should be “budgeted” within a program’s stress capacity:
set x, 5
mul x, 3        # +15 stress
breath.         # -20 stress (net: -5)

-----

## Technical Specifications

Paradigm: Imperative, stress-managed  
Typing: Dynamic (float-based)  
Execution: Interpreted with real-time delays  
Resource Model: Dual-constraint (stress + productivity)  
Turing Completeness: Theoretically complete; practically constrained

-----

## Implementation Notes

auq-n is implemented in Python 3.10+ and uses pattern matching for instruction dispatch. The runtime maintains three primary state variables:

- sc — Stress counter
- productivity — Instructions per second
- pc — Program counter

Execution continues until program completion or constraint violation.

-----

## Research Directions

auq-n opens several areas for future investigation:

1. Computational Complexity Under Stress Constraints  
   What is the class of problems solvable within stress/productivity bounds?
1. Optimal Stress Management Strategies  
   Can we formalize patterns for stress-efficient algorithms?
1. Language Extensions  
   Could team-based stress pooling or variable stress costs enable new patterns?
1. Empirical Developer Experience  
   Does programming in auq-n affect developer awareness of cognitive load?

-----

## Contributing

We welcome contributions that advance auq-n’s core mission: making cognitive and productivity constraints first-class language features.

Please ensure PRs maintain the language’s design philosophy.

-----

## License

MIT (Misery Included, Thanks)

-----

## Acknowledgments

auq-n is influenced by:
- Resource-aware programming languages
- Cognitive load theory
- Contemporary software development practices