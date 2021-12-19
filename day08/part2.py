<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link href="../output.css" rel="stylesheet" />
    <link href="../pygments.css" rel="stylesheet" />
    <script src="https://cdn.jsdelivr.net/pyodide/v0.18.1/full/pyodide.js"></script>
  </head>
  <body>
    <h1 class="text-2xl font-bold underline">
        day08
    </h1>
    <div class="flex mt-3">
      <div class="flex-1"><div class="highlight"><pre><span></span><span class="sd">&quot;&quot;&quot;</span>
<span class="sd">4 digit, seven segment display</span>
<span class="sd">segments a,b,c,d,e,f,g</span>
<span class="sd">wires are connected randomly</span>
<span class="sd">all digits within a 4-digit display use the same connections</span>

<span class="sd">example</span>
<span class="sd">wires b,g could be turned on</span>
<span class="sd">that doesn&#39;t mean _segments_ b &amp; g are turned on</span>
<span class="sd">1 is the only number with 2 segments</span>
<span class="sd">so you know wires b,g -&gt; c,f but not which one maps specifically</span>
<span class="sd">without more info</span>

<span class="sd">  0:      1:      2:      3:      4:</span>
<span class="sd"> aaaa    ....    aaaa    aaaa    ....</span>
<span class="sd">b    c  .    c  .    c  .    c  b    c</span>
<span class="sd">b    c  .    c  .    c  .    c  b    c</span>
<span class="sd"> ....    ....    dddd    dddd    dddd</span>
<span class="sd">e    f  .    f  e    .  .    f  .    f</span>
<span class="sd">e    f  .    f  e    .  .    f  .    f</span>
<span class="sd"> gggg    ....    gggg    gggg    ....</span>

<span class="sd">  5:      6:      7:      8:      9:</span>
<span class="sd"> aaaa    aaaa    aaaa    aaaa    aaaa</span>
<span class="sd">b    .  b    .  .    c  b    c  b    c</span>
<span class="sd">b    .  b    .  .    c  b    c  b    c</span>
<span class="sd"> dddd    dddd    ....    dddd    dddd</span>
<span class="sd">.    f  e    f  .    f  e    f  .    f</span>
<span class="sd">.    f  e    f  .    f  e    f  .    f</span>
<span class="sd"> gggg    gggg    ....    gggg    gggg</span>

<span class="sd">numbers with unique segments: 1, 4, 7, 8</span>

<span class="sd">len   nums</span>
<span class="sd">2     1</span>
<span class="sd">3     7</span>
<span class="sd">4     4</span>
<span class="sd">5     2,3,5</span>
<span class="sd">6     0,6,9</span>
<span class="sd">7     8</span>

<span class="sd">7 contains 1, so with 7 &amp; 1 we can get top (a) segment</span>
<span class="sd">1 contains (c,f), but we cannot identify which is which</span>
<span class="sd">4 contains 1, so, we know (b,d) segments, but not which is which</span>
<span class="sd">we can identify 2s from 3s &amp; 5s bec. after rem. known segs</span>
<span class="sd">of 2,3,5&#39;s, the e segment is the only one that differs</span>
<span class="sd">so we know 2 &amp; we know e segment</span>
<span class="sd">after we know 2, we can identify c from f (since c is in 2 but not f)</span>
<span class="sd">from 2 we know g segment</span>
<span class="sd">from 2 we identify b and d segments since d is in 2 but not b</span>

<span class="sd">at this point we have all segments</span>
<span class="sd">&quot;&quot;&quot;</span>

<span class="nb">input</span> <span class="o">=</span> <span class="s2">&quot;&quot;&quot;</span><span class="se">\</span>
<span class="s2">be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe</span>
<span class="s2">edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc</span>
<span class="s2">fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg</span>
<span class="s2">fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb</span>
<span class="s2">aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea</span>
<span class="s2">fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb</span>
<span class="s2">dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe</span>
<span class="s2">bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef</span>
<span class="s2">egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb</span>
<span class="s2">gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce</span>
<span class="s2">&quot;&quot;&quot;</span>

<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s2">&quot;2021/day08/data.txt&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">fh</span><span class="p">:</span>
    <span class="nb">input</span> <span class="o">=</span> <span class="n">fh</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>

<span class="n">total_output</span> <span class="o">=</span> <span class="mi">0</span>
<span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="nb">input</span><span class="o">.</span><span class="n">splitlines</span><span class="p">():</span>
    <span class="n">signal_pattern</span><span class="p">,</span> <span class="n">output</span> <span class="o">=</span> <span class="n">line</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">&quot; | &quot;</span><span class="p">)</span>

    <span class="c1"># split the signal pattern into digits</span>
    <span class="n">digits</span> <span class="o">=</span> <span class="n">signal_pattern</span><span class="o">.</span><span class="n">split</span><span class="p">()</span>

    <span class="c1"># identify the 1,4,7,8</span>
    <span class="n">digit_lens</span> <span class="o">=</span> <span class="p">[</span><span class="nb">len</span><span class="p">(</span><span class="n">d</span><span class="p">)</span> <span class="k">for</span> <span class="n">d</span> <span class="ow">in</span> <span class="n">digits</span><span class="p">]</span>

    <span class="n">codes</span> <span class="o">=</span> <span class="p">{}</span>
    <span class="n">codes</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="o">=</span> <span class="n">digits</span><span class="p">[</span><span class="n">digit_lens</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="mi">2</span><span class="p">)]</span>
    <span class="n">codes</span><span class="p">[</span><span class="mi">4</span><span class="p">]</span> <span class="o">=</span> <span class="n">digits</span><span class="p">[</span><span class="n">digit_lens</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="mi">4</span><span class="p">)]</span>
    <span class="n">codes</span><span class="p">[</span><span class="mi">7</span><span class="p">]</span> <span class="o">=</span> <span class="n">digits</span><span class="p">[</span><span class="n">digit_lens</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="mi">3</span><span class="p">)]</span>
    <span class="n">codes</span><span class="p">[</span><span class="mi">8</span><span class="p">]</span> <span class="o">=</span> <span class="n">digits</span><span class="p">[</span><span class="n">digit_lens</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="mi">7</span><span class="p">)]</span>

    <span class="c1"># identify 3</span>
    <span class="n">codes</span><span class="p">[</span><span class="mi">3</span><span class="p">]</span> <span class="o">=</span> <span class="nb">next</span><span class="p">(</span>
        <span class="n">d</span> <span class="k">for</span> <span class="n">d</span> <span class="ow">in</span> <span class="n">digits</span> <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">d</span><span class="p">)</span> <span class="o">==</span> <span class="mi">5</span> <span class="ow">and</span> <span class="nb">len</span><span class="p">(</span><span class="nb">set</span><span class="p">(</span><span class="n">d</span><span class="p">)</span> <span class="o">-</span> <span class="nb">set</span><span class="p">(</span><span class="n">codes</span><span class="p">[</span><span class="mi">1</span><span class="p">]))</span> <span class="o">==</span> <span class="mi">3</span>
    <span class="p">)</span>
    <span class="n">codes</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span> <span class="o">=</span> <span class="nb">next</span><span class="p">(</span>
        <span class="n">d</span>
        <span class="k">for</span> <span class="n">d</span> <span class="ow">in</span> <span class="n">digits</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">d</span><span class="p">)</span> <span class="o">==</span> <span class="mi">5</span> <span class="ow">and</span> <span class="nb">len</span><span class="p">(</span><span class="nb">set</span><span class="p">(</span><span class="n">d</span><span class="p">)</span> <span class="o">-</span> <span class="nb">set</span><span class="p">(</span><span class="n">codes</span><span class="p">[</span><span class="mi">3</span><span class="p">])</span> <span class="o">-</span> <span class="nb">set</span><span class="p">(</span><span class="n">codes</span><span class="p">[</span><span class="mi">4</span><span class="p">]))</span> <span class="o">==</span> <span class="mi">1</span>
    <span class="p">)</span>
    <span class="n">codes</span><span class="p">[</span><span class="mi">5</span><span class="p">]</span> <span class="o">=</span> <span class="nb">next</span><span class="p">(</span><span class="n">d</span> <span class="k">for</span> <span class="n">d</span> <span class="ow">in</span> <span class="n">digits</span> <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">d</span><span class="p">)</span> <span class="o">==</span> <span class="mi">5</span> <span class="ow">and</span> <span class="n">d</span> <span class="ow">not</span> <span class="ow">in</span> <span class="nb">list</span><span class="p">(</span><span class="n">codes</span><span class="o">.</span><span class="n">values</span><span class="p">()))</span>
    <span class="n">codes</span><span class="p">[</span><span class="mi">9</span><span class="p">]</span> <span class="o">=</span> <span class="nb">next</span><span class="p">(</span>
        <span class="n">d</span> <span class="k">for</span> <span class="n">d</span> <span class="ow">in</span> <span class="n">digits</span> <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">d</span><span class="p">)</span> <span class="o">==</span> <span class="mi">6</span> <span class="ow">and</span> <span class="nb">len</span><span class="p">(</span><span class="nb">set</span><span class="p">(</span><span class="n">d</span><span class="p">)</span> <span class="o">-</span> <span class="nb">set</span><span class="p">(</span><span class="n">codes</span><span class="p">[</span><span class="mi">3</span><span class="p">]))</span> <span class="o">==</span> <span class="mi">1</span>
    <span class="p">)</span>
    <span class="n">codes</span><span class="p">[</span><span class="mi">6</span><span class="p">]</span> <span class="o">=</span> <span class="nb">next</span><span class="p">(</span>
        <span class="n">d</span> <span class="k">for</span> <span class="n">d</span> <span class="ow">in</span> <span class="n">digits</span> <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">d</span><span class="p">)</span> <span class="o">==</span> <span class="mi">6</span> <span class="ow">and</span> <span class="nb">len</span><span class="p">(</span><span class="nb">set</span><span class="p">(</span><span class="n">d</span><span class="p">)</span> <span class="o">-</span> <span class="nb">set</span><span class="p">(</span><span class="n">codes</span><span class="p">[</span><span class="mi">7</span><span class="p">]))</span> <span class="o">==</span> <span class="mi">4</span>
    <span class="p">)</span>
    <span class="n">codes</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">=</span> <span class="nb">next</span><span class="p">(</span><span class="n">d</span> <span class="k">for</span> <span class="n">d</span> <span class="ow">in</span> <span class="n">digits</span> <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">d</span><span class="p">)</span> <span class="o">==</span> <span class="mi">6</span> <span class="ow">and</span> <span class="n">d</span> <span class="ow">not</span> <span class="ow">in</span> <span class="nb">list</span><span class="p">(</span><span class="n">codes</span><span class="o">.</span><span class="n">values</span><span class="p">()))</span>

    <span class="n">output_items</span> <span class="o">=</span> <span class="n">output</span><span class="o">.</span><span class="n">split</span><span class="p">()</span>
    <span class="n">total_output</span> <span class="o">+=</span> <span class="nb">int</span><span class="p">(</span>
        <span class="s2">&quot;&quot;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span>
            <span class="p">[</span>
                <span class="nb">str</span><span class="p">(</span><span class="n">n</span><span class="p">)</span>
                <span class="k">for</span> <span class="n">o</span> <span class="ow">in</span> <span class="n">output_items</span>
                <span class="k">for</span> <span class="n">n</span><span class="p">,</span> <span class="n">d</span> <span class="ow">in</span> <span class="n">codes</span><span class="o">.</span><span class="n">items</span><span class="p">()</span>
                <span class="k">if</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">d</span><span class="p">)</span> <span class="o">==</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">o</span><span class="p">)</span>
            <span class="p">]</span>
        <span class="p">)</span>
    <span class="p">)</span>

<span class="nb">print</span><span class="p">(</span><span class="n">total_output</span><span class="p">)</span>
</pre></div>
</div>
      <div class="flex-1">
        <p>
          Message to user
        </p>
        <input class="hidden" id="code" value=""""
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

with open("2021/day08/data.txt") as fh:
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
">
        <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded""
          onclick="evaluatePython()">Run</button>
        <br />
        <br />
        <div>Output:</div>
        <textarea id="output" style="width: 100%;" rows="6" disabled></textarea>
      </div>
    </div>

    <script>
      const output = document.getElementById("output");
      const code = document.getElementById("code");

      function addToOutput(s) {
        output.value += ">>>" + code.value + "\n" + s + "\n";
      }

      output.value = "Initializing...\n";
      // init Pyodide
      async function main() {
        let pyodide = await loadPyodide({
          indexURL: "https://cdn.jsdelivr.net/pyodide/v0.18.1/full/",
        });
        output.value += "Ready!\n";
        return pyodide;
      }
      let pyodideReadyPromise = main();

      async function evaluatePython() {
        let pyodide = await pyodideReadyPromise;
        try {
          let output = pyodide.runPython(code.value);
          addToOutput(output);
        } catch (err) {
          addToOutput(err);
        }
      }
    </script>
  </body>
</html>