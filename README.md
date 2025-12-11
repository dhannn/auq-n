# auq-n: a stress-aware programming language
> ### ayoko na (Tagalog: 😩🙅 *"I don’t want to do this anymore"*)

A stress-aware programming language for the modern developer
## Overview

auq-n (pronounced *“ayoko na”*) is a novel programming language that introduces **stress-based resource management** as a first-class language feature. Unlike traditional languages that abstract away the cognitive and emotional costs of computation, auq-n makes these costs explicit and enforceable.

## Design Philosophy

Modern software development operates under dual constraints:

1. **Cognitive load** accumulates during development
1. **Productivity expectations** must be maintained

auq-n is the first language to formalize both constraints at the language level, creating a more **realistic computational model** that mirrors actual developer experience.

auq-n is a meditation on modern labor conditions expressed through computational constraints. Every program is a negotiation between output and exhaustion, productivity and survival.

There is **no winning—only** degrees of making it through.

### Key Innovations

**Stress-Aware Execution Model**  
Every instruction carries an explicit stress cost, reflecting its cognitive complexity. Programs must manage accumulated stress or face termination—much like developers must manage burnout in real-world scenarios.

**Productivity Metrics**  
The runtime enforces minimum throughput requirements (2.5 instructions/second), ensuring programs maintain “acceptable” output levels. This creates a dual-constraint optimization problem unique to auq-n.

**Temporal Realism**  
Instructions execute with realistic delays proportional to their complexity. A mul operation genuinely takes longer than print, reflecting the actual cognitive overhead of mathematical operations.

-----

## Why auq-n?

Traditional programming languages ignore the human element. They assume infinite cognitive resources, unlimited focus, and sustained productivity. This is **unrealistic**.

auq-n addresses this gap by:

- Making cognitive costs **explicit** and **measurable**
- Enforcing resource management at the language level
- Requiring developers to balance multiple competing constraints
- Providing a more **honest** model of computational work

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
|`breathe.` |-20          |1.00s         |
|`rejuv!`   |-40          |1.80s         |

Higher-complexity operations (multiplication, division) carry greater stress costs, reflecting their cognitive overhead.

### Stress Mitigation

The language provides two stress-reduction primitives:

- `breathe.` — Moderate stress reduction with moderate time cost
- `rejuv!` — Significant stress reduction with significant time cost

Strategic use of these primitives is essential for program completion.

### Productivity Requirements

Programs must maintain a minimum throughput of **2.5 instructions per second**. Excessive use of stress-reduction primitives can cause productivity to fall below this threshold, resulting in termination.

-----

## Getting Started: Your First Loop

### Attempt 1: Basic Loop
```
set counter, 0
set max, 5

loop:
    add counter, 1
    print counter
    compare counter, max, loop
```

Output:
```
1.0
2.0
💀 BURNOUT at line 6

    Reason: Overthinking.
    Last thought: "compare counter, max, loop"
    Final stress level: 58 / 50

    You could've prevented this... stupid mf.
    Consider: working smarter, not harder.
```
**Analysis**: The program burned out after 2 iterations. Too much work, not enough recovery.

-----

### Attempt 2: Adding Self-Care

*“Have you tried just… breathing?”* — Management
```
set counter, 0
set max, 5

loop:
    add counter, 1
    print counter
    compare counter, max, loop
    breathe.
```

Output:
```
1.0
2.0
3.0
4.0
5.0
6.0
7.0
8.0
9.0
10.0
💀 BURNOUT at line 5

     Reason: Mild strain.
     Last thought: "print counter"
     Final stress level: 50 / 50

     You could've prevented this... stupid mf.
     Consider: working smarter, not harder.
```

**Analysis**: OOF--close enough. Burnouts usually creep in even when you think you're doing the right things. The self-care was there, but the workload never actually decreased.

-----

### Attempt 3: More Self-Care

*“Try breathing twice! Self-care is important.”* — HR

```
set counter, 0
set max, 10

loop:
    breathe.
    add counter, 1
    print counter
    breathe.
    compare counter, max, loop
```

Output:
```
📉 FIRED!!! at line 4

    Last thought: "breathe."
    Productivity: 2.497 instructions/sec
    Company minimum: 2.5 instructions/sec

    Such a lazy bum. Pack your variables and exit.
    Consider: working harder, not smarter.
```
Analysis: The program was terminated for insufficient productivity. Too much rest caused throughput to fall below minimum requirements.

-----

## Advanced Techniques

### Productivity Padding

Sometimes maintaining throughput requires... **creative solutions**.

```
set counter, 0
set max, 10

loop:
    add counter, 0      ; look busy
    add counter, 0      ; look busy
    breathe.
    add counter, 1
    print counter
    breathe.
    compare counter, max, loop
```

Output:
```
1.0
2.0
3.0
4.0
5.0
6.0
7.0
8.0
9.0
10.0
[ge lng] ✅ Program completed successfully

            Final stress: 2 / 50
            Final productivity: 2.615 instructions/sec

            Congratulations on surviving your job!
            Your reward: another job to run. These processes ain't gonna run themselves!
```

**Analysis**: By inserting a mathematically neutral operation (`add counter, 0`), we maintain productivity metrics while managing stress levels.

> 💡 Pro tip: Operations that don’t change program state still count toward throughput. This is not a bug—it’s **by design**.

### Best Practices

#### ✅ DO:

- Monitor your stress levels
- Balance work with strategic rest periods
- Use low-stress operations when possible
- Consider productivity padding when necessary

#### ❌ DON’T:

- Chain multiple `mul`/`div` operations
- Neglect self-care entirely
- Over-rest (productivity penalties apply)
- Expect the system to be fair

## Language Reference

### Arithmetic Operations
```
set x, 10
add x, 5        # x = 15
sub x, 3        # x = 12
mul x, 2        # x = 24
div x, 4        # x = 6
```

### Control Flow
```
compare x, 10, less_than_label
jump always_label

less_than_label:
    print 
```

### Output
```
print x
print 42
```

### Stress Management
```
breathe.         # -20 stress, 1.0s
rejuv!          # -40 stress, 1.8s
```

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
```
breathe.
breathe.
```

# Consider:
```
rejuv!
```

### Stress Budgeting

Complex operations (`mul`, `div`) should be “budgeted” within a program’s stress capacity:
```
set x, 5
mul x, 3        # +15 stress
breathe.         # -20 stress (net: -5)
```

-----

## Technical Specifications

**Paradigm**: Imperative, stress-managed  
**Typing**: Dynamic (float-based)  
**Execution**: Interpreted with real-time delays  
**Resource Model**: Dual-constraint (stress + productivity)  
**Turing Completeness**: Theoretically complete; practically constrained

-----

## Implementation Notes

auq-n is implemented in Python 3.10+ and uses pattern matching for instruction dispatch. The runtime maintains three primary state variables:

- `sc` — Stress counter
- `productivity` — Instructions per second
- `pc` — Program counter

Execution continues until program completion or constraint violation.

-----

## Research Directions

auq-n opens several areas for future investigation:

1. **Computational Complexity Under Stress Constraints**  
   What is the class of problems solvable within stress/productivity bounds?
1. **Optimal Stress Management Strategies**  
   Can we formalize patterns for stress-efficient algorithms?
1. **Language Extensions**  
   Could team-based stress pooling or variable stress costs enable new patterns?
1. **Empirical Developer Experience**  
   Does programming in auq-n affect developer awareness of cognitive load?

-----
## FAQ

### Is this an esoteric programming language?

No. auq-n is a **serious programming language** with a well-defined execution model and formal semantics.

The term “esoteric” implies novelty for novelty’s sake. auq-n introduces stress-based resource management because traditional languages **fail to model real computational constraints**. Dismissing innovations as “esoteric” simply because they challenge conventional paradigms is reductive.

If explicit resource management (memory, CPU cycles) is considered legitimate, why not cognitive resource management? auq-n takes the logical next step.

### Why do programs “burnout” or get “fired”?

These are technical terms describing constraint violations:

- `BURNOUT` — Stress threshold exceeded (analogous to stack overflow)
- `FIRED` — Productivity requirement not met (analogous to timeout)

The terminology reflects the nature of the constraints being modeled. We could have used `STRESS_OVERFLOW` and `THROUGHPUT_VIOLATION`, but the current terms are more semantically clear.

### Isn’t this just making programming artificially harder?

No. auq-n makes **existing difficulty explicit**.

Developers already manage cognitive load, context switching, and productivity pressure. Traditional languages simply ignore these costs. auq-n formalizes them, enabling:

- Better awareness of computational costs
- Explicit optimization strategies
- More realistic performance modeling

“Artificially harder” suggests these constraints are invented. They’re not—they’re **observed and formalized**.

### Why would anyone use this?

auq-n is designed for:

- **Educational contexts** — Teaching resource management under multiple constraints
- **Research applications** — Studying stress-bounded computation
- **Cognitive load modeling** — Simulating developer experience
- **Algorithmic challenges** — Solving optimization problems with novel constraints

Additionally, developers report that programming in auq-n increases awareness of cognitive costs in their primary language work.

### Can I disable stress tracking?

No. Stress tracking is fundamental to auq-n’s execution model. Disabling it would be equivalent to disabling type checking in a statically-typed language—it removes core functionality.

If you need a language without stress constraints, traditional languages remain available. Use those, duh.

### What about `add x, 0`? Isn’t that a “cheat”?

There are no “cheats” in auq-n—only strategies.

Neutral operations maintain throughput metrics while managing stress. This is a valid optimization technique within the language’s constraint model.

Real-world parallel: Strategic meeting scheduling to demonstrate productivity while managing actual workload. The language reflects reality.

### Is auq-n Turing complete?

Theoretically, yes—auq-n has all necessary computational primitives (arithmetic, conditional branching, loops).

Practically, Turing completeness is constrained by stress/productivity bounds. Some problems that are theoretically computable may be practically unsolvable within constraint limits.

This is not a limitation—it’s an **accurate model**. Not all theoretically solvable problems are practically solvable given real-world resource constraints.

### Who is this for?

auq-n is for developers interested in:

- Alternative computational models
- Resource-aware programming
- Cognitive load formalization
- Realistic constraint modeling

If you believe programming languages should model the full context of computation—including human factors—auq-n is for you.

### Is this a joke?

auq-n is a **serious exploration** of stress-based resource management in programming languages.

That it challenges assumptions about what programming languages should model does not make it a joke. Many innovations were initially dismissed before gaining acceptance.

We invite you to engage with auq-n’s ideas on their merits rather than through dismissive categorization.

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
- Contemporary art installations that speak to us like [Can't Help Myself](https://en.wikipedia.org/wiki/Can%27t_Help_Myself_(Sun_Yuan_and_Peng_Yu))
