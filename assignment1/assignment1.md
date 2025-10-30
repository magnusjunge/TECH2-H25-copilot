# TECH2 mandatory assignment #1

Deadline: September 19 at 16:00

## Random Password Generator

Passwords protect accounts and sensitive information. A good password should be hard to guess, contain a variety of character types, and be of sufficient length. In this assignment, you will write a Python program that generates a random password based on user input and following standard security rules.

## Program Requirements

Your program must:

1. Prompt for password length:

    * Ask the user to enter the desired password length.
    * The password length must be between 8 and 16 characters (inclusive).
    * If the user enters a number that is too small or too large, or a non-numeric input, display an error message and prompt the user again until they provide a valid input.

2. Generate the password

    The password must meet the following character requirements:

    * At least one lowercase letter: `a-z`
    * At least one uppercase letter: `A-Z`
    * At least one digit: `0-9`
    * At least one special character: `!@#$%^&*()-_=+`
    * The password cannot begin with a digit or a special character.

3. Display the Generated Password

    * Once a valid password has been generated, print it to the screen.

## Example Run

### Input/Output 
```
Enter the desired password length (8-16): 5
Error: Password length must be between 8 and 16 characters.
Enter the desired password length (8-16): 10
Generated password: G7d!apX4#s
```

## Implementation Tips

### `string` module

Use the `string` module to access character sets, e.g.:

| Python Code | Comment | Output String |
| :--- | :--- | :--- |
| `import string` | | |
| `string.ascii_lowercase` | | `'abcdefghijklmnopqrstuvwxyz'` |
| `string.ascii_uppercase` | | `'ABCDEFGHIJKLMNOPQRSTUVWXYZ'` |
| `string.digits` | | `'0123456789'` |

### `random` module

Use the `random` module for randomness, e.g.:

* `random.choice(sequence)`: Picks a random element
* `random.shuffle(list)`: Shuffles a list in place

## Submission Instructions

1. Submit your program as a Python script (.py) and not as a Jupyter notebook.
2. Explain and document your code with in-line comments (`#`) and larger comment blocks (`"""`).
3. Make sure that your program compiles without errors in the terminal.
    * If the code does not compile (or if the code is incomplete), this should be stated in the comments, and you should also explain what the issue is.
4. State the use of generative AI in the code and comments.
    * In case you have not used generative AI for assistance, this should also be stated.
5. Note that you are encouraged (but not required) to use self-defined functions in your program.