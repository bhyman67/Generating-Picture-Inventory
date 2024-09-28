# Picture Inventory Generator

This Python script automates the process of creating an inventory of image files. It searches for all picture files in a specified directory and outputs their names, locations, and clickable links into an Excel file. I used GitHub Copilot to help me develop this. 

## Features
- Traverses through all picture files in a directory (and subdirectories).
- Generates an Excel file listing each file's name, full path, and a hyperlink to open it.
- Supports images in common formats (JPEG, PNG, etc.).
- Handles large directories efficiently.

## Requirements
- Python 3.x
- Libraries: `os`, `openpyxl`

## Usage
1. Clone this repository:
    ```bash
    git clone https://github.com/bhyman67/Generating-Picture-Inventory.git
    ```
2. Install required libraries:
    ```bash
    pip install openpyxl
    ```
3. Run the script:
    ```bash
    python Generate_Picture_Inventory.py
    ```
4. Follow the prompts to specify the directory for scanning and where to save the Excel file.

## Output
The generated Excel file will include:
- Image filenames.
- Full file paths.
- Clickable links to both the file and directory.

## Example

![Screenshot](./Screenshot%202024-09-15%20102243.png)

<p align="right">Click <a href="https://github.com/bhyman67/Generating-Picture-Inventory">here</a> to view the code in this project's repository<p>
