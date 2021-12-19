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
        day05
    </h1>
    <div class="flex mt-3">
      <div class="flex-1"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">collections</span> <span class="kn">import</span> <span class="n">defaultdict</span>

<span class="nb">input</span> <span class="o">=</span> <span class="s2">&quot;&quot;&quot;</span><span class="se">\</span>
<span class="s2">0,9 -&gt; 5,9</span>
<span class="s2">8,0 -&gt; 0,8</span>
<span class="s2">9,4 -&gt; 3,4</span>
<span class="s2">2,2 -&gt; 2,1</span>
<span class="s2">7,0 -&gt; 7,4</span>
<span class="s2">6,4 -&gt; 2,0</span>
<span class="s2">0,9 -&gt; 2,9</span>
<span class="s2">3,4 -&gt; 1,4</span>
<span class="s2">0,0 -&gt; 8,8</span>
<span class="s2">5,5 -&gt; 8,2&quot;&quot;&quot;</span>

<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s2">&quot;2021/day05/data.txt&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">fh</span><span class="p">:</span>
    <span class="nb">input</span> <span class="o">=</span> <span class="n">fh</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>

<span class="n">counter</span> <span class="o">=</span> <span class="n">defaultdict</span><span class="p">(</span><span class="nb">int</span><span class="p">)</span>

<span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="nb">input</span><span class="o">.</span><span class="n">splitlines</span><span class="p">():</span>
    <span class="n">p1</span><span class="p">,</span> <span class="n">p2</span> <span class="o">=</span> <span class="n">line</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">&quot; -&gt; &quot;</span><span class="p">)</span>
    <span class="n">x1</span><span class="p">,</span> <span class="n">y1</span> <span class="o">=</span> <span class="nb">map</span><span class="p">(</span><span class="nb">int</span><span class="p">,</span> <span class="n">p1</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">&quot;,&quot;</span><span class="p">))</span>
    <span class="n">x2</span><span class="p">,</span> <span class="n">y2</span> <span class="o">=</span> <span class="nb">map</span><span class="p">(</span><span class="nb">int</span><span class="p">,</span> <span class="n">p2</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">&quot;,&quot;</span><span class="p">))</span>

    <span class="k">if</span> <span class="n">x1</span> <span class="o">==</span> <span class="n">x2</span><span class="p">:</span>
        <span class="c1"># vertical</span>
        <span class="k">for</span> <span class="n">yy</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">min</span><span class="p">(</span><span class="n">y1</span><span class="p">,</span> <span class="n">y2</span><span class="p">),</span> <span class="nb">max</span><span class="p">(</span><span class="n">y1</span><span class="p">,</span> <span class="n">y2</span><span class="p">)</span> <span class="o">+</span> <span class="mi">1</span><span class="p">):</span>
            <span class="n">counter</span><span class="p">[(</span><span class="n">x1</span><span class="p">,</span> <span class="n">yy</span><span class="p">)]</span> <span class="o">+=</span> <span class="mi">1</span>
    <span class="k">elif</span> <span class="n">y1</span> <span class="o">==</span> <span class="n">y2</span><span class="p">:</span>
        <span class="c1"># horizontal</span>
        <span class="k">for</span> <span class="n">xx</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">min</span><span class="p">(</span><span class="n">x1</span><span class="p">,</span> <span class="n">x2</span><span class="p">),</span> <span class="nb">max</span><span class="p">(</span><span class="n">x1</span><span class="p">,</span> <span class="n">x2</span><span class="p">)</span> <span class="o">+</span> <span class="mi">1</span><span class="p">):</span>
            <span class="n">counter</span><span class="p">[(</span><span class="n">xx</span><span class="p">,</span> <span class="n">y1</span><span class="p">)]</span> <span class="o">+=</span> <span class="mi">1</span>

<span class="n">intersect_pts</span> <span class="o">=</span> <span class="mi">0</span>
<span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="n">counter</span><span class="o">.</span><span class="n">values</span><span class="p">():</span>
    <span class="k">if</span> <span class="n">item</span> <span class="o">&gt;=</span> <span class="mi">2</span><span class="p">:</span>
        <span class="n">intersect_pts</span> <span class="o">+=</span> <span class="mi">1</span>

<span class="nb">print</span><span class="p">(</span><span class="n">intersect_pts</span><span class="p">)</span>
</pre></div>
</div>
      <div class="flex-1">
        <p>
          Message to user
        </p>
        <input class="hidden" id="code" value="from collections import defaultdict

input = """\
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""

with open("2021/day05/data.txt") as fh:
    input = fh.read()

counter = defaultdict(int)

for line in input.splitlines():
    p1, p2 = line.split(" -> ")
    x1, y1 = map(int, p1.split(","))
    x2, y2 = map(int, p2.split(","))

    if x1 == x2:
        # vertical
        for yy in range(min(y1, y2), max(y1, y2) + 1):
            counter[(x1, yy)] += 1
    elif y1 == y2:
        # horizontal
        for xx in range(min(x1, x2), max(x1, x2) + 1):
            counter[(xx, y1)] += 1

intersect_pts = 0
for item in counter.values():
    if item >= 2:
        intersect_pts += 1

print(intersect_pts)
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