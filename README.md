# Super 30: Python Loops - Task 1

Practice tasks demonstrating Python loops, sequences, strings, and dictionary manipulations.

---

## Sample Inputs and Outputs

| Script | Description | Sample Input | Sample Output |
| :--- | :--- | :--- | :--- |
| `01_print_1_to_100.py` | Numbers 1 to 100 | *None* | `1 2 3 ... 99 100` |
| `02_even_numbers.py` | Even numbers 1 to 100 | *None* | `2 4 6 ... 98 100` |
| `03_odd_numbers.py` | Odd numbers 1 to 100 | *None* | `1 3 5 ... 97 99` |
| `04_multiplication_table.py` | Multiplication table up to 20 | `7` | `7 * 1 = 7 ... 7 * 20 = 140` |
| `05_sum_of_n_numbers.py` | Sum from 1 to n | `9` | `The total of the number is 45` |
| `06_factorial.py` | Factorial of n | `5` | `The factorial of the number is 120` |
| `07_divisible_by_three.py` | Multiples of 3 from list | *None* | `12 9 33 42 15` |
| `08_string_lengths.py` | Length of language strings | *None* | `the language is Python and its length is 6` ... |
| `09_dictionary_iteration.py` | Key-value pairs of student | *None* | `name Rahul`<br>`age 22`<br>`course Data Science`<br>`city Bangalore` |
| `10_count_vowels.py` | Vowel count in string | `Sanjeet` | `The count of vowel in string is: 3` |
| `11_reverse_string.py` | Reverse string without slicing | `ketan` | `natek` |
| `12_find_largest.py` | Max item without `max()` | *None* | `The largest of list is: 11` |

---

 Detailed Logic & Approaches

1. Print Numbers 1 to 100 (`01_print_1_to_100.py`)
Approach:** Loop construct `for i in range(1, 101):` iterates from starting value `1` up to `100` (`stop - 1`).
Logic:** Used `end=' '` inside the `print()` function to output all numbers inline horizontally separated by spaces instead of printing on a new line.

---

2. Even Numbers from 1 to 100 (`02_even_numbers.py`)
  Approach:** Iterated through range `1` to `101` and tested divisibility using the modulus operator (`%`).
 Logic:** Condition `i % 2 == 0` evaluates to true whenever a number has no remainder when divided by 2, identifying it as an even number.

---
 3. Odd Numbers from 1 to 100 (`03_odd_numbers.py`)
Approach:** Iterated through range `1` to `101`.
Logic:** Condition `i % 2 != 0` filters numbers that yield a remainder of `1` when divided by 2, identifying them as odd numbers.

---

4. Multiplication Table up to 20 (`04_multiplication_table.py`)
   Approach:** Took dynamic integer input from user using `int(input())`.
 Logic:** Ran a loop `for i in range(1, 21):` to multiply the user input with multiplicands `1` through `20`, formatting the output with formatted string literals (`f-strings`).

---

 5. Sum of Numbers from 1 to N (`05_sum_of_n_numbers.py`)
 Approach:** Initialized an accumulator variable `total = 0`.
 Logic:** Iterated through sequence `range(1, n + 1)` and accumulated each step's value (`total = total + i`).

---

6. Factorial Calculation without Built-in Methods (`06_factorial.py`)
Approach:** Initialized a product accumulator `total = 1` (starting at 1 to prevent zero-multiplication issues).
 Logic:** Multiplied `total` iteratively by each value from `1` to `n` (`total = total * i`), simulating $n! = 1 \times 2 \times \dots \times n$.

---

7. Filter Numbers Divisible by 3 (`07_divisible_by_three.py`)
Approach:** Iterated directly across list elements (`for i in numbers:`).
Logic:** Evaluated remainder via `i % 3 == 0` to filter and print elements directly divisible by 3.

---

8. Language List & String Lengths (`08_string_lengths.py`)
Approach:** Traversed each item in the list of strings.
Logic:** Applied Python's built-in `len(item)` function to compute character counts dynamically per iteration.

---

9. Dictionary Key-Value Unpacking (`09_dictionary_iteration.py`)
Approach:** Used the `.items()` method on the dictionary object.
Logic:** Unpacked key-value pairs simultaneously into two iteration variables (`for key, value in student.items():`) and displayed both.

---

10. Count Vowels in a String (`10_count_vowels.py`)
 Approach:** Normalized user input to lowercase using `.lower()` to handle case-insensitivity.
 Logic:** Initialized a counter at 0. Looped through each character and checked membership against a vowel tuple `('a', 'e', 'i', 'o', 'u')` using the `in` operator.

---

11. Reverse String without Slicing or Built-ins (`11_reverse_string.py`)
   Approach:** Used a prepending string concatenation technique.
 Logic:** Started with an empty string `rev_str = ""`. For every incoming character, concatenated it at the beginning (`rev_str = char + rev_str`), reversing the order without using `[::-1]` or `reversed()`.

---

12. Find Largest Number without `max()` (`12_find_largest.py`)
 Approach:** Greedy tracking using a candidate variable initialized to the first element `largest = L[0]`.
 Logic:** Traversed the entire list comparing each element against `largest`. Whenever an element exceeded `largest` (`if i > largest:`), updated `largest = i`.
