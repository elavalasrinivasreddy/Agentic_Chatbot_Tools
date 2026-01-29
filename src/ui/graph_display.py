class GraphDisplay:
    def __init__(self):
        pass
    
    # Display the graph in mermaid
    def display_graph(self, graph):
        # Image(graph.get_graph().draw_mermaid_png())
        print(graph.get_graph().draw_ascii())
        # print(graph.get_graph().draw_mermaid())