#Project Idea: Subodh Niroula, Yoichi Watanabe  

import heapq
from typing import Dict, List, Tuple

class ChemicalPathfinder:
    def __init__(self):
        """
        Initialize the chemical reaction network graph.
        Stores connections between compounds and their reaction costs.
        """
        self.graph = {}
    
    def add_reaction(self, start_compound: str, end_compound: str, reaction_cost: float):
        """
        Add a chemical reaction pathway between compounds.
        
        :param start_compound: Starting molecular/chemical compound
        :param end_compound: Target molecular/chemical compound
        :param reaction_cost: Cost of the reaction (e.g., energy, time, yield)
        """
        if start_compound not in self.graph:
            self.graph[start_compound] = []
        
        self.graph[start_compound].append((end_compound, reaction_cost))
        
        # Ensure all compounds are included in the graph (even if they don't have outgoing edges)
        if end_compound not in self.graph:
            self.graph[end_compound] = []
    
    def find_shortest_pathway(self, start: str, end: str) -> Tuple[List[str], float]:
        """
        Find the shortest pathway between two chemical compounds using Dijkstra's algorithm.
        
        :param start: Starting compound
        :param end: Target compound
        :return: Tuple of (pathway, total reaction cost)
        """
        if start not in self.graph:
            return [], float('inf')
        
        # Distance tracking
        distances = {compound: float('inf') for compound in self.graph}
        distances[start] = 0
        
        # Previous compound tracking for path reconstruction
        previous = {compound: None for compound in self.graph}
        
        # Priority queue for efficient node selection
        pq = [(0, start)]
        
        while pq:
            current_distance, current_compound = heapq.heappop(pq)
            
            # Stop if we've reached the target compound
            if current_compound == end:
                break
            
            # If we've found a longer path, skip
            if current_distance > distances[current_compound]:
                continue
            
            # Check all possible reactions from current compound
            if current_compound in self.graph:
                for neighbor, reaction_cost in self.graph[current_compound]:
                    distance = current_distance + reaction_cost
                    
                    # Update if we've found a shorter path
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        previous[neighbor] = current_compound
                        heapq.heappush(pq, (distance, neighbor))
        
        # Reconstruct the pathway
        if distances[end] == float('inf'):
            return [], float('inf')  # No path found
        
        pathway = []
        current = end
        while current is not None:
            pathway.insert(0, current)
            current = previous[current]
        
        return pathway, distances[end]
    
    def display_graph(self):
        """
        Display the chemical reaction network as ASCII art.
        """
        print("\nChemical Reaction Network Graph:")
        for start_compound, edges in self.graph.items():
            for end_compound, cost in edges:
                print(f"{start_compound} --[{cost}]--> {end_compound}")
        print()


# Example Usage
def main():
    pathfinder = ChemicalPathfinder()
    
    print("Enter reactions in the format:")
    print("StartCompound EndCompound ReactionCost")
    print("Type 'done' to finish entering reactions.\n")
    
    # Take user inputs for reactions
    while True:
        user_input = input("Enter reaction: ").strip()
        if user_input.lower() == "done":
            break
        
        try:
            start, end, cost = user_input.split()
            cost = float(cost)
            pathfinder.add_reaction(start, end, cost)
        except ValueError:
            print("Invalid input format. Please use: StartCompound EndCompound ReactionCost")
    
    # Display the reaction network graph
    pathfinder.display_graph()
    
    # Get the start and end compounds for the pathway calculation
    start_compound = input("Enter the starting compound: ").strip()
    end_compound = input("Enter the target compound: ").strip()
    
    # Find and display the shortest pathway
    pathway, total_cost = pathfinder.find_shortest_pathway(start_compound, end_compound)
    
    if pathway:
        print("\nShortest Reaction Pathway:", " -> ".join(pathway))
        print(f"Total Reaction Cost: {total_cost}")
    else:
        print("\nNo pathway found between the specified compounds.")

if __name__ == "__main__":
    main()
