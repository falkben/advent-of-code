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
        day10
    </h1>
    <div class="flex mt-3">
      <div class="flex-1"><div class="highlight"><pre><span></span><span class="sd">&quot;&quot;&quot;corrupted means chunk closed by wrong character</span>

<span class="sd">incomplete means chunk was never closed</span>


<span class="sd">corrupted line is chunk closes with wrong character</span>
<span class="sd">&quot;(]&quot;</span>
<span class="sd">&quot;&quot;&quot;</span>


<span class="nb">input</span> <span class="o">=</span> <span class="s2">&quot;&quot;&quot;</span><span class="se">\</span>
<span class="s2">[({(&lt;(())[]&gt;[[{[]{&lt;()&lt;&gt;&gt;</span>
<span class="s2">[(()[&lt;&gt;])]({[&lt;{&lt;&lt;[]&gt;&gt;(</span>
<span class="s2">{([(&lt;</span><span class="si">{}</span><span class="s2">[&lt;&gt;[]}&gt;{[]{[(&lt;()&gt;</span>
<span class="s2">(((({&lt;&gt;}&lt;{&lt;{&lt;&gt;}{[]{[]</span><span class="si">{}</span><span class="s2"></span>
<span class="s2">[[&lt;[([]))&lt;([[</span><span class="si">{}</span><span class="s2">[[()]]]</span>
<span class="s2">[{[{(</span><span class="si">{}</span><span class="s2">]</span><span class="si">{}</span><span class="s2">}([{[{{</span><span class="si">{}</span><span class="s2">}([]</span>
<span class="s2">{&lt;[[]]&gt;}&lt;{[{[{[]{()[[[]</span>
<span class="s2">[&lt;(&lt;(&lt;(&lt;</span><span class="si">{}</span><span class="s2">))&gt;&lt;([]([]()</span>
<span class="s2">&lt;{([([[(&lt;&gt;())</span><span class="si">{}</span><span class="s2">]&gt;(&lt;&lt;{{</span>
<span class="s2">&lt;{([{{}}[&lt;[[[&lt;&gt;</span><span class="si">{}</span><span class="s2">]]]&gt;[]]</span>
<span class="s2">&quot;&quot;&quot;</span>

<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s2">&quot;2021/day10/data.txt&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">fh</span><span class="p">:</span>
    <span class="nb">input</span> <span class="o">=</span> <span class="n">fh</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>

<span class="n">scoring</span> <span class="o">=</span> <span class="p">{</span>
    <span class="s2">&quot;)&quot;</span><span class="p">:</span> <span class="mi">3</span><span class="p">,</span>
    <span class="s2">&quot;]&quot;</span><span class="p">:</span> <span class="mi">57</span><span class="p">,</span>
    <span class="s2">&quot;}&quot;</span><span class="p">:</span> <span class="mi">1197</span><span class="p">,</span>
    <span class="s2">&quot;&gt;&quot;</span><span class="p">:</span> <span class="mi">25137</span><span class="p">,</span>
<span class="p">}</span>

<span class="n">chunk_brackets</span> <span class="o">=</span> <span class="p">{</span>
    <span class="s2">&quot;)&quot;</span><span class="p">:</span> <span class="s2">&quot;(&quot;</span><span class="p">,</span>
    <span class="s2">&quot;]&quot;</span><span class="p">:</span> <span class="s2">&quot;[&quot;</span><span class="p">,</span>
    <span class="s2">&quot;}&quot;</span><span class="p">:</span> <span class="s2">&quot;{&quot;</span><span class="p">,</span>
    <span class="s2">&quot;&gt;&quot;</span><span class="p">:</span> <span class="s2">&quot;&lt;&quot;</span><span class="p">,</span>
<span class="p">}</span>
<span class="n">opening_chars</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">chunk_brackets</span><span class="o">.</span><span class="n">values</span><span class="p">())</span>
<span class="n">closing_chars</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">chunk_brackets</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span>

<span class="n">score_total</span> <span class="o">=</span> <span class="mi">0</span>
<span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="nb">input</span><span class="o">.</span><span class="n">splitlines</span><span class="p">():</span>

    <span class="n">open_chunks_stack</span> <span class="o">=</span> <span class="p">[]</span>

    <span class="k">for</span> <span class="n">char</span> <span class="ow">in</span> <span class="n">line</span><span class="p">:</span>

        <span class="k">if</span> <span class="n">char</span> <span class="ow">in</span> <span class="n">opening_chars</span><span class="p">:</span>
            <span class="c1"># add to stack</span>
            <span class="n">open_chunks_stack</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">char</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">char</span> <span class="ow">in</span> <span class="n">closing_chars</span><span class="p">:</span>

            <span class="c1"># check if it closes the chunk</span>
            <span class="k">if</span> <span class="n">open_chunks_stack</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span> <span class="o">!=</span> <span class="n">chunk_brackets</span><span class="p">[</span><span class="n">char</span><span class="p">]:</span>
                <span class="c1"># if it doesn&#39;t, we have corr. line</span>
                <span class="n">score_total</span> <span class="o">+=</span> <span class="n">scoring</span><span class="p">[</span><span class="n">char</span><span class="p">]</span>
                <span class="k">break</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="c1"># if it does, we remove from stack</span>
                <span class="n">open_chunks_stack</span><span class="o">.</span><span class="n">pop</span><span class="p">()</span>

<span class="nb">print</span><span class="p">(</span><span class="n">score_total</span><span class="p">)</span>
</pre></div>
</div>
      <div class="flex-1">
        <p>
          Message to user
        </p>
        <input class="hidden" id="code" value=""""corrupted means chunk closed by wrong character

incomplete means chunk was never closed


corrupted line is chunk closes with wrong character
"(]"
"""


input = """\
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""

with open("2021/day10/data.txt") as fh:
    input = fh.read()

scoring = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

chunk_brackets = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}
opening_chars = list(chunk_brackets.values())
closing_chars = list(chunk_brackets.keys())

score_total = 0
for line in input.splitlines():

    open_chunks_stack = []

    for char in line:

        if char in opening_chars:
            # add to stack
            open_chunks_stack.append(char)
        if char in closing_chars:

            # check if it closes the chunk
            if open_chunks_stack[-1] != chunk_brackets[char]:
                # if it doesn't, we have corr. line
                score_total += scoring[char]
                break
            else:
                # if it does, we remove from stack
                open_chunks_stack.pop()

print(score_total)
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