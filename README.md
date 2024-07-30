# MSDie: Multi-Sided Die Class

## Overview

Ever wanted to create your own multi-sided die like the ones you use in board games? This Python program lets you do just that! With the `MSDie` class, you can make dice with any number of sides, roll them to get a random number, and set or check the current value showing on the die. There's also a simple example included to show you how it works.

## How It Works

### MSDie Class

1. **Initialization (`__init__`):**
   - When you create a die, you specify how many sides it has, and it starts with the value 1.

2. **Rolling the Die (`roll`):**
   - The `roll` method changes the die's value to a random number between 1 and the number of sides.

3. **Getting the Current Value (`getValue`):**
   - The `getValue` method lets you see the current number showing on the die.

4. **Setting the Face Value (`setValue`):**
   - The `setValue` method allows you to manually set the die to a specific number.

### Example Usage

The `main` function in the code shows you how to create a 6-sided die, set its value, roll it, and then get the current value. The result is printed out so you can see it in action.

## Key Concepts Covered

- **Class Definition:** Learn how to create a class with methods and attributes.
- **Initialization:** Understand how to set up an object's initial state with the `__init__` method.
- **Randomization:** Use the `randrange` function to generate random values.
- **Encapsulation:** Create methods to interact with the object's data (`roll`, `getValue`, and `setValue`).
- **Example Usage:** See a simple program demonstrating how to use the class.
