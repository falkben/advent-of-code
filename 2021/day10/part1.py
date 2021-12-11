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

with open("2021/day10/data.txt") as fh:
    input = fh.read()

scoring = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

chunk_brackets = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}
opening_chars = list(chunk_brackets.values())
closing_chars = list(chunk_brackets.keys())

score_total = 0
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
                score_total += scoring[char]
                break
            else:
                # if it does, we remove from stack
                open_chunks_stack.pop()

print(score_total)
