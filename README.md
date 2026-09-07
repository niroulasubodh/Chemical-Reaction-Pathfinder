# Chemical-Reaction-Pathfinder

This program models simple chemical reaction pathways as a weighted, directed graph and finds the lowest-cost pathway between two compounds using **Dijkstra's algorithm**.

Nodes represent chemical compounds, and directed edges represent reactions, weighted by a "reaction cost" (e.g., energy required, time, or inverse yield). The tool computes the shortest (lowest-cost) reaction pathway between a starting compound and a target compound, giving chemists a quick way to compare synthesis routes.

Two implementations are provided:

- **`pathfinder.py`** — command-line Python tool (original)
- **`pathfinder.html`** — interactive, browser-based version with no install required (new)

---

## How It Works (Python version)

The `ChemicalPathfinder` class stores the reaction network as an adjacency list (`self.graph`), mapping each compound to a list of `(neighbor, cost)` tuples.

### Core methods

| Method | Description |
|---|---|
| `add_reaction(start, end, cost)` | Adds a directed, weighted edge from `start` to `end`. Automatically registers both compounds as nodes, even if `end` has no outgoing reactions. |
| `find_shortest_pathway(start, end)` | Runs Dijkstra's algorithm from `start` using a binary heap priority queue. Returns the compound sequence and total cost, or `([], inf)` if no path exists or `start` isn't in the graph. |
| `display_graph()` | Prints every reaction edge as ASCII text in the form `A --[cost]--> B`. |

### Algorithm notes

- Reactions are **directed** (A → B does not imply B → A) — add both edges manually if a reaction is reversible.
- Reaction costs should be **non-negative**, as Dijkstra's algorithm does not support negative edge weights.
- The search terminates early once the target compound is popped from the priority queue (standard Dijkstra optimization).
- If a compound is entered as a start/end node but never added via `add_reaction`, it won't exist in the graph and pathfinding will report no path found.

### Running the Python version

```bash
python pathfinder.py
```

You'll be prompted to enter reactions interactively, then a start and target compound.

---

## Example Usage

### User Input
```
Enter reaction: Ethanol Acetaldehyde 5.2
Enter reaction: Ethanol AceticAcid 7.1
Enter reaction: Acetaldehyde AceticAcid 2.3
Enter reaction: Acetaldehyde EthylAcetate 4.5
Enter reaction: AceticAcid EthylAcetate 3.7
Enter reaction: done
```

### Output (Graph)
```
Chemical Reaction Network Graph:
Ethanol --[5.2]--> Acetaldehyde
Ethanol --[7.1]--> AceticAcid
Acetaldehyde --[2.3]--> AceticAcid
Acetaldehyde --[4.5]--> EthylAcetate
AceticAcid --[3.7]--> EthylAcetate
```

### Pathway Calculation
```
Enter the starting compound: Ethanol
Enter the target compound: EthylAcetate
```

### Output (Shortest Pathway and Reaction Cost)
```
Shortest Reaction Pathway: Ethanol -> Acetaldehyde -> EthylAcetate
Total Reaction Cost: 9.7
```

---

## Interactive Web Version (`pathfinder.html`)

An interactive, self-contained HTML/JavaScript port of the same Dijkstra-based logic. Just open the file in any browser — no server or dependencies needed.

Features:
- Add reactions through a form (start compound, end compound, cost)
- Live-updating table and visual graph diagram of all reactions
- Select start/target compound and instantly compute the shortest pathway and total cost
- Highlights the resulting path on the diagram
- Load the example dataset above with one click
- Reset/clear the network at any time

---

## Acknowledgment

This project was developed as part of the Discrete Mathematics course. I would like to acknowledge Professor Sonwabile Mafunda for teaching graph theory concepts and assigning this project.
