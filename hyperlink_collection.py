import os
from metaphor_python import Metaphor
import networkx as nx
import matplotlib.pyplot as plt
import hashlib

class MetaphorDeepSearch:
    def __init__(self, api_key: str):
        self.api = Metaphor(api_key)
        self.visited_nodes = set()

    def deep_search(self, query: str, initial_depth: int) -> nx.DiGraph:
        graph = nx.DiGraph()
        initial_response = self.api.search(query=query, type='neural', num_results=1)
        if initial_response.results:
            first_id = initial_response.results[0].id
            self._recursive_search(first_id, initial_depth, graph)
        return graph

    def _recursive_search(self, content_id, depth: int, graph: nx.DiGraph) -> None:
        if depth == 0 or content_id in self.visited_nodes:
            return

        # Mark the content ID as visited
        self.visited_nodes.add(content_id)

        try:
            # Fetch content and title for the current content_id
            contents = self.api.get_contents([content_id])
            if not contents.contents:
                return

            content = contents.contents[0]
            url = content.url
            title = content.title  # Adjust if this field doesn't exist; using placeholder here
            summary = content.extract
    
            # Add the current node with its summary
            graph.add_node(content_id, title=title, summary=summary)

            # Use find_similar to get IDs related to the current URL
            similar_results = self.api.find_similar(url, num_results=10)
            similar_ids = [res.id for res in similar_results.results[8:]]
    
            for link_id in similar_ids:
                # Recurse into the similar link by its ID
                self._recursive_search(link_id, depth - 1, graph)
        
                # Now that the recursive search is done, check if both nodes exist before adding the edge.
                if content_id in graph.nodes and link_id in graph.nodes:
                    graph.add_edge(content_id, link_id)

        except Exception as e:
            print(f"Error processing content ID '{content_id}': {e}")

    @staticmethod
    def generate_hash_code(content: str) -> str:
        hash_object = hashlib.sha256(content.encode())
        return hash_object.hexdigest()[:8]

    def save_to_markdown(self, graph: nx.DiGraph, output_dir: str) -> None:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Generate hash codes for nodes
        for node, data in graph.nodes(data=True):
            content = f"# {data['title']}\n\n{data['summary']}\n\n"
            content_hash = self.generate_hash_code(content)
            # Store hash code in node's data
            data['hash'] = content_hash

        for node, data in graph.nodes(data=True):
            sanitized_title = ''.join([c if c.isalnum() else '-' for c in data['title']])
            file_name = f"{sanitized_title}-{data['hash']}.md"
            file_path = os.path.join(output_dir, file_name)

            with open(file_path, "w", encoding="utf-8") as file:
                file.write(f"# {data['title']}\n\n")
                file.write(data['summary'] + "\n\n")
            
                related_links = []
                for neighbor in graph.neighbors(node):
                    neighbor_data = graph.nodes[neighbor]
                    sanitized_neighbor_title = ''.join([c if c.isalnum() else '-' for c in neighbor_data['title']])
                    neighbor_file_name = f"{sanitized_neighbor_title}-{neighbor_data['hash']}.md"
                    related_links.append(f"[[{neighbor_file_name.replace('.md', '')}]]")
            
                if related_links:
                    file.write("## Related Links\n")
                    file.write('\n'.join(related_links))



if __name__ == "__main__":
    api_key = input("What is your API key?\n")
    searcher = MetaphorDeepSearch(api_key)
    user_query = input("What would you like notes on?\n")
    # How deep the graph should be
    user_depth = int(input("How deep would you like the search to be? Answer should be a number\n"))
    graph = searcher.deep_search(user_query, user_depth)
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=2000, edge_color='gray', width=1.5, font_size=15, alpha=0.6, arrowsize=20)
    plt.title("Networkx Graph Visualization")
    plt.show()
    obsidian_path = input("What's the path for your Obsidian vault?\n")
    searcher.save_to_markdown(graph, obsidian_path)
