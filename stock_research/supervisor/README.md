## Multi-Agent Architecture: Sub-Agent Delegation Model

This system implements a **Sub-Agent Delegation Model**, where the **Supervisor Agent** receives user queries and routes them to specialized **Sub-Agents** based on the nature of the task.
Each Sub-Agent focuses on a specific domain, while the Supervisor acts as a central router and tool executor.

---

### 📁 Directory Structure

```
supervisor/
├── agent.py                  # Defines the Supervisor Agent and delegation logic
├── .env                      # Environment variables
├── tools/
│   ├── tools.py              # Tool for returning the current time
│   └── __init__.py
└── sub_agents/
    ├── __init__.py
    ├── news_analyst/
    │   ├── __init__.py
    │   └── agent.py          # Defines the News Analyst Sub-Agent
    └── stock_analyst/
        ├── __init__.py
        └── agent.py          # Defines the Stock Analyst Sub-Agent
```

---

### Components

#### 1. **Stock Analyst Sub-Agent**

* **Function**: Retrieves the current stock price using the `yfinance` library.
* **Role**: Handles all stock-related queries.

#### 2. **News Analyst Sub-Agent**

* **Function**: Searches for the latest news using Google Search.
* **Role**: Handles queries related to current events, trends, or recent developments.

#### 3. **Current Time Tool**

* **Function**: Returns the current time.

#### 4. **Supervisor Agent**

* **Responsibilities**:

  * Analyzes user input.
  * Delegates tasks to the appropriate Sub-Agent.
  * Executes internal tools when needed.

---

### ⚠️ Sub-Agent Restrictions

**Built-in tools cannot be used within a Sub-Agent.**

Specifically, using built-in tools such as:

* Google Search
* Code Execution
* Vertex AI Search
  directly inside a Sub-Agent is **not supported**.

#### ✅ Workaround

To address this limitation:

* Required functionalities are implemented as **Agent Tools**.
* These tools are attached to the **Supervisor Agent**, which can execute them **on behalf of Sub-Agents**.

---
