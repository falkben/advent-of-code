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
        day13
    </h1>
    <div class="flex mt-3">
      <div class="flex-1"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">collections</span> <span class="kn">import</span> <span class="n">defaultdict</span>

<span class="nb">input</span> <span class="o">=</span> <span class="s2">&quot;&quot;&quot;</span><span class="se">\</span>
<span class="s2">6,10</span>
<span class="s2">0,14</span>
<span class="s2">9,10</span>
<span class="s2">0,3</span>
<span class="s2">10,4</span>
<span class="s2">4,11</span>
<span class="s2">6,0</span>
<span class="s2">6,12</span>
<span class="s2">4,1</span>
<span class="s2">0,13</span>
<span class="s2">10,12</span>
<span class="s2">3,4</span>
<span class="s2">3,0</span>
<span class="s2">8,4</span>
<span class="s2">1,10</span>
<span class="s2">2,14</span>
<span class="s2">8,10</span>
<span class="s2">9,0</span>

<span class="s2">fold along y=7</span>
<span class="s2">fold along x=5&quot;&quot;&quot;</span>


<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s2">&quot;2021/day13/data.txt&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">fh</span><span class="p">:</span>
    <span class="nb">input</span> <span class="o">=</span> <span class="n">fh</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>

<span class="n">dot_input</span><span class="p">,</span> <span class="n">fold_input</span> <span class="o">=</span> <span class="nb">input</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\n\n</span><span class="s2">&quot;</span><span class="p">)</span>
<span class="n">pair_data</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
<span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">dot_input</span><span class="o">.</span><span class="n">splitlines</span><span class="p">():</span>
    <span class="n">x</span><span class="p">,</span> <span class="n">y</span> <span class="o">=</span> <span class="n">line</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">&quot;,&quot;</span><span class="p">)</span>
    <span class="n">pair_data</span><span class="o">.</span><span class="n">add</span><span class="p">((</span><span class="nb">int</span><span class="p">(</span><span class="n">x</span><span class="p">),</span> <span class="nb">int</span><span class="p">(</span><span class="n">y</span><span class="p">)))</span>
<span class="c1"># print(pair_data)</span>

<span class="n">folds</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="n">fold_line</span> <span class="ow">in</span> <span class="n">fold_input</span><span class="o">.</span><span class="n">splitlines</span><span class="p">():</span>
    <span class="n">_</span><span class="p">,</span> <span class="n">fold_val_str</span> <span class="o">=</span> <span class="n">fold_line</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">&quot;fold along &quot;</span><span class="p">)</span>
    <span class="n">axis</span><span class="p">,</span> <span class="n">fold_val</span> <span class="o">=</span> <span class="n">fold_val_str</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">&quot;=&quot;</span><span class="p">)</span>
    <span class="n">folds</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="mi">0</span> <span class="k">if</span> <span class="n">axis</span> <span class="o">==</span> <span class="s2">&quot;x&quot;</span> <span class="k">else</span> <span class="mi">1</span><span class="p">,</span> <span class="nb">int</span><span class="p">(</span><span class="n">fold_val</span><span class="p">)))</span>
<span class="c1"># print(folds)</span>

<span class="c1"># part1 only the first fold</span>
<span class="k">for</span> <span class="n">axis</span><span class="p">,</span> <span class="n">fold_val</span> <span class="ow">in</span> <span class="n">folds</span><span class="p">[</span><span class="mi">0</span><span class="p">:</span><span class="mi">1</span><span class="p">]:</span>
    <span class="n">folded_pair_data</span> <span class="o">=</span> <span class="n">pair_data</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>
    <span class="k">for</span> <span class="n">pair</span> <span class="ow">in</span> <span class="n">pair_data</span><span class="p">:</span>
        <span class="n">point_val</span> <span class="o">=</span> <span class="n">pair</span><span class="p">[</span><span class="n">axis</span><span class="p">]</span>
        <span class="k">if</span> <span class="n">point_val</span> <span class="o">&gt;</span> <span class="n">fold_val</span><span class="p">:</span>
            <span class="n">folded_pair</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">pair</span><span class="p">)</span>
            <span class="n">folded_pair</span><span class="p">[</span><span class="n">axis</span><span class="p">]</span> <span class="o">=</span> <span class="mi">2</span> <span class="o">*</span> <span class="n">fold_val</span> <span class="o">-</span> <span class="n">folded_pair</span><span class="p">[</span><span class="n">axis</span><span class="p">]</span>
            <span class="n">folded_pair_data</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">pair</span><span class="p">)</span>
            <span class="n">folded_pair_data</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="nb">tuple</span><span class="p">(</span><span class="n">folded_pair</span><span class="p">))</span>
    <span class="n">pair_data</span> <span class="o">=</span> <span class="n">folded_pair_data</span>

<span class="nb">print</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">folded_pair_data</span><span class="p">))</span>


<span class="sd">&quot;&quot;&quot;</span>
<span class="sd">0   0</span>
<span class="sd">1   1</span>
<span class="sd">2   2</span>
<span class="sd">3   3</span>
<span class="sd">4----</span>
<span class="sd">5   3   4 - (5-4) = n + -v +n = 2n-v</span>
<span class="sd">6   2   4 - (6-4)</span>
<span class="sd">7   1   4 - (7-4)</span>
<span class="sd">8   0   4 - (8-4)</span>
<span class="sd">&quot;&quot;&quot;</span>
</pre></div>
</div>
      <div class="flex-1">
        <p>
          Message to user
        </p>
        <input class="hidden" id="code" value="from collections import defaultdict

input = """\
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""


with open("2021/day13/data.txt") as fh:
    input = fh.read()

dot_input, fold_input = input.split("\n\n")
pair_data = set()
for line in dot_input.splitlines():
    x, y = line.split(",")
    pair_data.add((int(x), int(y)))
# print(pair_data)

folds = []
for fold_line in fold_input.splitlines():
    _, fold_val_str = fold_line.split("fold along ")
    axis, fold_val = fold_val_str.split("=")
    folds.append((0 if axis == "x" else 1, int(fold_val)))
# print(folds)

# part1 only the first fold
for axis, fold_val in folds[0:1]:
    folded_pair_data = pair_data.copy()
    for pair in pair_data:
        point_val = pair[axis]
        if point_val > fold_val:
            folded_pair = list(pair)
            folded_pair[axis] = 2 * fold_val - folded_pair[axis]
            folded_pair_data.remove(pair)
            folded_pair_data.add(tuple(folded_pair))
    pair_data = folded_pair_data

print(len(folded_pair_data))


"""
0   0
1   1
2   2
3   3
4----
5   3   4 - (5-4) = n + -v +n = 2n-v
6   2   4 - (6-4)
7   1   4 - (7-4)
8   0   4 - (8-4)
"""
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