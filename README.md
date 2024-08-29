# Setup
1. Set up OpenAI API key and store in environment variable ``OPENAI_API_KEY`` (see [here](https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety)). 

2. Install:
```bash
git clone https://github.com/DaKhanh/solve_math_with_ToT
pip install -r requirements.txt
pip install -e .  
```

# Experiments

Run the script for doing experiments and testing results
- To run with standard prompts or chain of thought (CoT) prompts
python run.py  --backen --temperature --data --data_file --start_index --end_index --method --n_sample 

- To run with Tree of Thoughts prompts
python run.py  --backen --temperature --data --data_file --start_index --end_index --method --n_generate --n_evaluate

# Citations
Yao, Shunyu, et al. "Tree of Thoughts: Deliberate Problem Solving with Large Language Models." NeurIPS 2023
https://github.com/princeton-nlp/tree-of-thought-llm