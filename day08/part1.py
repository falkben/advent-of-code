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
<span class="sd">that doesn&#39;t mean _segments_ b and g are turned on</span>
<span class="sd">1 is the only number with 2 segments</span>
<span class="sd">so you know wires b,g -&gt; c,f but not which one maps specifically</span>
<span class="sd">without more info</span>
<span class="sd">&quot;&quot;&quot;</span>

<span class="n">correct_digit_mapping</span> <span class="o">=</span> <span class="p">{</span>
    <span class="mi">0</span><span class="p">:</span> <span class="s2">&quot;abcefg&quot;</span><span class="p">,</span>
    <span class="mi">1</span><span class="p">:</span> <span class="s2">&quot;cf&quot;</span><span class="p">,</span>
    <span class="mi">2</span><span class="p">:</span> <span class="s2">&quot;acdeg&quot;</span><span class="p">,</span>
    <span class="mi">3</span><span class="p">:</span> <span class="s2">&quot;acdfg&quot;</span><span class="p">,</span>
    <span class="mi">4</span><span class="p">:</span> <span class="s2">&quot;bcdf&quot;</span><span class="p">,</span>
    <span class="mi">5</span><span class="p">:</span> <span class="s2">&quot;abdfg&quot;</span><span class="p">,</span>
    <span class="mi">6</span><span class="p">:</span> <span class="s2">&quot;abdefg&quot;</span><span class="p">,</span>
    <span class="mi">7</span><span class="p">:</span> <span class="s2">&quot;acf&quot;</span><span class="p">,</span>
    <span class="mi">8</span><span class="p">:</span> <span class="s2">&quot;abcdefg&quot;</span><span class="p">,</span>
    <span class="mi">9</span><span class="p">:</span> <span class="s2">&quot;abcdfg&quot;</span><span class="p">,</span>
<span class="p">}</span>

<span class="n">uniq_lengths</span> <span class="o">=</span> <span class="p">[</span><span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">,</span> <span class="mi">4</span><span class="p">,</span> <span class="mi">7</span><span class="p">]</span>

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

<span class="n">uniq_digits_in_output</span> <span class="o">=</span> <span class="mi">0</span>
<span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="nb">input</span><span class="o">.</span><span class="n">splitlines</span><span class="p">():</span>
    <span class="n">signal_pattern</span><span class="p">,</span> <span class="n">output</span> <span class="o">=</span> <span class="n">line</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">&quot; | &quot;</span><span class="p">)</span>

    <span class="c1"># print(signal_pattern, output)</span>

    <span class="p">[</span>
        <span class="n">uniq_digits_in_output</span> <span class="o">:=</span> <span class="n">uniq_digits_in_output</span> <span class="o">+</span> <span class="mi">1</span>
        <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">output</span><span class="o">.</span><span class="n">split</span><span class="p">()</span>
        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">item</span><span class="p">)</span> <span class="ow">in</span> <span class="n">uniq_lengths</span>
    <span class="p">]</span>

<span class="nb">print</span><span class="p">(</span><span class="n">uniq_digits_in_output</span><span class="p">)</span>
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