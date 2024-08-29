from src.models import gpt


def evaluate_and_select_best(task, args, x): 
    initial_prompt = task.tot_initial_prompt(x)
    initial_responses = gpt(initial_prompt, n=args.n_generate, stop=None)
    
    evaluations = []
    for i, response in enumerate(initial_responses):
        steps = response.split('\n')
        
        evaluation_prompt = task.tot_evaluate_prompt.format(input=response)
        evaluation_response = gpt(evaluation_prompt, n=args.n_evaluate, stop=None)[0]
        
        scores = extract_scores(evaluation_response)
        evaluations.append((steps, scores))
    
    best_step_set = max(evaluations, key=lambda x: sum(x[1])/len(x[1]))[0]
    
    return best_step_set

def extract_scores(evaluation_response):
    scores = []
    for line in evaluation_response.split('\n'):
        if 'Score:' in line:
            try:
                score = int(line.split('Score:')[1].split('/')[0].strip())
                scores.append(score)
            except:
                continue
    return scores

def get_samples(task, x, n_sample, method):
    if method == 'standard':
        prompt = task.standard_prompt(x)
    elif method == 'cot':
        prompt = task.cot_prompt(x)
    else:
        raise ValueError(f'method {method} not recognized')
    # Generate samples using GPT
    samples = gpt(prompt, n=n_sample)
    # Format the output
    return [sample for sample in samples]


def solve(args, task, idx, to_print=False):
    x = task.get_input(idx)

    # Choose prompt type and generate samples or evaluate
    if args.method == 'cot':
        prompt_sample = 'cot'
        samples = get_samples(task, x, args.n_sample, prompt_sample)
    elif args.method == 'standard':
        prompt_sample = 'standard'
        samples = get_samples(task, x, args.n_sample, prompt_sample)
    elif args.method == 'tot':
        samples = evaluate_and_select_best(task, args, x)
    else:
        raise ValueError(f'prompt_type {args.prompt_type} not recognized')

    # Print the results if requested
    if to_print:
        print(f"Input {idx}: {x}")
        print("Generated samples:")
        for sample in samples:
            print(sample)
            print('-' * 80)

    return samples
