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
        day12
    </h1>
    <div class="flex mt-3">
      <div class="flex-1"><div class="highlight"><pre><span></span><span class="sd">&quot;&quot;&quot;</span>
<span class="sd">find all the paths. how to fully traverse a graph?</span>

<span class="sd">graph is made up of nodes</span>
<span class="sd">first node is &quot;start&quot;</span>
<span class="sd">nodes are either large or small</span>
<span class="sd">small nodes cannot be visited more than once</span>
<span class="sd">large nodes can be visited any number of times</span>
<span class="sd">find all the possible paths</span>

<span class="sd">rules:</span>

<span class="sd">- don&#39;t go back to start</span>
<span class="sd">- path ends at end</span>

<span class="sd">&quot;&quot;&quot;</span>
<span class="kn">from</span> <span class="nn">collections</span> <span class="kn">import</span> <span class="n">defaultdict</span>

<span class="kn">from</span> <span class="nn">rich</span> <span class="kn">import</span> <span class="nb">print</span>

<span class="nb">input</span> <span class="o">=</span> <span class="s2">&quot;&quot;&quot;</span><span class="se">\</span>
<span class="s2">start-A</span>
<span class="s2">start-b</span>
<span class="s2">A-c</span>
<span class="s2">A-b</span>
<span class="s2">b-d</span>
<span class="s2">A-end</span>
<span class="s2">b-end&quot;&quot;&quot;</span>

<span class="nb">input</span> <span class="o">=</span> <span class="s2">&quot;&quot;&quot;</span><span class="se">\</span>
<span class="s2">dc-end</span>
<span class="s2">HN-start</span>
<span class="s2">start-kj</span>
<span class="s2">dc-start</span>
<span class="s2">dc-HN</span>
<span class="s2">LN-dc</span>
<span class="s2">HN-end</span>
<span class="s2">kj-sa</span>
<span class="s2">kj-HN</span>
<span class="s2">kj-dc&quot;&quot;&quot;</span>

<span class="nb">input</span> <span class="o">=</span> <span class="s2">&quot;&quot;&quot;</span><span class="se">\</span>
<span class="s2">fs-end</span>
<span class="s2">he-DX</span>
<span class="s2">fs-he</span>
<span class="s2">start-DX</span>
<span class="s2">pj-DX</span>
<span class="s2">end-zg</span>
<span class="s2">zg-sl</span>
<span class="s2">zg-pj</span>
<span class="s2">pj-he</span>
<span class="s2">RW-he</span>
<span class="s2">fs-DX</span>
<span class="s2">pj-RW</span>
<span class="s2">zg-RW</span>
<span class="s2">start-pj</span>
<span class="s2">he-WI</span>
<span class="s2">zg-he</span>
<span class="s2">pj-fs</span>
<span class="s2">start-RW&quot;&quot;&quot;</span>

<span class="nb">input</span> <span class="o">=</span> <span class="s2">&quot;&quot;&quot;</span><span class="se">\</span>
<span class="s2">ma-start</span>
<span class="s2">YZ-rv</span>
<span class="s2">MP-rv</span>
<span class="s2">vc-MP</span>
<span class="s2">QD-kj</span>
<span class="s2">rv-kj</span>
<span class="s2">ma-rv</span>
<span class="s2">YZ-zd</span>
<span class="s2">UB-rv</span>
<span class="s2">MP-xe</span>
<span class="s2">start-MP</span>
<span class="s2">zd-end</span>
<span class="s2">ma-UB</span>
<span class="s2">ma-MP</span>
<span class="s2">UB-xe</span>
<span class="s2">end-UB</span>
<span class="s2">ju-MP</span>
<span class="s2">ma-xe</span>
<span class="s2">zd-UB</span>
<span class="s2">start-xe</span>
<span class="s2">YZ-end&quot;&quot;&quot;</span>

<span class="n">graph</span> <span class="o">=</span> <span class="n">defaultdict</span><span class="p">(</span><span class="nb">set</span><span class="p">)</span>
<span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="nb">input</span><span class="o">.</span><span class="n">splitlines</span><span class="p">():</span>
    <span class="n">node1</span><span class="p">,</span> <span class="n">node2</span> <span class="o">=</span> <span class="n">line</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s2">&quot;-&quot;</span><span class="p">)</span>
    <span class="n">graph</span><span class="p">[</span><span class="n">node1</span><span class="p">]</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">node2</span><span class="p">)</span>
    <span class="n">graph</span><span class="p">[</span><span class="n">node2</span><span class="p">]</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">node1</span><span class="p">)</span>

<span class="c1"># print(graph)</span>


<span class="k">def</span> <span class="nf">traverse_graph</span><span class="p">():</span>
    <span class="c1"># always start at start</span>
    <span class="n">paths</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">node_stack</span> <span class="o">=</span> <span class="p">[([</span><span class="s2">&quot;start&quot;</span><span class="p">],</span> <span class="n">n</span><span class="p">)</span> <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="n">graph</span><span class="p">[</span><span class="s2">&quot;start&quot;</span><span class="p">]]</span>

    <span class="k">while</span> <span class="nb">len</span><span class="p">(</span><span class="n">node_stack</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
        <span class="n">path</span><span class="p">,</span> <span class="n">node</span> <span class="o">=</span> <span class="n">node_stack</span><span class="o">.</span><span class="n">pop</span><span class="p">()</span>
        <span class="n">path</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">node</span><span class="p">)</span>

        <span class="k">if</span> <span class="n">node</span> <span class="o">==</span> <span class="s2">&quot;end&quot;</span><span class="p">:</span>
            <span class="n">paths</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">path</span><span class="p">)</span>
            <span class="k">continue</span>

        <span class="n">new_nodes</span> <span class="o">=</span> <span class="n">graph</span><span class="p">[</span><span class="n">node</span><span class="p">]</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span>

        <span class="c1"># we don&#39;t go back to start</span>
        <span class="n">new_nodes</span> <span class="o">-=</span> <span class="p">{</span><span class="s2">&quot;start&quot;</span><span class="p">}</span>

        <span class="c1"># if we&#39;re trying to visit a node of lowercase more than once we terminate that path</span>
        <span class="n">rem_nodes</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">n</span> <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="n">new_nodes</span> <span class="k">if</span> <span class="n">n</span> <span class="ow">in</span> <span class="n">path</span> <span class="ow">and</span> <span class="n">n</span><span class="o">.</span><span class="n">islower</span><span class="p">())</span>
        <span class="n">new_nodes</span> <span class="o">-=</span> <span class="n">rem_nodes</span>

        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">new_nodes</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
            <span class="k">continue</span>

        <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="n">new_nodes</span><span class="p">:</span>
            <span class="n">node_stack</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">path</span><span class="o">.</span><span class="n">copy</span><span class="p">(),</span> <span class="n">n</span><span class="p">))</span>

    <span class="k">return</span> <span class="n">paths</span>


<span class="n">paths</span> <span class="o">=</span> <span class="n">traverse_graph</span><span class="p">()</span>
<span class="c1"># print(sorted(paths))</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">paths</span><span class="p">))</span>
</pre></div>
</div>
      <div class="flex-1">
        <p>
          Message to user
        </p>
        <input class="hidden" id="code" value=""""
find all the paths. how to fully traverse a graph?

graph is made up of nodes
first node is "start"
nodes are either large or small
small nodes cannot be visited more than once
large nodes can be visited any number of times
find all the possible paths

rules:

- don't go back to start
- path ends at end

"""
from collections import defaultdict

from rich import print

input = """\
start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

input = """\
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

input = """\
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""

input = """\
ma-start
YZ-rv
MP-rv
vc-MP
QD-kj
rv-kj
ma-rv
YZ-zd
UB-rv
MP-xe
start-MP
zd-end
ma-UB
ma-MP
UB-xe
end-UB
ju-MP
ma-xe
zd-UB
start-xe
YZ-end"""

graph = defaultdict(set)
for line in input.splitlines():
    node1, node2 = line.split("-")
    graph[node1].add(node2)
    graph[node2].add(node1)

# print(graph)


def traverse_graph():
    # always start at start
    paths = []
    node_stack = [(["start"], n) for n in graph["start"]]

    while len(node_stack) > 0:
        path, node = node_stack.pop()
        path.append(node)

        if node == "end":
            paths.append(path)
            continue

        new_nodes = graph[node].copy()

        # we don't go back to start
        new_nodes -= {"start"}

        # if we're trying to visit a node of lowercase more than once we terminate that path
        rem_nodes = set(n for n in new_nodes if n in path and n.islower())
        new_nodes -= rem_nodes

        if len(new_nodes) == 0:
            continue

        for n in new_nodes:
            node_stack.append((path.copy(), n))

    return paths


paths = traverse_graph()
# print(sorted(paths))
print(len(paths))
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