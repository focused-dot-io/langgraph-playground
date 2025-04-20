# LangGraph Playground

This repository contains example scripts demonstrating various features of LangGraph.

## Installation

It is recommended to use `uv` for managing dependencies and running the scripts.

1. Install `uv` if you haven't already: [https://github.com/astral-sh/uv#installation](https://github.com/astral-sh/uv#installation)
2. Create a virtual environment (optional but recommended):

    ```bash
    uv venv
    source .venv/bin/activate
    ```

3. Install required packages (check individual script requirements):

    ```bash
    uv pip install langgraph typing_extensions # Base packages
    uv pip install pyppeteer nest_asyncio     # For PNG visualization
    # Install pyppeteer browser dependencies if needed
    # playwright install --with-deps # Only needed if using playwright backend
    ```

## Scripts

### `parallel-execution.py`

**Purpose:** Demonstrates how to define and execute both a linear and a parallel workflow using LangGraph.

**Functionality:**

1. **Defines Nodes:** Creates simple placeholder functions (`search_web`, `search_vector_db`, `aggregate_results`) representing tasks.
2. **Builds Linear Graph:** Constructs a graph where nodes execute sequentially: `START` -> `search_web` -> `search_vector_db` -> `aggregate_results` -> `END`.
3. **Builds Parallel Graph:** Constructs a graph where `search_web` and `search_vector_db` execute in parallel after `START`, with both feeding into `aggregate_results` before `END`.
4. **Visualizes Graphs:** Generates PNG images (`linear_graph.png`, `parallel_graph.png`) visualizing the structure of both graphs using `draw_mermaid_png`. This requires `pyppeteer` and its Chromium dependency.
5. **Invokes Graphs:** Runs both the linear and parallel graphs, printing messages to the console indicating which node is executing.

**Dependencies:**

* `langgraph`
* `typing_extensions`
* `pyppeteer` (for visualization)
* `nest_asyncio` (often needed with `pyppeteer`)

**To Run:**

```bash
# Ensure pyppeteer's browser is downloaded (happens automatically on first run)
uv run python parallel-execution.py
```

**Output:**

* Console output showing the execution flow of nodes for both graphs.
* `linear_graph.png`: Visualization of the sequential workflow.
* `parallel_graph.png`: Visualization of the parallel workflow.
