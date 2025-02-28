# 🎯 **Git Assignment - Hero Vired**  

Welcome to the **Git Assignment Repository**! 📌 This project covers **multiple Git and Python development tasks**, including **branch management, feature development, bug fixes, Git LFS, and pull request handling.** Let's dive in! 🎉  

## 📂 **Repository Name:** `git_assignment_HeroVired`  

## 📌 **Table of Contents**  
- 🔹 [Q1: CalculatorPlus - Square Root Feature](#-q1-calculatorplus---square-root-feature)  
- 🔹 [Q2: Git LFS - Handling Large Files](#-q2-git-lfs---handling-large-files)  
- 🔹 [Q3: Geometry Calculator - Area Calculations](#-q3-geometry-calculator---area-calculations)  
- 🔹 [🚀 Workflow Summary](#-workflow-summary)  

---

## 🧮 **Q1: CalculatorPlus - Square Root Feature**  

### **📌 Task Overview**  
We are enhancing the `CalculatorPlus` application by adding support for **square root calculations** and fixing a **division bug**.

### **📂 Steps to Follow**  
1️⃣ **Create a GitHub repository** named `git_assignment_HeroVired`.  
2️⃣ **Create a `dev` branch** and add the following initial code:  

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

    # TODO: Implement the following function to calculate the square root
    # def square_root(self, x):
    #     return math.sqrt(x)
```

3️⃣ **Implement the `square_root()` method** by uncommenting the function.  
4️⃣ **Create a branch `feature/sqrt`** and add the square root functionality.  
5️⃣ **Fix the `divide()` method** to prevent division by zero:  

```python
def divide(self, a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
```

6️⃣ **Push changes, create a pull request, and merge into `dev`**  
7️⃣ **Test thoroughly in `dev` before merging to `main`**  
8️⃣ **Create a `Version 2` release 🎉**  

---

## 📁 **Q2: Git LFS - Handling Large Files**  

### **📌 Task Overview**  
We need to handle **large binary files** efficiently using **Git LFS (Large File Storage)**.

### **📂 Steps to Follow**  
1️⃣ **Create a branch `lfs`** in the repository.  
2️⃣ **Install Git LFS** (if not installed):  
   ```sh
   git lfs install
   ```
3️⃣ **Track large files**:  
   ```sh
   git lfs track "*.zip" "*.mp4" "*.psd"
   ```
4️⃣ **Upload a file over `200MB`** and push changes.  
5️⃣ **Clone the repo on another machine to verify that LFS downloads files correctly.**  

---

## 📏 **Q3: Geometry Calculator - Area Calculations**  

### **📌 Task Overview**  
We're building a **Geometry Calculator** that calculates the **area of a circle and rectangle**. The challenge is to use `git stash` to manage multiple features effectively.  

### **📂 Steps to Follow**  
1️⃣ **Create a new branch `geometry-calculator`**.  
2️⃣ **Create feature branches** for different area calculations:  
   - `feature/circle-area`  
   - `feature/rectangle-area`  
3️⃣ **Use `git stash` to save incomplete changes before switching branches**:  
   ```sh
   git stash
   git checkout feature/rectangle-area
   ```
4️⃣ **Retrieve stashed changes when switching back**:  
   ```sh
   git stash pop
   ```
5️⃣ **Complete both features and commit them separately.**  
6️⃣ **Create pull requests (PRs) to `dev` branch.**  
7️⃣ **After review & approval, merge into `main` and release `Version 3` 🎉**  

---

## 🚀 **Workflow Summary**  

| Task 🏆                | Branch Name 🌿          | Action 🚀 |
|----------------------|----------------------|---------|
| 📌 **Initialize Repo** | `main` | Create Repo |
| 🔀 **Create Dev Branch** | `dev` | Work on `dev` |
| 🧮 **CalculatorPlus** | `feature/sqrt` | Implement `sqrt()` |
| 🐞 **Fix Division Bug** | `feature/sqrt` | Fix `divide()` |
| 🔁 **Merge Features** | `dev → main` | Version 2 Release |
| 🗂️ **Git LFS Setup** | `lfs` | Track Large Files |
| 🔄 **Geometry Calculator** | `geometry-calculator` | Calculate Areas |
| 🎯 **Final PRs & Merges** | `dev → main` | Version 3 Release |

---

## 🎉 **Congratulations! You're Done!**  
This repository is now fully functional with **multiple features, fixes, and Git best practices!** 🎯💡  

**Happy Coding! 🚀🔥**
