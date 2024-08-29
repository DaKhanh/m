import os
import re
from src.prompts import *
from src.models import gpt


DATA_PATH = os.path.join(os.path.dirname(__file__), 'data')  # fix

class Task():
    def __init__(self, args) -> None:
        super().__init__()
        file = args.data_file
        path = os.path.join(DATA_PATH, file) # fix
        self.data = open(path).readlines()
        self.steps = 2
        self.stops = ['\nConclusion\n', None]

    def __len__(self) -> int:
        return len(self.data)
    
    def get_input(self, idx: int) -> str:
        return self.data[idx]
        
    @staticmethod
    def standard_prompt(x: str) -> str:
        return standard_prompt.format(input=x) 

    @staticmethod
    def cot_prompt(x: str) -> str:
        return cot_prompt.format(input=x) 

    @staticmethod
    def tot_initial_prompt(x: str) -> str:
        return tot_initial_prompt.format(input=x) 
    
    @staticmethod
    def tot_evaluate_prompt(x: str) -> str:
        return tot_evaluate_prompt