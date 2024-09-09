from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ollama-agents-knowledge",
    version="0.1.0",
    author="Mike Bee",
    author_email="mbonsign@gmail.com",
    description="Knowledge management and graph operations for Ollama Agents",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MikeyBeez/ollama-agents-knowledge",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy",
        "ollama",
        "rich",
        "spacy",
        "scikit-learn",
        "networkx",
        "sqlite3",  # This is part of Python's standard library, so you don't need to include it
    ],
    extras_require={
        "dev": [
            "pytest",
            "pytest-cov",
            "flake8",
            "black",
            "mypy",
        ],
    },
    entry_points={
        "console_scripts": [
            "ollama-knowledge=ollama_agents_knowledge.cli:main",
        ],
    },
)
