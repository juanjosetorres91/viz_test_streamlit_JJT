import nbformat
import shutil
import os

def reorder_notebook(notebook_path, new_order):
    # Backup
    backup_path = notebook_path.replace('.ipynb', '_backup.ipynb')
    shutil.copy2(notebook_path, backup_path)
    print(f"Backed up to {backup_path}")

    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    # Validate indices
    total_cells = len(nb.cells)
    if max(new_order) >= total_cells:
        print(f"Error: Index {max(new_order)} out of bounds (Total: {total_cells})")
        return

    # Check if we are using all cells (optional, but good for safety)
    if len(set(new_order)) != total_cells:
        print(f"Warning: New order has {len(set(new_order))} unique cells, but original had {total_cells}. Some cells might be dropped.")
        missing = set(range(total_cells)) - set(new_order)
        print(f"Missing indices: {missing}")

    # Reorder
    new_cells = [nb.cells[i] for i in new_order]
    nb.cells = new_cells

    with open(notebook_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)
    
    print("Notebook reordered successfully.")

if __name__ == "__main__":
    notebook_path = r"c:/Users/christian.vasquez/Documents/antigravity/storytelling/storytelling_executive.ipynb"
    # Order: [0-5, 13-14 (Geo), 17-18 (HIV), 6-8 (Analysis), 15-16 (Scatter), 9-11 (Climax), 12 (Res), 19 (Conc)]
    new_order = [0, 1, 2, 3, 4, 5, 13, 14, 17, 18, 6, 7, 8, 15, 16, 9, 10, 11, 12, 19]
    reorder_notebook(notebook_path, new_order)
