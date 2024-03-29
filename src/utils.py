import random
import json


def random_text_select(text: str):
    inst_lines = text.split("\n")
    inst_lines = [i for i in inst_lines if i != ""]
    return random.choice(inst_lines)


def random_toi():
    inst = random.choice(["質問　", "問い：　",
                          "質問：　", "問い　",
                         "問題：　",
                          "問題　",
                          ""])
    return inst


def random_sentakushi():
    return random.choice(["選択肢：", "", "選択肢　"])


def write_jsonl(problem_list, path):
    with open(path, "w") as f:
        for problem in problem_list:
            f.write(json.dumps(problem, ensure_ascii=False) + "\n")
