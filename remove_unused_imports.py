import os
import subprocess

# Path to your Django project root folder
PROJECT_ROOT = './'  # Adjust if needed

def remove_unused_imports(file_path):
    """Run autoflake on a single file to remove unused imports."""
    print(f"Processing {file_path}")
    try:
        subprocess.run([
            'autoflake',
            '--in-place',
            '--remove-unused-variables',
            '--remove-all-unused-imports',
            file_path
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error processing {file_path}: {e}")

def main():
    for root, _, files in os.walk(PROJECT_ROOT):
        for file in files:
            if file.endswith('.py'):
                full_path = os.path.join(root, file)
                remove_unused_imports(full_path)

if __name__ == '__main__':
    main()
