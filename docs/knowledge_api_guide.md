# Ollama Agents Knowledge API Guide

This guide describes how to use the `ollama-agents-knowledge` package in your projects. The package provides functionality for knowledge graph operations, knowledge extraction, and memory search.

## Installation

First, install the package using pip:

```bash
pip install git+https://github.com/MikeyBeez/ollama-agents-knowledge.git
```

## Importing Modules

After installation, you can import the modules as follows:

```python
from ollama_agents_knowledge import kb_graph, knowledge_extraction, memory_search
```

## KB Graph Module

The `kb_graph` module provides functions for managing a knowledge graph.

### Creating an Edge

```python
from ollama_agents_knowledge.kb_graph import create_edge

create_edge("concept1", "concept2", "RELATED_TO", 0.8)
```

This creates a relationship between two concepts in the knowledge graph.

### Getting Related Nodes

```python
from ollama_agents_knowledge.kb_graph import get_related_nodes

related_nodes = get_related_nodes("concept1")
print(related_nodes)
```

This retrieves nodes related to a given concept.

### Analyzing File Pairs

```python
from ollama_agents_knowledge.kb_graph import analyze_file_pair

file1 = {
    "title": "Python Basics",
    "content": "Python is a programming language.",
    "tags": ["python", "programming"],
    "timestamp": "2023-05-01T10:00:00Z"
}
file2 = {
    "title": "Python in Data Science",
    "content": "Python is used in data analysis.",
    "tags": ["python", "data science"],
    "timestamp": "2023-05-01T11:00:00Z"
}

categories = analyze_file_pair(file1, file2)
print(categories)
```

This analyzes the similarity and relationships between two files.

## Knowledge Extraction Module

The `knowledge_extraction` module provides functions for extracting knowledge from text.

### Extracting Knowledge

```python
from ollama_agents_knowledge.knowledge_extraction import extract_knowledge

text = "Apple Inc. was founded by Steve Jobs in California."
knowledge = extract_knowledge(text)
print(knowledge)
```

This extracts various types of knowledge from the given text, including key concepts, named entities, relationships, topic, and sentiment.

## Memory Search Module

The `memory_search` module provides functions for searching through stored memories.

### Searching Memories

```python
from ollama_agents_knowledge.memory_search import search_memories

query = "Python programming"
results = search_memories(query, top_k=5, similarity_threshold=0.5)
print(results)
```

This searches for memories related to the given query, returning the top k results above the specified similarity threshold.

### Getting Embeddings

```python
from ollama_agents_knowledge.memory_search import get_embeddings

filename = "memory_file.json"
embeddings = get_embeddings(filename)
print(embeddings)
```

This retrieves or generates embeddings for a given memory file.

### Finding Most Similar

```python
from ollama_agents_knowledge.memory_search import find_most_similar

needle = [1, 1, 0]
haystack = [[1, 0, 0], [0, 1, 0], [1, 1, 1]]
similarities = find_most_similar(needle, haystack)
print(similarities)
```

This finds the most similar vectors in a haystack given a needle vector.

## Configuration

The package uses configuration values from a `config.py` file. You may need to set up this file in your project with the following variables:

- `DATA_DIR`: Directory for storing memory files
- `EMBEDDINGS_DIR`: Directory for storing embeddings
- `EMBEDDING_MODEL`: Name of the embedding model to use
- `DEFAULT_MODEL`: Default language model to use

Example `config.py`:

```python
from pathlib import Path

DATA_DIR = Path('data/memories')
EMBEDDINGS_DIR = Path('data/embeddings')
EMBEDDING_MODEL = 'text-embedding-ada-002'
DEFAULT_MODEL = 'gpt-3.5-turbo'
```

## Error Handling

Most functions in the package will raise exceptions if they encounter errors. It's recommended to use try-except blocks when calling these functions to handle potential errors gracefully.

## Logging

The package uses Python's built-in logging module. You can configure logging in your main application to capture log messages from the ollama-agents-knowledge package.

```python
import logging

logging.basicConfig(level=logging.INFO)
```

## Threading and Concurrency

The package is not explicitly designed for concurrent use. If you need to use it in a multi-threaded environment, you may need to implement your own synchronization mechanisms.

## Data Persistence

The KB Graph module uses SQLite for data persistence. The database file location is determined by the `DB_PATH` variable in the `kb_graph` module.

## Conclusion

This API provides a powerful set of tools for knowledge management, extraction, and search. By integrating these functions into your project, you can create sophisticated AI agents capable of managing and utilizing complex knowledge structures.

Remember to refer to the source code and inline documentation for more detailed information about each function and its parameters.
