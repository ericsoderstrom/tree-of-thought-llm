import re
import os
import json
from tot.tasks.base import Task, DATA_PATH
from tot.prompts.connections import * 
from tot.models import gpt

class ConnectionsTask(Task):
    """
    Input (x)   : 16 words comprising a game of NYT connections
    Output (y)  : Four disjoint sets of four related words that cover the input set
    Reward (r)  : 1 for each fully correct category
    """
    def __init__(self, file='connections.json'):
        super().__init__()
        self.file = os.path.join(DATA_PATH, 'connections', file)
        self.data = json.load(open(self.file)) 
        self.steps = 4
        self.value_cache = {}

    def __len__(self):
        return 1

    def get_input(self, idx: int) -> str:
        return ', '.join(self.data[idx][0])

    def test_output(self, idx: int, output: str):
        output = output.split('Output:\n')[-1]
        score = 0
        answers = self.data[idx][1]
        groups = set()
        print("evaluating output:")
        print(output)

        for row in answers:
            words = row[1]
            words = sorted([w.strip() for w in words.split(',')])
            groups.add(tuple(words))

        for i, line in enumerate(output.strip().split('\n')):
            words = line[line.rfind(':')+1:]
            # category, words = line.split(':')
            words = tuple(sorted(w.strip() for w in words.split(',')))
            if words in groups:
                score += 1
        return {'r': score}

    @staticmethod
    def standard_prompt_wrap(x: str, y:str='') -> str:
        return standard_prompt.format(input=x) + y

    @staticmethod
    def cot_prompt_wrap(x: str, y:str='') -> str:
        return cot_prompt.format(input=x) + y

    def get_current_words(y):
        return y

    @staticmethod
    def value_prompt_wrap(x: str, y: str) -> str:
        return value_prompt.format(input=y)


    @staticmethod
    def value_outputs_unwrap(x: str, y: str, value_outputs: list) -> float:
        value_map = {'impossible': 0.001, 'likely': 1, 'sure': 20}
        value_names = [_.split('\n')[-1] for _ in value_outputs]
        value = sum(value * value_names.count(name) for name, value in value_map.items())
        return value


    @staticmethod
    def propose_prompt_wrap(x: str, y: str='') -> str:
        if not y: return propose_prompt.format(input=x)
        remaining_words = set(x.strip().split(','))
        categories = y.strip().split('\n')
        for category in categories:
            category, words = category.split(':')
            words = words.strip().split(',')
            remaining_words -= set(words)

        if len(remaining_words) == 0:
            prompt = cot_prompt.format(input=x) + 'Steps:' + y
        else:
            prompt = propose_prompt.format(input=', '.join(remaining_words))
            return prompt