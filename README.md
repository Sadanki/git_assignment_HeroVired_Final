# git_assignment_HeroVired_Final
# 📌 **CalculatorPlus - Git Assignment**

## 📖 **Overview**
Welcome to the **CalculatorPlus** project! This Python application provides basic arithmetic operations such as addition, subtraction, multiplication, and division. Your task is to implement a new feature: **square root calculation**. 🚀

## 📂 **Repository Details**
- Repository Name: `git_assignment_HeroVired_Final`
- Primary Branch: `main`
- Development Branch: `dev`

---

## ✅ **Q1: Implementing Square Root Feature**
### 🔨 **Steps to Follow**

### 📌 **Step 1: Create a Repository and Branch**
1. Create a repository named **git_assignment_HeroVired_Final**.
2. Create a branch named `dev` from `main`.
3. Add the following Python code:

```python
import math

class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        return a / b
    
    # TODO: Implement the square root function
    # def square_root(self, x):
    #     return math.sqrt(x)
```

4. Uncomment and implement the `square_root` function.

```python
    def square_root(self, x):
        return math.sqrt(x)
```

5. Run the following test cases:

```python
if __name__ == "__main__":
    calculator = Calculator()
    print(f"Square root of 25 = {calculator.square_root(25)}")
```

### 📌 **Step 2: Merge and Release Version 1**
- Merge the `dev` branch into `main`.
- Create a **Version 1 Release**.

### 📌 **Step 3: Collaborate & Fix Bugs**
- Add a collaborator to the repository.
- Create a new branch `feature/sqrt` from `main`.
- Uncomment the square root function code.

### 📌 **Step 4: Bug Fixing in `divide` Function**
- Switch to `dev` branch and fix the divide function:

```python
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
```

- Merge the fix into `feature/sqrt`.
- Request a **code review** from a team member.
- Merge `feature/sqrt` into `dev` and finalize **Version 2 Release**.

---

## ✅ **Q2: Handling Large Binary Files with Git LFS**
For handling **large binary files**, follow these steps:

### 📌 **Step 1: Initialize Git LFS**
```bash
git lfs install
git checkout -b lfs
git lfs track "*.mp4"
```

### 📌 **Step 2: Add Large Files**
- Upload any **large file (200MB+)**
```bash
git add big_file.mp4
git commit -m "Added large file to Git LFS"
git push origin lfs
```

### 📌 **Step 3: Clone & Verify**
- Clone the repository on another machine:
```bash
git clone <repo_link>
```
- Verify the large files are correctly downloaded.

---

## ✅ **Q3: Geometry Calculator with Git Stash**

### 📌 **Step 1: Create a New Branch**
```bash
git checkout -b geometry-calculator
```

### 📌 **Step 2: Implement Geometry Functions**
```python
import math

class GeometryCalculator:
    def calculate_circle_area(self, radius):
        return math.pi * radius ** 2

    def calculate_rectangle_area(self, length, width):
        return length * width
```

### 📌 **Step 3: Stash Changes**
```bash
git stash
```

### 📌 **Step 4: Work on Another Feature**
```bash
git checkout -b feature/rectangle-area
```

- Retrieve stashed changes:
```bash
git stash pop
```

- Finalize implementations, commit, and push changes.

### 📌 **Step 5: Merge Features**
- Open **Pull Requests** to `dev` branch.
- Get **Code Review & Approval**.
- Merge branches into `main` and finalize the **Version Release**.



