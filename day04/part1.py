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
        day04
    </h1>
    <div class="flex mt-3">
      <div class="flex-1"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>

<span class="nb">input</span> <span class="o">=</span> <span class="s2">&quot;&quot;&quot;</span><span class="se">\</span>
<span class="s2">7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1</span>

<span class="s2">22 13 17 11  0</span>
<span class="s2"> 8  2 23  4 24</span>
<span class="s2">21  9 14 16  7</span>
<span class="s2"> 6 10  3 18  5E</span>
<span class="s2"> 1 12 20 15 19</span>

<span class="s2"> 3 15  0  2 22</span>
<span class="s2"> 9 18 13 17  5</span>
<span class="s2">19  8  7 25 23</span>
<span class="s2">20 11 10 24  4</span>
<span class="s2">14 21 16 12  6</span>

<span class="s2">14 21 17 24  4</span>
<span class="s2">10 16 15  9 19</span>
<span class="s2">18  8 23 26 20</span>
<span class="s2">22 11 13  6  5</span>
<span class="s2"> 2  0 12  3  7&quot;&quot;&quot;</span>

<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="s2">&quot;2021/day04/data.txt&quot;</span><span class="p">)</span> <span class="k">as</span> <span class="n">fh</span><span class="p">:</span>
    <span class="nb">input</span> <span class="o">=</span> <span class="n">fh</span><span class="o">.</span><span class="n">read</span><span class="p">()</span>

<span class="n">board_data_list</span> <span class="o">=</span> <span class="p">[]</span>

<span class="k">for</span> <span class="n">i</span><span class="p">,</span> <span class="n">line</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="nb">input</span><span class="o">.</span><span class="n">splitlines</span><span class="p">()):</span>
    <span class="k">if</span> <span class="n">i</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
        <span class="n">draw_nums</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="nb">map</span><span class="p">(</span><span class="nb">int</span><span class="p">,</span> <span class="n">line</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">&quot;,&quot;</span><span class="p">)))</span>
        <span class="k">continue</span>
    <span class="k">if</span> <span class="n">line</span><span class="p">:</span>
        <span class="n">board_data_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="nb">list</span><span class="p">(</span><span class="nb">map</span><span class="p">(</span><span class="nb">int</span><span class="p">,</span> <span class="n">line</span><span class="o">.</span><span class="n">split</span><span class="p">())))</span>

<span class="n">all_board_data</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">board_data_list</span><span class="p">)</span>
<span class="n">boards</span> <span class="o">=</span> <span class="n">np</span><span class="o">.</span><span class="n">array_split</span><span class="p">(</span><span class="n">all_board_data</span><span class="p">,</span> <span class="n">all_board_data</span><span class="o">.</span><span class="n">shape</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">/</span> <span class="mi">5</span><span class="p">)</span>


<span class="k">def</span> <span class="nf">calc_answer</span><span class="p">(</span><span class="n">arr</span><span class="p">,</span> <span class="n">draw</span><span class="p">):</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">draw</span> <span class="o">*</span> <span class="n">np</span><span class="o">.</span><span class="n">sum</span><span class="p">(</span><span class="n">arr</span><span class="p">[</span><span class="n">arr</span> <span class="o">!=</span> <span class="o">-</span><span class="mi">1</span><span class="p">]))</span>


<span class="k">for</span> <span class="n">draw</span> <span class="ow">in</span> <span class="n">draw_nums</span><span class="p">:</span>
    <span class="k">for</span> <span class="n">board</span> <span class="ow">in</span> <span class="n">boards</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">draw</span> <span class="ow">in</span> <span class="n">board</span><span class="p">:</span>
            <span class="n">board</span><span class="p">[</span><span class="n">board</span> <span class="o">==</span> <span class="n">draw</span><span class="p">]</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span>

            <span class="k">for</span> <span class="n">row</span> <span class="ow">in</span> <span class="n">board</span><span class="p">:</span>
                <span class="k">if</span> <span class="n">np</span><span class="o">.</span><span class="n">all</span><span class="p">(</span><span class="n">row</span> <span class="o">==</span> <span class="o">-</span><span class="mi">1</span><span class="p">):</span>
                    <span class="c1"># we have a winner</span>
                    <span class="n">calc_answer</span><span class="p">(</span><span class="n">board</span><span class="p">,</span> <span class="n">draw</span><span class="p">)</span>
                    <span class="k">raise</span> <span class="p">(</span><span class="ne">SystemExit</span><span class="p">)</span>
            <span class="k">for</span> <span class="n">col</span> <span class="ow">in</span> <span class="n">board</span><span class="o">.</span><span class="n">transpose</span><span class="p">():</span>
                <span class="k">if</span> <span class="n">np</span><span class="o">.</span><span class="n">all</span><span class="p">(</span><span class="n">col</span> <span class="o">==</span> <span class="o">-</span><span class="mi">1</span><span class="p">):</span>
                    <span class="c1"># we have a winner</span>
                    <span class="n">calc_answer</span><span class="p">(</span><span class="n">board</span><span class="p">,</span> <span class="n">draw</span><span class="p">)</span>
                    <span class="k">raise</span> <span class="p">(</span><span class="ne">SystemExit</span><span class="p">)</span>
            <span class="c1"># if np.all(board.diagonal() == -1):</span>
            <span class="c1">#     # we have a winner</span>
            <span class="c1">#     ...</span>
            <span class="c1">#     raise(SystemExit)</span>
            <span class="c1"># if np.all(np.fliplr(board).diagonal() == -1):</span>
            <span class="c1">#     # we have a winner</span>
            <span class="c1">#     ...</span>
            <span class="c1">#     raise(SystemExit)</span>
</pre></div>
</div>
      <div class="flex-1">
        <p>
          Message to user
        </p>
        <input class="hidden" id="code" value="import numpy as np

input = """\
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5E
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""

with open("2021/day04/data.txt") as fh:
    input = fh.read()

board_data_list = []

for i, line in enumerate(input.splitlines()):
    if i == 0:
        draw_nums = list(map(int, line.split(",")))
        continue
    if line:
        board_data_list.append(list(map(int, line.split())))

all_board_data = np.array(board_data_list)
boards = np.array_split(all_board_data, all_board_data.shape[0] / 5)


def calc_answer(arr, draw):
    print(draw * np.sum(arr[arr != -1]))


for draw in draw_nums:
    for board in boards:
        if draw in board:
            board[board == draw] = -1

            for row in board:
                if np.all(row == -1):
                    # we have a winner
                    calc_answer(board, draw)
                    raise (SystemExit)
            for col in board.transpose():
                if np.all(col == -1):
                    # we have a winner
                    calc_answer(board, draw)
                    raise (SystemExit)
            # if np.all(board.diagonal() == -1):
            #     # we have a winner
            #     ...
            #     raise(SystemExit)
            # if np.all(np.fliplr(board).diagonal() == -1):
            #     # we have a winner
            #     ...
            #     raise(SystemExit)
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