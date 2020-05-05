from scripts.create_solved_files import main as create_solved_files
from scripts.generate_solution_files import main as generate_solution_files
from scripts.generate_readme import main as generate_readme


if __name__ == '__main__':
    create_solved_files()
    generate_solution_files()
    generate_readme()
