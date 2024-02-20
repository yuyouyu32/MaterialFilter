from openai import OpenAI

import random
import pandas as pd
from tqdm import tqdm
import time

import os

Client = OpenAI(api_key = os.getenv('OPENAI_KEY'))
N = 3
Cost = 0


# GPT-4
def calculate_token_price(prompt_tokens, completion_tokens):
    return 7.13 * (0.01 * prompt_tokens / 1000 + 0.03 * completion_tokens / 1000)

def get_rsp_from_GPT(sys_prompt: str, user_prompt: str, n: int = 1):
    """
    Description: 
        Get copywriter from GPT-4
    Args:
        sys_prompt (str): System prompt
        user_prompt (str): User prompt
        n (int, optional): Number of rsp to generate. Defaults to 1.
    Returns:
        rsp (list): List of rsp
        cost (float): Cost price(￥) of generating rsp
    """
    response = Client.chat.completions.create(
    model="gpt-4-0125-preview",
    messages=[
        {"role": "system", "content": sys_prompt},
        {"role": "user", "content": user_prompt},
    ],
    n = n
    ).model_dump()
    cost = calculate_token_price(response['usage']['prompt_tokens'], response['usage']['completion_tokens'])
    rsp = []
    for choice in range(n):
        rsp.append(response['choices'][choice]['message']['content'])
    return rsp, cost

def paper_filter():
    from prompts.PaperFilter import KeyPoints, PaperFilterPrompt
    all_cost = 0
    data = pd.read_excel('../data/TitleAbstract.xlsx')
    for index, row in tqdm(data.iterrows(), total=data.shape[0]):
        title = row['Title']
        abstract = row['Abstract']
        task_prompt = PaperFilterPrompt.format(title=title, abstract=abstract, KeyPoints=KeyPoints)
        copywriters, cost = get_rsp_from_GPT(sys_prompt='', user_prompt=task_prompt, n=1)
        copywriters = '\n'.join(copywriters)
        all_cost += cost
        data.loc[index, 'Relevance'] = copywriters
        data.to_excel('../data/TitleAbstract_R.xlsx', index=False)
        time.sleep(random.randint(2, 3))
    print('Cost: ', all_cost)


def evalue():
    from prompts.Evalue import RULE, EvaluePrompt
    all_cost = 0
    data = pd.read_excel('../data/Score_Design.xlsx')
    for index, row in tqdm(data.iterrows(), total=data.shape[0]):
        data_prompt = str(row.to_dict())
        task_prompt = EvaluePrompt.format(rule=RULE, data=data_prompt)
        copywriters, cost = get_rsp_from_GPT(sys_prompt='', user_prompt=task_prompt, n=1)
        copywriters = '\n'.join(copywriters)
        all_cost += cost
        data.loc[index, 'Evalue'] = copywriters
        data.to_excel('../data/Score_Design_Evalue.xlsx', index=False)
        time.sleep(random.randint(2, 3))
    print('Cost: ', all_cost)

if __name__ == '__main__':
    evalue()