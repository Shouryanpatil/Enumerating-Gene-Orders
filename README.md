# Enumerating Gene Orders

This project is a simple Python script that generates all possible permutations of the numbers from 1 to `n`, where `n` is a positive integer less than or equal to 7.

## 🧠 Problem Explanation
A **permutation** is just a way of arranging items. For example, the numbers `1 2 3` can be arranged in several different ways like `1 3 2` or `3 2 1`. If you have `n` different items, this program will:

1. Show you **how many** different ways they can be arranged.
2. Print **each** arrangement.

## 📥 Input
Set the value of `n` directly in the Python file. No external input files are required. Example:
```python
n = 3
```

## 📤 Output
For `n = 3`, the output will be:
```
6
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
```

## 🧪 How to Run
1. Make sure you have Python installed (version 3+).
2. Download or clone this repository.
3. Open the Python file and set your desired value of `n`.
4. Run the script:
```bash
python permutations.py
```

## 📂 Files
- `permutations.py`: Main script that generates and prints permutations.

## 📌 Constraints
- `n` must be an integer such that `1 <= n <= 7`.

