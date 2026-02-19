<div align="center">

# 🐍 Python Programming Mastery

### 🚀 Structured Learning • Clean Code • Strong Fundamentals

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Status](https://img.shields.io/badge/Status-Actively%20Developing-success?style=for-the-badge)
![Focus](https://img.shields.io/badge/Focus-Core%20Concepts-orange?style=for-the-badge)
![Discipline](https://img.shields.io/badge/Approach-Structured%20Learning-blueviolet?style=for-the-badge)


</div>

---

# 🏗 About This Repository

This repository represents a **structured and engineering-focused journey** toward mastering Python.

The emphasis is not merely on syntax —  
but on developing:

- Strong computational thinking  
- Clean, maintainable code practices  
- Deep conceptual understanding  
- Scalable problem-solving skills  
- Industry-ready engineering discipline  

This repository is built with a **long-term systems design mindset**. 

---

## 🌿 Branch Strategy

| Branch | Purpose |
|--------|----------|
| `main` | Stable and clean version |
| `core-python-practice` | Structured concept-wise learning |


---

## 📂 Repository Structure

```
Python-Programming
│
├── core-python-practice/
│   │
│   ├── 01_programming_elements/
│   ├── 02_control_flow/
│   ├── 03_iteration_and_loops/
│   ├── 04_functions_practice/
│   ├── 05_lists_and_tuples/
│   ├── 06_lists_and_tuples_level_2/
│   ├── 07_Sets_and_Dictionaries/
│
└── README.md
```

---

# 📅 Week 1 – Python Foundations

### Day 1 — Programming Elements

**Concepts Implemented**

- Variables & Naming Conventions  
- Primitive Data Types (`int`, `float`, `str`, `bool`)  
- Type Checking (`type()`)  
- Explicit Type Casting  
- Arithmetic Operators  
- Boolean Evaluation Model  
- Operator Precedence  
- f-String Formatting  

**Key Engineering Insights**

- Python uses dynamic typing with runtime binding.
- `bool` is a subclass of `int` (True → 1, False → 0).
- `input()` always returns `str` — explicit conversion required.
- Expression evaluation order affects correctness.
- Python supports tuple-based variable swapping (no temp variable).

---

### Day 2 — Control Flow

**Concepts Implemented**

- Conditional Statements (if, if-else, if-elif-else)
- Comparison Operators (==, !=, >, <, >=, <=)
- Logical Operators (and, or, not)
- Nested Conditional Structures
- Multi-branch Decision Logic
- Short-circuit Evaluation
- Operator Precedence in Conditions
- Real-world Rule Implementation (Grade system, Leap year logic, Calculator logic)

**Key Engineering Insights**

- Control flow determines execution path based on runtime conditions.
- Logical operators must be used instead of bitwise operators (and vs &).
- Condition order impacts correctness and edge-case handling.
- Python evaluates conditional blocks top-down with short-circuit behavior.
- Clean indentation defines logical structure and execution scope.
- Complex conditions should prioritize clarity over compactness.
- Equality edge cases must be checked deliberately in multi-variable comparisons.


---

### Day 3 — Iteration & Loop Constructs

**Concepts Implemented**

- for Loop (bounded iteration)
- while Loop (condition-driven iteration)
- range(start, stop, step)
- Loop Initialization & Termination
- Accumulator Pattern (sum, factorial, counters)
- break and continue
- Nested Loops
- Pattern Printing
- Mathematical Problems (Prime, Fibonacci, Reverse Number)

**Key Engineering Insights**

- Iteration enables scalable and repeatable execution.
- Use for when count is known, while when condition controls execution.
- Improper loop conditions may cause infinite loops.
- Accumulators are fundamental for aggregation logic.
- break improves efficiency via early termination.
- Nested loops increase time complexity (often O(n²)).
- Prime checks can be optimized to √n.
- Loop problems build core algorithmic thinking skills.

---


### Day 4 — Functions & Modular Programming

**Concepts Implemented**

- Function Definition & Calling (`def`)
- Parameters & Arguments (Positional & Default)
- Return Statement (Single & Multiple Values)
- Built-in vs User-defined Functions
- Local vs Global Scope
- Function Reusability & Modularization

**Key Engineering Insights**

- Functions enable reusable, maintainable, and testable code.
- Abstraction separates *what* from *how*.
- Local scope prevents side effects.
- Modular code replaces repetitive scripting logic.
- Functions form the foundation of scalable programs.

---

### Day 5 — Lists & Tuples (Core Data Structures)

**Concepts Implemented**

- List Creation & Indexing
- Negative Indexing
- List Slicing
- List Methods (append(), insert(), remove(), pop(), sort(), reverse())
- Iterating Over Lists
- Nested Lists
- Tuple Creation & Immutability
- Tuple Packing & Unpacking
- List vs Tuple Differences

**Key Engineering Insights**

- Lists are mutable and suited for dynamic data manipulation.
- Tuples are immutable and safer for fixed datasets.
- Indexing and slicing enable controlled data access.
- List methods modify objects in place (memory-efficient operations).
- Tuples provide performance and integrity advantages.
- Choosing the right data structure impacts readability and efficiency.
- Nested lists introduce multi-dimensional data handling.
- Proper iteration patterns improve clarity and maintainability.

---

### Day 6 — Lists & Tuples (Intermediate Problem Solving)

**Concepts Implemented**

- Finding Second Largest Element (Without Built-in Sorting)
- Palindrome Check Using Two-Pointer Technique
- List Rotation by K Positions
- Pair Sum Problem (Unique Pairs)
- Flattening Nested Lists (One Level)
- Manual Frequency Counting (Without `collections`)
- Removing All Occurrences of an Element
- Matrix Transpose Using Nested Lists
- Sorting List of Tuples by Custom Key
- Detecting Duplicate Elements (Without Repetition in Output)

**Key Engineering Insights**

- Tracking state with variables improves algorithm clarity.
- Two-pointer and slicing strategies reduce unnecessary complexity.
- Avoiding built-in helpers strengthens core logic development.
- Hash-based lookups optimize pair and frequency problems to O(n).
- Controlled mutation prevents unintended side effects.
- Nested iteration requires careful boundary management.
- Matrix problems strengthen multi-dimensional indexing skills.
- Custom sorting demonstrates function-based comparison control.
- Duplicate detection reinforces set-based reasoning and uniqueness handling.
- Understanding time complexity (O(n), O(n²)) guides better implementation decisions.

---

### Day 07 — Sets & Dictionaries (Hash-Based Problem Solving)

**Concepts Implemented**

- Removing Duplicates Using Set
- Set Operations (Union, Intersection, Difference)
- Anagram Check Using Dictionary
- Frequency Counting with Hash Map
- First Non-Repeating Element
- Two Sum Problem (Optimized with Hashing)
- Grouping Data Using Dictionary
- Merging Dictionaries
- Detecting Duplicates Using Set Tracking
- Inverting Dictionary (Key-Value Swap)

**Key Engineering Insights**

- Sets provide average O(1) time complexity for membership checks.
- Dictionaries enable constant-time lookups and efficient state tracking.
- Hashing eliminates the need for nested loops in many problems.
- The `get()` method simplifies frequency counting logic.
- Proper key management prevents collisions and logical errors.
- Using sets ensures uniqueness without additional validation logic.
- Dictionary-based solutions scale better than brute-force approaches.
- Data modeling (choosing key-value structure) improves clarity.
- Hash maps are foundational for optimizing search and pairing problems.
- Understanding time-space trade-offs is critical in hash-based design.

---


# 🧠 Engineering Principles Applied

- Code readability over clever shortcuts
- Explicit over implicit conversions
- Concept-first learning approach
- Directory-level modular organization
- Incremental progression

---

## 🛠 Tech Stack

- 🐍 Python 3.x
- 🖥 VS Code
- 🌿 Git
- ☁ GitHub

---

# 🎯 Long-Term Objective

To achieve:

- Strong Data Structures & Algorithms proficiency
- Backend engineering readiness
- Clean architecture design capability
- Interview-level conceptual clarity
- Production-level code discipline

---

## 👨‍💻 Author

**Raj Bahadur Singh**  
B.Tech Computer Science  

---

## 📌 Repository Purpose

This repository is maintained strictly for:

- 📚 Structured learning
- 🔁 Concept revision
- 💼 Professional skill development
- 🚀 Long-term career growth

---

<div align="center">
  
### “Master fundamentals. Scale systems. Think like an engineer.”

</div>
