"""
4 digit, seven segment display
segments a,b,c,d,e,f,g
wires are connected randomly
all digits within a 4-digit display use the same connections

example
wires b,g could be turned on
that doesn't mean _segments_ b and g are turned on
1 is the only number with 2 segments
so you know wires b,g -> c,f but not which one maps specifically
without more info
"""

correct_digit_mapping = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg",
}

uniq_lengths = [2, 3, 4, 7]

input = """\
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""

with open("2021/day08/data.txt") as fh:
    input = fh.read()

uniq_digits_in_output = 0
for line in input.splitlines():
    signal_pattern, output = line.split(" | ")

    # print(signal_pattern, output)

    [
        uniq_digits_in_output := uniq_digits_in_output + 1
        for item in output.split()
        if len(item) in uniq_lengths
    ]

print(uniq_digits_in_output)
