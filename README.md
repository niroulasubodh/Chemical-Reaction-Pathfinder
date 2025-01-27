# Chemical-Reaction-Pathfinder

This program is designed to optimize simple chemical reaction pathways using the principles of graph theory and Dijkstra's algorithm. It allows users to model chemical reactions as a weighted graph, where nodes (vertices) represent chemical compounds, and edges represent reactions, with weights corresponding to reaction costs (e.g., energy, time, or yield).

The tool calculates the shortest reaction pathway between two compounds, providing chemists with an efficient method to optimize chemical synthesis processes.

# Example Usage

## User Input:
Enter reaction: Ethanol Acetaldehyde 5.2
Enter reaction: Ethanol AceticAcid 7.1
Enter reaction: Acetaldehyde AceticAcid 2.3
Enter reaction: Acetaldehyde EthylAcetate 4.5
Enter reaction: AceticAcid EthylAcetate 3.7
Enter reaction: done

## Output (Graph): 
Chemical Reaction Network Graph:
Ethanol --[5.2]--> Acetaldehyde
Ethanol --[7.1]--> AceticAcid
Acetaldehyde --[2.3]--> AceticAcid
Acetaldehyde --[4.5]--> EthylAcetate
AceticAcid --[3.7]--> EthylAcetate

## Pathway Calculation:
Enter the starting compound: Ethanol
Enter the target compound: EthylAcetate

## Output (Shortest Pathway and Reaction Cost):
Shortest Reaction Pathway: Ethanol -> Acetaldehyde -> EthylAcetate
Total Reaction Cost: 9.7

# Acknowledgment

This project was developed as part of the Discrete Mathematics course. The idea for the project was conceived by me and my classmate, Yoichi Watanabe. I would also like to acknowledge Professor Sonwabile Mafunda for teaching graph theory concepts and assigning this project.
