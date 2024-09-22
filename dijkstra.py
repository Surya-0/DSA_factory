import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgba


def run():
    st.title("Dijkstra's Algorithm Visualization")
    st.write("This page demonstrates how Dijkstra's algorithm finds the shortest path in a weighted graph.")

    # Create a sample graph
    G = nx.Graph()
    G.add_edges_from([
        ('A', 'B', {'weight': 4}),
        ('A', 'C', {'weight': 2}),
        ('B', 'D', {'weight': 3}),
        ('B', 'E', {'weight': 1}),
        ('C', 'D', {'weight': 5}),
        ('D', 'E', {'weight': 2})
    ])

    # Initialize algorithm state
    if 'step' not in st.session_state:
        st.session_state.step = 0
        st.session_state.distances = {node: float('inf') for node in G.nodes()}
        st.session_state.distances['A'] = 0
        st.session_state.visited = set()
        st.session_state.path = {}

    # Dijkstra's algorithm step
    def dijkstra_step():
        if len(st.session_state.visited) == len(G.nodes()):
            return False

        # Find the node with the minimum distance
        current_node = min(
            (node for node in G.nodes() if node not in st.session_state.visited),
            key=lambda x: st.session_state.distances[x]
        )

        # Mark the current node as visited
        st.session_state.visited.add(current_node)

        # Update distances to neighboring nodes
        for neighbor in G.neighbors(current_node):
            if neighbor not in st.session_state.visited:
                new_distance = st.session_state.distances[current_node] + G[current_node][neighbor]['weight']
                if new_distance < st.session_state.distances[neighbor]:
                    st.session_state.distances[neighbor] = new_distance
                    st.session_state.path[neighbor] = current_node

        st.session_state.step += 1
        return True

    # Visualization
    def visualize_graph():
        plt.figure(figsize=(10, 6))
        pos = nx.spring_layout(G)

        # Draw edges
        nx.draw_networkx_edges(G, pos, alpha=0.2)

        # Draw nodes
        node_colors = ['lightblue' if node not in st.session_state.visited else 'lightgreen' for node in G.nodes()]
        nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=500)

        # Draw labels
        labels = {node: f"{node}\n{st.session_state.distances[node]}" for node in G.nodes()}
        nx.draw_networkx_labels(G, pos, labels, font_size=10)

        # Draw edge labels
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        # Highlight the path
        path_edges = [(st.session_state.path[node], node) for node in st.session_state.path]
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)

        st.pyplot(plt)

    # Streamlit interface
    col1, col2 = st.columns([3, 1])

    with col1:
        visualize_graph()

    with col2:
        st.write(f"Step: {st.session_state.step}")
        st.write("Distances:")
        for node, distance in st.session_state.distances.items():
            st.write(f"{node}: {distance}")

        if st.button("Next Step"):
            if not dijkstra_step():
                st.write("Algorithm completed!")

        if st.button("Reset"):
            st.session_state.step = 0
            st.session_state.distances = {node: float('inf') for node in G.nodes()}
            st.session_state.distances['A'] = 0
            st.session_state.visited = set()
            st.session_state.path = {}
            st.experimental_rerun()

    # Explanation
    st.write("## How Dijkstra's Algorithm Works")
    st.write("1. Initialize distances: Set the distance to the start node (A) as 0 and all other nodes as infinity.")
    st.write("2. Select the unvisited node with the smallest distance as the current node.")
    st.write("3. For each neighbor of the current node:")
    st.write("   - Calculate the distance through the current node.")
    st.write("   - If this distance is less than the previously recorded distance, update it.")
    st.write("4. Mark the current node as visited.")
    st.write("5. Repeat steps 2-4 until all nodes are visited.")
    st.write("6. The shortest path can be reconstructed using the recorded distances and paths.")
