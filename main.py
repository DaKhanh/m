import os
import json
import argparse

from src.tasks import Task
from src.methods import solve
from src.models import gpt_usage


def run(args):
    task = Task(args)
    if args.method == 'standard' or args.method == 'cot':
        file = f'./logs/{args.data}/{args.backend}_{args.method}_{args.n_sample}.json'
    else:
        file = f'./logs/{args.data}/{args.backend}_{args.method}_{args.n_generate}_{args.n_evaluate}.json'
    os.makedirs(os.path.dirname(file), exist_ok=True)

    results = []

    for i in range(args.start_index, args.end_index):
        # solve
        result = solve(args, task, i, to_print=True)
        results.append({
            'index': i,
            'result': result
        })

    with open(file, 'w') as json_file:
        json.dump(results, json_file, indent=4)
    
    n = args.end_index - args.start_index
    print('usage_so_far', gpt_usage(args.backend), n)


def parse_args():
    args = argparse.ArgumentParser()
    args.add_argument('--backend', type=str, choices=['gpt-4', 'gpt-3.5-turbo'], default='gpt-3.5-turbo')
    args.add_argument('--temperature', type=float, default=0.7)
    args.add_argument('--data', type=str, choices=['hard', 'too_hard'], default='too_hard')
    args.add_argument('--data_file', type=str, choices=['hard.txt', 'too_hard.txt'], default='hard.txt')
    args.add_argument('--start_index', type=int, default=1)
    args.add_argument('--end_index', type=int, default=10)
    args.add_argument('--method', type=str, choices=['standard', 'cot', 'tot'], default='standard')
    args.add_argument('--n_sample', type=int, default=1)  # use for standard and cot
    args.add_argument('--n_generate', type=int, default=3) # use for tot
    args.add_argument('--n_evaluate', type=int, default=1) # use for tot

    args = args.parse_args()
    return args


if __name__ == '__main__':
    args = parse_args()
    print(args)
    run(args)