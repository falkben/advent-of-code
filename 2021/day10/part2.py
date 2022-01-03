"""corrupted means chunk closed by wrong character

incomplete means chunk was never closed

corrupted line is chunk closes with wrong character
"(]"
"""


input = """\
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""

# with open("2021/day10/data.txt") as fh:
#     input = fh.read()

scoring = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}

chunk_brackets = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}
opening_chars = list(chunk_brackets.values())
closing_chars = list(chunk_brackets.keys())

line_scores = []
for line in input.splitlines():

    open_chunks_stack = []

    for char in line:

        if char in opening_chars:
            # add to stack
            open_chunks_stack.append(char)
        if char in closing_chars:
            # check if it closes the chunk
            if open_chunks_stack[-1] != chunk_brackets[char]:
                # if it doesn't, we have corr. line
                break
            else:
                # if it does, we remove from stack
                open_chunks_stack.pop()

    else:
        line_score = 0
        while len(open_chunks_stack) > 0:
            char = open_chunks_stack.pop()
            line_score = line_score * 5 + scoring[char]

        line_scores.append(line_score)

line_scores.sort()
print(line_scores[len(line_scores) // 2])

return_value = line_scores[len(line_scores) // 2]
