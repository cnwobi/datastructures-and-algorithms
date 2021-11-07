import re


def questionCorrectionBot(question):
    question = question.strip().lstrip() + "?"
    question = re.sub(r"\?+", "?", question)
    question = re.sub(r",", ", ", question)
    question = re.sub(r"\s+,", ",", question)
    question = re.sub(r"\s+", " ", question)
    return question[:1].upper() + question[1:]


