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
        day02
    </h1>
    <div class="flex mt-3">
      <div class="flex-1"><div class="highlight"><pre><span></span><span class="nb">input</span> <span class="o">=</span> <span class="s2">&quot;&quot;&quot;</span><span class="se">\</span>
<span class="s2">forward 5</span>
<span class="s2">down 5</span>
<span class="s2">forward 8</span>
<span class="s2">up 3</span>
<span class="s2">down 8</span>
<span class="s2">forward 2&quot;&quot;&quot;</span>

<span class="c1"># part 1</span>

<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s2">&quot;2021/day2/data.txt&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">inputfh</span><span class="p">:</span>
    <span class="n">data</span> <span class="o">=</span> <span class="n">inputfh</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>
<span class="nb">input</span> <span class="o">=</span> <span class="n">data</span>

<span class="n">depth</span> <span class="o">=</span> <span class="mi">0</span>
<span class="n">hor</span> <span class="o">=</span> <span class="mi">0</span>

<span class="k">for</span> <span class="n">l</span> <span class="ow">in</span> <span class="nb">input</span><span class="o">.</span><span class="n">splitlines</span><span class="p">():</span>
    <span class="nb">dir</span><span class="p">,</span> <span class="n">amount</span> <span class="o">=</span> <span class="n">l</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">&quot; &quot;</span><span class="p">)</span>
    <span class="n">amount</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">amount</span><span class="p">)</span>
    <span class="k">if</span> <span class="nb">dir</span> <span class="o">==</span> <span class="s2">&quot;forward&quot;</span><span class="p">:</span>
        <span class="n">hor</span> <span class="o">+=</span> <span class="n">amount</span>
    <span class="k">elif</span> <span class="nb">dir</span> <span class="o">==</span> <span class="s2">&quot;down&quot;</span><span class="p">:</span>
        <span class="n">depth</span> <span class="o">+=</span> <span class="n">amount</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">depth</span> <span class="o">-=</span> <span class="n">amount</span>

<span class="nb">print</span><span class="p">(</span><span class="n">depth</span> <span class="o">*</span> <span class="n">hor</span><span class="p">)</span>
</pre></div>
</div>
      <div class="flex-1">
        <p>
          Message to user
        </p>
        <input class="hidden" id="code" value="input = """\
forward 5
down 5
forward 8
up 3
down 8
forward 2"""

# part 1

with open("2021/day2/data.txt") as inputfh:
    data = inputfh.read()
input = data

depth = 0
hor = 0

for l in input.splitlines():
    dir, amount = l.split(" ")
    amount = int(amount)
    if dir == "forward":
        hor += amount
    elif dir == "down":
        depth += amount
    else:
        depth -= amount

print(depth * hor)
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