"""
4 digit, seven segment display
segments a,b,c,d,e,f,g
wires are connected randomly
all digits within a 4-digit display use the same connections

example
wires b,g could be turned on
that doesn't mean _segments_ b & g are turned on
1 is the only number with 2 segments
so you know wires b,g -> c,f but not which one maps specifically
without more info

  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg

numbers with unique segments: 1, 4, 7, 8

len   nums
2     1
3     7
4     4
5     2,3,5
6     0,6,9
7     8

7 contains 1, so with 7 & 1 we can get top (a) segment
1 contains (c,f), but we cannot identify which is which
4 contains 1, so, we know (b,d) segments, but not which is which
we can identify 2s from 3s & 5s bec. after rem. known segs
of 2,3,5's, the e segment is the only one that differs
so we know 2 & we know e segment
after we know 2, we can identify c from f (since c is in 2 but not f)
from 2 we know g segment
from 2 we identify b and d segments since d is in 2 but not b

at this point we have all segments
"""

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

with open("2021/day8/data.txt") as fh:
    input = fh.read()

total_output = 0
for line in input.splitlines():
    signal_pattern, output = line.split(" | ")

    # split the signal pattern into digits
    digits = signal_pattern.split()

    # identify the 1,4,7,8
    digit_lens = [len(d) for d in digits]

    codes = {}
    codes[1] = digits[digit_lens.index(2)]
    codes[4] = digits[digit_lens.index(4)]
    codes[7] = digits[digit_lens.index(3)]
    codes[8] = digits[digit_lens.index(7)]

    # identify 3
    codes[3] = next(
        d for d in digits if len(d) == 5 and len(set(d) - set(codes[1])) == 3
    )
    codes[2] = next(
        d
        for d in digits
        if len(d) == 5 and len(set(d) - set(codes[3]) - set(codes[4])) == 1
    )
    codes[5] = next(d for d in digits if len(d) == 5 and d not in list(codes.values()))
    codes[9] = next(
        d for d in digits if len(d) == 6 and len(set(d) - set(codes[3])) == 1
    )
    codes[6] = next(
        d for d in digits if len(d) == 6 and len(set(d) - set(codes[7])) == 4
    )
    codes[0] = next(d for d in digits if len(d) == 6 and d not in list(codes.values()))

    output_items = output.split()
    total_output += int(
        "".join(
            [
                str(n)
                for o in output_items
                for n, d in codes.items()
                if sorted(d) == sorted(o)
            ]
        )
    )

print(total_output)
