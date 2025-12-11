import nbformat
import sys

def dump_structure(notebook_path, output_path):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    with open(output_path, 'w', encoding='utf-8') as out:
        for i, cell in enumerate(nb.cells):
            content = cell.source[:100].replace('\n', ' ')
            out.write(f"Cell {i} [{cell.cell_type}]: {content}\n")

if __name__ == "__main__":
    notebook_path = r"c:/Users/christian.vasquez/Documents/antigravity/storytelling/storytelling_executive.ipynb"
    output_path = r"c:/Users/christian.vasquez/Documents/antigravity/storytelling/structure.txt"
    dump_structure(notebook_path, output_path)
