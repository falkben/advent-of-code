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
        day09
    </h1>
    <div class="flex mt-3">
      <div class="flex-1"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>

<span class="nb">input</span> <span class="o">=</span> <span class="s2">&quot;&quot;&quot;</span><span class="se">\</span>
<span class="s2">2199943210</span>
<span class="s2">3987894921</span>
<span class="s2">9856789892</span>
<span class="s2">8767896789</span>
<span class="s2">9899965678&quot;&quot;&quot;</span>

<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s2">&quot;2021/day09/data.txt&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">fh</span><span class="p">:</span>
    <span class="nb">input</span> <span class="o">=</span> <span class="n">fh</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>

<span class="n">linelen</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="nb">input</span><span class="o">.</span><span class="n">splitlines</span><span class="p">()[</span><span class="mi">0</span><span class="p">])</span>
<span class="n">rowlen</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="nb">input</span><span class="o">.</span><span class="n">splitlines</span><span class="p">())</span>

<span class="n">hmap</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">genfromtxt</span><span class="p">(</span>
    <span class="nb">input</span><span class="o">.</span><span class="n">splitlines</span><span class="p">(),</span> <span class="n">dtype</span><span class="o">=</span><span class="n">np</span><span class="o">.</span><span class="n">int8</span><span class="p">,</span> <span class="n">delimiter</span><span class="o">=</span><span class="n">np</span><span class="o">.</span><span class="n">ones</span><span class="p">(</span><span class="n">linelen</span><span class="p">,</span> <span class="n">dtype</span><span class="o">=</span><span class="n">np</span><span class="o">.</span><span class="n">int8</span><span class="p">)</span>
<span class="p">)</span>

<span class="n">risk_lvl</span> <span class="o">=</span> <span class="mi">0</span>
<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">hmap</span><span class="o">.</span><span class="n">shape</span><span class="p">[</span><span class="mi">0</span><span class="p">]):</span>
    <span class="k">for</span> <span class="n">j</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">hmap</span><span class="o">.</span><span class="n">shape</span><span class="p">[</span><span class="mi">1</span><span class="p">]):</span>
        <span class="n">val</span> <span class="o">=</span> <span class="n">hmap</span><span class="p">[</span><span class="n">i</span><span class="p">,</span> <span class="n">j</span><span class="p">]</span>

        <span class="k">if</span> <span class="p">(</span>
            <span class="p">(</span><span class="n">i</span> <span class="o">==</span> <span class="n">rowlen</span> <span class="o">-</span> <span class="mi">1</span> <span class="ow">or</span> <span class="n">val</span> <span class="o">&lt;</span> <span class="n">hmap</span><span class="p">[</span><span class="n">i</span> <span class="o">+</span> <span class="mi">1</span><span class="p">,</span> <span class="n">j</span><span class="p">])</span>
            <span class="ow">and</span> <span class="p">(</span><span class="n">i</span> <span class="o">==</span> <span class="mi">0</span> <span class="ow">or</span> <span class="n">val</span> <span class="o">&lt;</span> <span class="n">hmap</span><span class="p">[</span><span class="n">i</span> <span class="o">-</span> <span class="mi">1</span><span class="p">,</span> <span class="n">j</span><span class="p">])</span>
            <span class="ow">and</span> <span class="p">(</span><span class="n">j</span> <span class="o">==</span> <span class="mi">0</span> <span class="ow">or</span> <span class="n">val</span> <span class="o">&lt;</span> <span class="n">hmap</span><span class="p">[</span><span class="n">i</span><span class="p">,</span> <span class="n">j</span> <span class="o">-</span> <span class="mi">1</span><span class="p">])</span>
            <span class="ow">and</span> <span class="p">(</span><span class="n">j</span> <span class="o">==</span> <span class="n">linelen</span> <span class="o">-</span> <span class="mi">1</span> <span class="ow">or</span> <span class="n">val</span> <span class="o">&lt;</span> <span class="n">hmap</span><span class="p">[</span><span class="n">i</span><span class="p">,</span> <span class="n">j</span> <span class="o">+</span> <span class="mi">1</span><span class="p">])</span>
        <span class="p">):</span>
            <span class="n">risk_lvl</span> <span class="o">+=</span> <span class="n">hmap</span><span class="p">[</span><span class="n">i</span><span class="p">,</span> <span class="n">j</span><span class="p">]</span> <span class="o">+</span> <span class="mi">1</span>
            <span class="nb">print</span><span class="p">(</span><span class="n">hmap</span><span class="p">[</span><span class="n">i</span><span class="p">,</span> <span class="n">j</span><span class="p">])</span>

<span class="nb">print</span><span class="p">(</span><span class="n">risk_lvl</span><span class="p">)</span>
</pre></div>
</div>
      <div class="flex-1">
        <p>
          Message to user
        </p>
        <input class="hidden" id="code" value="import numpy as np

input = """\
2199943210
3987894921
9856789892
8767896789
9899965678"""

with open("2021/day09/data.txt") as fh:
    input = fh.read()

linelen = len(input.splitlines()[0])
rowlen = len(input.splitlines())

hmap = np.genfromtxt(
    input.splitlines(), dtype=np.int8, delimiter=np.ones(linelen, dtype=np.int8)
)

risk_lvl = 0
for i in range(hmap.shape[0]):
    for j in range(hmap.shape[1]):
        val = hmap[i, j]

        if (
            (i == rowlen - 1 or val < hmap[i + 1, j])
            and (i == 0 or val < hmap[i - 1, j])
            and (j == 0 or val < hmap[i, j - 1])
            and (j == linelen - 1 or val < hmap[i, j + 1])
        ):
            risk_lvl += hmap[i, j] + 1
            print(hmap[i, j])

print(risk_lvl)
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