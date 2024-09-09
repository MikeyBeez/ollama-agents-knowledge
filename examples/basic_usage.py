from ollama_agents_knowledge import kb_graph, knowledge_extraction, memory_search

# Example usage of kb_graph
kb_graph.create_edge("concept1", "concept2", "RELATED_TO", 0.8)
related_nodes = kb_graph.get_related_nodes("concept1")
print("Related nodes:", related_nodes)

# Example usage of knowledge_extraction
text = "Apple Inc. was founded by Steve Jobs in California."
extracted_knowledge = knowledge_extraction.extract_knowledge(text)
print("Extracted knowledge:", extracted_knowledge)

# Example usage of memory_search
query = "Apple company"
search_results = memory_search.search_memories(query, top_k=3)
print("Search results:", search_results)
