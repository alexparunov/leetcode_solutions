import json
from typing import List, Tuple


def extract_data() -> dict:
    """
    Method that extract data from newly downloaded json file from browser using GET call on: https://leetcode.com/api/problems/all

    This can't be done programmatically since we need authorization
    :return:
    """
    file_data_path = '../data/extracted_data.json'
    with open(file_data_path, 'r', encoding='utf-8') as f:
        print(f'Reading data from: {file_data_path}')
        return json.load(f)


def extract_solved_problems(data: dict) -> Tuple[dict, List[dict]]:
    print(f'Extracting solved problems data and stats')
    total_user_stats = {
        'num_solved': int(data['num_solved']),
        'num_total': int(data['num_total']),
        'num_solved_easy': int(data['ac_easy']),
        'num_solved_medium': int(data['ac_medium']),
        'num_solved_hard': int(data['ac_hard']),
    }

    all_problems = data['stat_status_pairs']

    solved_problems = [prob for prob in all_problems if prob['status'] == 'ac']

    difficulty_map = {1: "Easy", 2: "Medium", 3: "Hard"}

    solved_data = list()
    for prob in solved_problems:
        problem_id = int(prob['stat']['frontend_question_id'])
        title = prob['stat']['question__title']
        title_slug = prob['stat']['question__title_slug']
        url = 'https://leetcode.com/problems/' + title_slug + '/'
        difficulty = difficulty_map[int(prob['difficulty']['level'])]

        solved_data.append((problem_id, title, title_slug, url, difficulty))

    solved_data.sort(key=lambda x: x[0])

    solved_data_dicts = []
    for problem_id, title, title_slug, url, difficulty in solved_data:
        problem_dict = {
            'problem_id': problem_id,
            'title': title,
            'title_slug': title_slug,
            'url': url,
            'difficulty': difficulty
        }

        solved_data_dicts.append(problem_dict)

    return total_user_stats, solved_data_dicts


def save_solved_data(total_user_stats: dict, solved_data: List[dict]):
    stats_path = '../data/total_user_stats.json'
    with open(stats_path, 'w') as f:
        print(f'Saving statistics to: {stats_path}')
        json.dump(total_user_stats, f, indent=2)

    solved_data_path = '../data/solved_data.json'
    with open(solved_data_path, 'w') as f:
        print(f'Saving: {len(solved_data)} problems data to: {solved_data_path}')
        json.dump({'solved_problems': solved_data}, f, indent=2)


def main():
    print(f'\n\nRunning create_solved_files.py...')
    data = extract_data()
    total_user_stats, solved_data = extract_solved_problems(data)
    save_solved_data(total_user_stats, solved_data)


if __name__ == '__main__':
    main()
