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
        day14
    </h1>
    <div class="flex mt-3">
      <div class="flex-1"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">collections</span> <span class="kn">import</span> <span class="n">Counter</span>

<span class="nb">input</span> <span class="o">=</span> <span class="s2">&quot;&quot;&quot;</span><span class="se">\</span>
<span class="s2">NNCB</span>

<span class="s2">CH -&gt; B</span>
<span class="s2">HH -&gt; N</span>
<span class="s2">CB -&gt; H</span>
<span class="s2">NH -&gt; C</span>
<span class="s2">HB -&gt; C</span>
<span class="s2">HC -&gt; B</span>
<span class="s2">HN -&gt; C</span>
<span class="s2">NN -&gt; C</span>
<span class="s2">BH -&gt; H</span>
<span class="s2">NC -&gt; B</span>
<span class="s2">NB -&gt; B</span>
<span class="s2">BN -&gt; B</span>
<span class="s2">BB -&gt; N</span>
<span class="s2">BC -&gt; B</span>
<span class="s2">CC -&gt; N</span>
<span class="s2">CN -&gt; C</span>
<span class="s2">&quot;&quot;&quot;</span>

<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s2">&quot;2021/day14/data.txt&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">fh</span><span class="p">:</span>
    <span class="nb">input</span> <span class="o">=</span> <span class="n">fh</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>

<span class="n">template</span><span class="p">,</span> <span class="n">rules_s</span> <span class="o">=</span> <span class="nb">input</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\n\n</span><span class="s2">&quot;</span><span class="p">)</span>

<span class="n">rules</span> <span class="o">=</span> <span class="p">{}</span>
<span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">rules_s</span><span class="o">.</span><span class="n">splitlines</span><span class="p">():</span>
    <span class="n">rule_pair</span><span class="p">,</span> <span class="n">insert_char</span> <span class="o">=</span> <span class="n">line</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">&quot; -&gt; &quot;</span><span class="p">)</span>
    <span class="n">rules</span><span class="p">[</span><span class="n">rule_pair</span><span class="p">]</span> <span class="o">=</span> <span class="n">insert_char</span>

<span class="k">for</span> <span class="n">step</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">10</span><span class="p">):</span>
    <span class="n">insertions</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="c1"># go through the template</span>
    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">template</span><span class="p">)):</span>
        <span class="n">char_pair</span> <span class="o">=</span> <span class="n">template</span><span class="p">[</span><span class="n">i</span> <span class="p">:</span> <span class="n">i</span> <span class="o">+</span> <span class="mi">2</span><span class="p">]</span>
        <span class="k">if</span> <span class="n">char_pair</span> <span class="ow">in</span> <span class="n">rules</span><span class="p">:</span>
            <span class="c1"># evaluate rule against template</span>
            <span class="c1"># store insertions to make</span>
            <span class="n">insertions</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">i</span> <span class="o">+</span> <span class="mi">1</span><span class="p">,</span> <span class="n">rules</span><span class="p">[</span><span class="n">char_pair</span><span class="p">]))</span>
    <span class="c1"># apply insertions</span>
    <span class="n">insertions_applied</span> <span class="o">=</span> <span class="mi">0</span>
    <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">char</span> <span class="ow">in</span> <span class="n">insertions</span><span class="p">:</span>
        <span class="n">template</span> <span class="o">=</span> <span class="p">(</span>
            <span class="n">template</span><span class="p">[:</span> <span class="n">i</span> <span class="o">+</span> <span class="n">insertions_applied</span><span class="p">]</span>
            <span class="o">+</span> <span class="n">char</span>
            <span class="o">+</span> <span class="n">template</span><span class="p">[</span><span class="n">i</span> <span class="o">+</span> <span class="n">insertions_applied</span> <span class="p">:]</span>
        <span class="p">)</span>
        <span class="n">insertions_applied</span> <span class="o">+=</span> <span class="mi">1</span>

    <span class="c1"># print(template)</span>

<span class="n">c</span> <span class="o">=</span> <span class="n">Counter</span><span class="p">(</span><span class="n">template</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">c</span><span class="o">.</span><span class="n">most_common</span><span class="p">()[</span><span class="mi">0</span><span class="p">][</span><span class="mi">1</span><span class="p">]</span> <span class="o">-</span> <span class="n">c</span><span class="o">.</span><span class="n">most_common</span><span class="p">()[</span><span class="o">-</span><span class="mi">1</span><span class="p">][</span><span class="mi">1</span><span class="p">])</span>

<span class="c1"># print(template)</span>
<span class="c1"># print(rules)</span>
</pre></div>
</div>
      <div class="flex-1">
        <p>
          Message to user
        </p>
        <input class="hidden" id="code" value="from collections import Counter

input = """\
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""

with open("2021/day14/data.txt") as fh:
    input = fh.read()

template, rules_s = input.split("\n\n")

rules = {}
for line in rules_s.splitlines():
    rule_pair, insert_char = line.split(" -> ")
    rules[rule_pair] = insert_char

for step in range(10):
    insertions = []

    # go through the template
    for i in range(len(template)):
        char_pair = template[i : i + 2]
        if char_pair in rules:
            # evaluate rule against template
            # store insertions to make
            insertions.append((i + 1, rules[char_pair]))
    # apply insertions
    insertions_applied = 0
    for i, char in insertions:
        template = (
            template[: i + insertions_applied]
            + char
            + template[i + insertions_applied :]
        )
        insertions_applied += 1

    # print(template)

c = Counter(template)
print(c.most_common()[0][1] - c.most_common()[-1][1])

# print(template)
# print(rules)
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