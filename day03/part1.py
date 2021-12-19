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
        day03
    </h1>
    <div class="flex mt-3">
      <div class="flex-1"><div class="highlight"><pre><span></span><span class="kn">from</span> <span class="nn">io</span> <span class="kn">import</span> <span class="n">StringIO</span>

<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>

<span class="nb">input</span> <span class="o">=</span> <span class="s2">&quot;&quot;&quot;</span><span class="se">\</span>
<span class="s2">00100</span>
<span class="s2">11110</span>
<span class="s2">10110</span>
<span class="s2">10111</span>
<span class="s2">10101</span>
<span class="s2">01111</span>
<span class="s2">00111</span>
<span class="s2">11100</span>
<span class="s2">10000</span>
<span class="s2">11001</span>
<span class="s2">00010</span>
<span class="s2">01010&quot;&quot;&quot;</span>

<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s2">&quot;2021/day03/data.txt&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">fh</span><span class="p">:</span>
    <span class="nb">input</span> <span class="o">=</span> <span class="n">fh</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>


<span class="n">c</span> <span class="o">=</span> <span class="n">StringIO</span><span class="p">(</span><span class="nb">input</span><span class="p">)</span>
<span class="n">arr</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">genfromtxt</span><span class="p">(</span><span class="n">c</span><span class="p">,</span> <span class="n">dtype</span><span class="o">=</span><span class="nb">int</span><span class="p">,</span> <span class="n">delimiter</span><span class="o">=</span><span class="n">np</span><span class="o">.</span><span class="n">ones</span><span class="p">(</span><span class="mi">12</span><span class="p">,</span> <span class="nb">int</span><span class="p">))</span>

<span class="n">arr_avg</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">mean</span><span class="p">(</span><span class="n">arr</span><span class="p">,</span> <span class="n">axis</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>

<span class="n">gamma_bin</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">round</span><span class="p">(</span><span class="n">arr_avg</span><span class="p">)</span><span class="o">.</span><span class="n">astype</span><span class="p">(</span><span class="nb">int</span><span class="p">)</span>
<span class="n">epsilon_bin</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">abs</span><span class="p">(</span><span class="mi">1</span> <span class="o">-</span> <span class="n">gamma_bin</span><span class="p">)</span>


<span class="k">def</span> <span class="nf">conv_arr_dec</span><span class="p">(</span><span class="n">arr</span><span class="p">):</span>
    <span class="n">dec</span> <span class="o">=</span> <span class="mi">0</span>
    <span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">v</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="nb">reversed</span><span class="p">(</span><span class="n">arr</span><span class="p">)):</span>
        <span class="n">dec</span> <span class="o">+=</span> <span class="n">v</span> <span class="o">*</span> <span class="mi">2</span> <span class="o">**</span> <span class="n">i</span>
    <span class="k">return</span> <span class="n">dec</span>


<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;power consumption:&quot;</span><span class="p">,</span> <span class="n">conv_arr_dec</span><span class="p">(</span><span class="n">gamma_bin</span><span class="p">)</span> <span class="o">*</span> <span class="n">conv_arr_dec</span><span class="p">(</span><span class="n">epsilon_bin</span><span class="p">))</span>
</pre></div>
</div>
      <div class="flex-1">
        <p>
          Message to user
        </p>
        <input class="hidden" id="code" value="from io import StringIO

import numpy as np

input = """\
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

with open("2021/day03/data.txt") as fh:
    input = fh.read()


c = StringIO(input)
arr = np.genfromtxt(c, dtype=int, delimiter=np.ones(12, int))

arr_avg = np.mean(arr, axis=0)

gamma_bin = np.round(arr_avg).astype(int)
epsilon_bin = np.abs(1 - gamma_bin)


def conv_arr_dec(arr):
    dec = 0
    for i, v in enumerate(reversed(arr)):
        dec += v * 2 ** i
    return dec


print("power consumption:", conv_arr_dec(gamma_bin) * conv_arr_dec(epsilon_bin))
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