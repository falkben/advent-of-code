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
        day06
    </h1>
    <div class="flex mt-3">
      <div class="flex-1"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>

<span class="nb">input</span> <span class="o">=</span> <span class="s2">&quot;&quot;&quot;3,4,3,1,2&quot;&quot;&quot;</span>
<span class="c1"># input = &quot;&quot;&quot;4,1,1,4,1,1,1,1,1,1,1,1,3,4,1,1,1,3,1,3,1,1,1,1,1,1,1,1,1,3,1,3,1,1,1,5,1,2,1,1,5,3,4,2,1,1,4,1,1,5,1,1,5,5,1,1,5,2,1,4,1,2,1,4,5,4,1,1,1,1,3,1,1,1,4,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,1,2,1,1,1,1,1,1,1,2,4,4,1,1,3,1,3,2,4,3,1,1,1,1,1,2,1,1,1,1,2,5,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,4,1,5,1,3,1,1,1,1,1,5,1,1,1,3,1,2,1,2,1,3,4,5,1,1,1,1,1,1,5,1,1,1,1,1,1,1,1,3,1,1,3,1,1,4,1,1,1,1,1,2,1,1,1,1,3,2,1,1,1,4,2,1,1,1,4,1,1,2,3,1,4,1,5,1,1,1,2,1,5,3,3,3,1,5,3,1,1,1,1,1,1,1,1,4,5,3,1,1,5,1,1,1,4,1,1,5,1,2,3,4,2,1,5,2,1,2,5,1,1,1,1,4,1,2,1,1,1,2,5,1,1,5,1,1,1,3,2,4,1,3,1,1,2,1,5,1,3,4,4,2,2,1,1,1,1,5,1,5,2&quot;&quot;&quot;</span>

<span class="n">ages</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">fromstring</span><span class="p">(</span><span class="nb">input</span><span class="p">,</span> <span class="n">dtype</span><span class="o">=</span><span class="nb">int</span><span class="p">,</span> <span class="n">sep</span><span class="o">=</span><span class="s2">&quot;,&quot;</span><span class="p">))</span>

<span class="c1"># print(ages)</span>

<span class="k">for</span> <span class="n">day</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">80</span><span class="p">):</span>
    <span class="n">ages</span> <span class="o">=</span> <span class="n">ages</span> <span class="o">-</span> <span class="mi">1</span>
    <span class="n">new_fish</span> <span class="o">=</span> <span class="nb">sum</span><span class="p">(</span><span class="n">ages</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">)</span>
    <span class="n">ages</span><span class="p">[</span><span class="n">ages</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">]</span> <span class="o">=</span> <span class="mi">6</span>
    <span class="n">ages</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">ages</span><span class="p">,</span> <span class="n">np</span><span class="o">.</span><span class="n">ones</span><span class="p">(</span><span class="n">new_fish</span><span class="p">,</span> <span class="n">dtype</span><span class="o">=</span><span class="nb">int</span><span class="p">)</span> <span class="o">*</span> <span class="mi">8</span><span class="p">)</span>
    <span class="c1"># print(day, ages)</span>

<span class="nb">print</span><span class="p">(</span><span class="n">ages</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
</pre></div>
</div>
      <div class="flex-1">
        <p>
          Message to user
        </p>
        <input class="hidden" id="code" value="import numpy as np

input = """3,4,3,1,2"""
# input = """4,1,1,4,1,1,1,1,1,1,1,1,3,4,1,1,1,3,1,3,1,1,1,1,1,1,1,1,1,3,1,3,1,1,1,5,1,2,1,1,5,3,4,2,1,1,4,1,1,5,1,1,5,5,1,1,5,2,1,4,1,2,1,4,5,4,1,1,1,1,3,1,1,1,4,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,1,2,1,1,1,1,1,1,1,2,4,4,1,1,3,1,3,2,4,3,1,1,1,1,1,2,1,1,1,1,2,5,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,4,1,5,1,3,1,1,1,1,1,5,1,1,1,3,1,2,1,2,1,3,4,5,1,1,1,1,1,1,5,1,1,1,1,1,1,1,1,3,1,1,3,1,1,4,1,1,1,1,1,2,1,1,1,1,3,2,1,1,1,4,2,1,1,1,4,1,1,2,3,1,4,1,5,1,1,1,2,1,5,3,3,3,1,5,3,1,1,1,1,1,1,1,1,4,5,3,1,1,5,1,1,1,4,1,1,5,1,2,3,4,2,1,5,2,1,2,5,1,1,1,1,4,1,2,1,1,1,2,5,1,1,5,1,1,1,3,2,4,1,3,1,1,2,1,5,1,3,4,4,2,2,1,1,1,1,5,1,5,2"""

ages = np.array(np.fromstring(input, dtype=int, sep=","))

# print(ages)

for day in range(80):
    ages = ages - 1
    new_fish = sum(ages < 0)
    ages[ages < 0] = 6
    ages = np.append(ages, np.ones(new_fish, dtype=int) * 8)
    # print(day, ages)

print(ages.shape)
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