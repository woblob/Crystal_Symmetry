import os
import shutil

def create_dirs(base_path, dirs):
    for d in dirs:
        os.makedirs(os.path.join(base_path, d), exist_ok=True)

def main():
    # Create directory structure
    dirs = [
        'krysztalki/core',
        'krysztalki/io',
        'krysztalki/utils',
        'krysztalki/cli',
        'tests/unit',
        'tests/integration',
        'docs/api',
        'docs/user_guide'
    ]

    create_dirs('.', dirs)

    # Move files to appropriate locations
    moves = [
        ('krysztalki/SYMfunc.py', 'krysztalki/core/symmetry.py'),
        ('krysztalki/cif_parsing.py', 'krysztalki/io/cif.py'),
        ('krysztalki/main.py', 'krysztalki/cli/main.py'),
        ('krysztalki/task_manager.py', 'krysztalki/utils/task_manager.py')
    ]

    for src, dst in moves:
        if os.path.exists(src):
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.move(src, dst)

    # Create necessary __init__.py files
    init_dirs = [
        'krysztalki/core',
        'krysztalki/io',
        'krysztalki/utils',
        'krysztalki/cli',
        'tests/unit',
        'tests/integration'
    ]

    for d in init_dirs:
        init_file = os.path.join(d, '__init__.py')
        if not os.path.exists(init_file):
            open(init_file, 'a').close()

if __name__ == '__main__':
    main() 