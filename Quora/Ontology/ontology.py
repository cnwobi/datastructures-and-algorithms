from collections import defaultdict


def parse_tree_repr(tree_repr):
    level = 0
    tree = defaultdict(list)
    level_tokens = defaultdict(list)
    for idx, token in enumerate(tree_repr.split(" ")):
        if token == "(":
            level += 1
        elif token == ")":
            level -= 1
        else:
            level_tokens[level].append(token)
            if level == 0:
                tree['root'] = token
            else:
                tree[level_tokens[level - 1][-1]].append(token)
    return tree


def parse_questions(questions):
    result = defaultdict(list)
    for question in questions:
        key, value = question.split(": ")
        result[key].append(value)
    return result


def flatten_questions(keys, tree, question_graph):
    flattened = defaultdict(list)

    def dfs(key):
        if not tree:
            return
        ques = []
        if not tree[key]:
            if key in question_graph:
                ques.extend(question_graph[key])
                flattened[key] = ques.copy()
            return ques

        for child_key in tree[key]:
            ques += dfs(child_key)

        if key in question_graph:
            ques.extend(question_graph[key])

        flattened[key] = ques.copy()
        return ques

    for k in list(keys):
        dfs(k)
    return flattened


def count_matching_questions(query, flattened):
    key, prefix = query.split(" ", 1)
    return len([x for x in flattened[key] if x.startswith(prefix)])


def ontology(treeRepr, questions, queries):
    tree = parse_tree_repr(treeRepr)
    question_graph = parse_questions(questions)
    flattened = flatten_questions(list(tree.keys()), tree, question_graph)
    return [count_matching_questions(query, flattened) for query in queries]


if __name__ == '__main__':
    questions_i = [
        "Reptiles: Why are many reptiles green?",
        "Birds: How do birds fly?",
        "Eagles: How endangered are eagles?",
        "Pigeons: Where in the world are pigeons most densely populated?",
        "Eagles: Where do most eagles live?"]

    tree_repr_i = "Animals ( Reptiles Birds ( Eagles Pigeons Crows ) )"
    queries_i = ["Eagles How en",
                 "Birds Where",
                 "Reptiles Why do",
                 "Animals Wh"]
    print(ontology(tree_repr_i, questions_i, queries_i))
