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

    def __len__(self):
        return 1

    def get_input(self, idx: int) -> str:
        return self.data[idx][0]

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
            category, words = line.split(':')
            words = tuple(sorted(w.strip() for w in words.split(',')))
            if words in groups:
                score += 1
        return {'r': score}

    @staticmethod
    def standard_prompt_wrap(x: str, y:str='') -> str:
        return standard_prompt.format(input=x) + y
