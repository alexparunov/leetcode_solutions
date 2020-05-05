import json
from pathlib import Path


def generate_files(solved_data: dict):
    print(f"Parsing total of {len(solved_data['solved_problems'])} files (problems data)")
    new_files = 0
    for prob in solved_data['solved_problems']:
        problem_id = prob['problem_id']
        title_slug = prob['title_slug']
        url = prob['url']
        full_file_path, directory_name = get_full_solution_file_path(problem_id, title_slug)

        Path(directory_name).mkdir(exist_ok=True)

        if not Path(full_file_path).exists():
            new_files += 1
            with open(full_file_path, 'w') as f:
                string_to_write = f"\"\"\"\n{url}\n\n\"\"\""
                f.write(string_to_write)

    print(f'Generated new {new_files} files')


def get_full_solution_file_path(problem_id, title_slug):
    digit, remainder = divmod(problem_id, 100)
    directory_range = f'{max(1, digit * 100)}-{(digit + 1) * 100}'

    directory_name = '../src/' + directory_range
    file_name = f'_{problem_id}_{title_slug}.py'
    full_file_path = directory_name + '/' + file_name

    return full_file_path, directory_name


def main():
    print(f'\n\nRunning generate_solution_files.py...')
    with open('../data/solved_data.json', 'r') as f:
        solved_data = json.load(f)

    generate_files(solved_data)


if __name__ == '__main__':
    main()
