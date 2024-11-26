# Advent of Code 2024 Workspace

This workspace is set up to help you solve Advent of Code 2024 challenges efficiently using Python, VSCode, and a Makefile. Below, you'll find instructions on how to use the Makefile, the `create_day` script, and the VSCode enhancements for debugging and running solutions.

---

## **Using the Makefile**

The `Makefile` includes commands to streamline running and setting up your Advent of Code solutions.

### Available Targets

1. **Run a Day's Solution**
   - **Prompt-Based Execution**:
     ```bash
     make run
     ```
     - This will prompt you to enter the day number (e.g., `01` or `02`).
     - It will then execute the corresponding Python file from the `2024/day_<day>/` folder.

   - **Direct Execution for a Specific Day**:
     ```bash
     make run_day DAY=<day_number>
     ```
     - Replace `<day_number>` with the day number (e.g., `01` or `02`).
     - Example:
       ```bash
       make run_day DAY=03
       ```

2. **Create a New Day's Folder and Files**
   - To set up files for a new day:
     ```bash
     make create_day
     ```
     - This will prompt you for the day number (e.g., `01` or `02`).
     - It will:
       - Create a folder: `2024/day_<day_number>/`.
       - Copy the `day_template.py` to `day_<day_number>.py`.
       - Create empty input files: `day_<day_number>_input.txt` and `day_<day_number>_test_input.txt`.
     - Example:
       ```bash
       make create_day
       ```
       Enter `05` when prompted, and it will set up:
       ```
       2024/day_05/
       ├── day_05.py
       ├── day_05_input.txt
       ├── day_05_test_input.txt
       ```

---

## **Using the `create_day.sh` Script (Optional)**

If you prefer to use a Bash script instead of the Makefile for creating days, you can use `create_day.sh`.

1. Ensure the script is executable:
   ```bash
   chmod +x 2024/create_day.sh
   ```

2. Run the script:
   ```bash
   ./2024/create_day.sh <day_number>
   ```
   Replace `<day_number>` with the desired day (e.g., `01` or `02`).

3. The script will create the same files as the Makefile target:
   ```
   2024/day_<day_number>/
   ├── day_<day_number>.py
   ├── day_<day_number>_input.txt
   ├── day_<day_number>_test_input.txt
   ```

---

## **VSCode Enhancements**

We've made several changes to VSCode to improve the workflow for Advent of Code:

### Debugging with `launch.json`
- Location: `.vscode/launch.json`
- Debugging Configuration:
  ```json
  {
    "version": "0.2.0",
    "configurations": [
      {
        "name": "Python: Current File",
        "type": "python",
        "request": "launch",
        "program": "${file}",
        "console": "integratedTerminal",
        "cwd": "${workspaceFolder}/2024"
      }
    ]
  }
  ```
- How to Use:
  1. Open any Python file for a specific day (e.g., `2024/day_01/day_01.py`).
  2. Go to the **Run and Debug** tab (`Ctrl+Shift+D`).
  3. Select **"Python: Current File"** from the dropdown.
  4. Hit `F5` to start debugging.

### Task Runner with `tasks.json`
- Location: `.vscode/tasks.json`
- Task Configuration:
  ```json
  {
    "version": "2.0.0",
    "tasks": [
      {
        "label": "Run Any Day",
        "type": "shell",
        "command": "python 2024/day_${input:day_number}/day_${input:day_number}.py",
        "problemMatcher": [],
        "inputs": [
          {
            "id": "day_number",
            "type": "promptString",
            "description": "Enter the day number (e.g., 01, 02)"
          }
        ]
      }
    ]
  }
  ```
- How to Use:
  1. Open the Command Palette (`Ctrl+Shift+P`).
  2. Search for `Tasks: Run Task`.
  3. Select **"Run Any Day"**.
  4. Enter the day number when prompted (e.g., `03`).

---

## **Folder Structure**

Here’s how your workspace is structured:
```
AdventOfCode/
├── 2024/
│   ├── day_template.py
│   ├── day_01/
│   │   ├── day_01.py
│   │   ├── day_01_input.txt
│   │   ├── day_01_test_input.txt
│   ├── create_day.sh
├── .vscode/
│   ├── launch.json
│   ├── tasks.json
├── Makefile
```

---

## **Future Enhancements**
- Add tasks for linting (`flake8`) or formatting (`black`).
- Integrate testing with `pytest`.
- Automate cleanup or archiving of solved days.

---

Enjoy solving the puzzles, and may your Advent of Code season be merry and bug-free! 🎄💻
