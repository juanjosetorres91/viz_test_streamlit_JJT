import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import os

def run_notebook(notebook_path):
    print(f"Executing {notebook_path}...")
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)

    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')

    try:
        ep.preprocess(nb, {'metadata': {'path': os.path.dirname(notebook_path)}})
        print("Notebook executed successfully.")
        
        # Save the executed notebook (with outputs)
        output_path = notebook_path.replace('.ipynb', '_executed.ipynb')
        with open(output_path, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)
        print(f"Executed notebook saved to {output_path}")

    except Exception as e:
        print(f"Error executing notebook: {e}")
        # Save partial execution
        output_path = notebook_path.replace('.ipynb', '_error.ipynb')
        with open(output_path, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)
        raise

if __name__ == "__main__":
    notebook_path = r"c:/Users/christian.vasquez/Documents/antigravity/storytelling/storytelling_executive.ipynb"
    run_notebook(notebook_path)
