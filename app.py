import streamlit as st
import dijkstra

# Import other algorithm modules here

st.set_page_config(page_title="DSA Factory", page_icon="🏭", layout="wide")


def main():
    st.title("DSA Factory 🏭")
    st.write("Welcome to DSA Factory! Choose an algorithm to visualize and learn.")

    algorithm = st.sidebar.selectbox(
        "Select an Algorithm",
        ["Home", "Dijkstra's Algorithm", "Binary Search", "Quick Sort", "LRU Cache"]
    )

    if algorithm == "Home":
        st.write("## Learn Data Structures and Algorithms Interactively")
        st.write("This app provides interactive visualizations for various DSA concepts. "
                 "Select an algorithm from the sidebar to get started!")

        st.write("### Available Algorithms:")
        st.write("1. Dijkstra's Algorithm - Shortest path in weighted graphs")
        st.write("2. Binary Search - Efficient searching in sorted arrays")
        st.write("3. Quick Sort - Fast sorting algorithm")
        st.write("4. LRU Cache - Least Recently Used caching mechanism")

    elif algorithm == "Dijkstra's Algorithm":
        dijkstra.run()

    # Add elif statements for other algorithms here

main()