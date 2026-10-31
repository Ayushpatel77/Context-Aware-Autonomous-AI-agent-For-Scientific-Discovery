# 🧪 Context-Aware Autonomous AI Agent for Scientific Discovery

An AI-powered research assistant that helps explore scientific topics by retrieving relevant research papers, generating AI-based summaries, and proposing exploratory molecule concepts using large language models (LLMs).

The project combines scientific literature retrieval, LLM-powered reasoning, and an interactive Streamlit interface to support early-stage scientific exploration.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Framework-Streamlit-FF4B4B?logo=streamlit" alt="Streamlit">
  <img src="https://img.shields.io/badge/LLM-OpenRouter-purple" alt="OpenRouter">
  <img src="https://img.shields.io/badge/Research-Semantic%20Scholar-green" alt="Semantic Scholar">
  <img src="https://img.shields.io/badge/Status-Academic%20Project-orange" alt="Project Status">
</p>

## 📌 Overview

Scientific research often requires reviewing numerous papers, identifying relevant findings, and exploring potential research directions.

This project demonstrates how an AI agent can assist with these tasks through a unified interface. Users can enter a scientific topic, retrieve relevant academic literature, generate AI-powered summaries, and explore preliminary molecule concepts.

The application is designed as an academic AI project demonstrating the integration of LLMs, research APIs, and an interactive web application.

## ✨ Key Features

- ** Scientific Literature Retrieval** — Fetches relevant research papers using Semantic Scholar.
- ** AI-Powered Research Summarization** — Uses an LLM to synthesize information and generate concise research insights.
- ** Exploratory Molecule Concept Generation** — Generates preliminary molecule concepts inspired by a selected research topic.
- ** Output Validation** — Includes a validation component to check generated outputs.
- ** Interactive Web Interface** — Provides a user-friendly interface built with Streamlit.
- ** LLM Integration** — Connects to language models through OpenRouter.
- ** Research Topic Exploration** — Supports exploration of scientific topics such as Alzheimer's disease and related research areas.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Streamlit | Interactive web interface |
| OpenRouter API | Access to supported large language models |
| Semantic Scholar API | Scientific paper retrieval |
| LLMs | Research synthesis and exploratory generation |
| Pytest | Automated testing |

## 🏗️ System Architecture

The application follows a modular architecture in which each component handles a specific responsibility.

```text
                 ┌───────────────────────┐
                 │         User          │
                 └───────────┬───────────┘
                             │
                             ▼
                 ┌───────────────────────┐
                 │   Streamlit Interface │
                 │        app.py         │
                 └───────────┬───────────┘
                             │
                 ┌───────────┴───────────┐
                 ▼                       ▼
      ┌──────────────────┐    ┌──────────────────┐
      │ Semantic Scholar │    │   LLM Service    │
      │ Paper Retrieval  │    │    llm.py        │
      └────────┬─────────┘    └────────┬─────────┘
               │                       │
               ▼                       ▼
      ┌──────────────────┐    ┌──────────────────┐
      │ Research Papers  │    │ Research Insight │
      └──────────────────┘    │ and Generation   │
                              └────────┬─────────┘
                                       │
                                       ▼
                              ┌──────────────────┐
                              │ Output Validation│
                              │   validator.py   │
                              └────────┬─────────┘
                                       │
                                       ▼
                              ┌──────────────────┐
                              │ Results Presented│
                              │    to the User   │
                              └──────────────────┘
```

*Note: This diagram represents the intended high-level workflow. The exact execution sequence depends on the implementation of each module.*

## 📂 Project Structure

```text
context-aware-autonomous-ai-agent-scientific-discovery/
│
├── app.py                 # Streamlit application and user interface
├── semanti_scholar.py     # Semantic Scholar research-paper retrieval
├── llm.py                 # LLM integration and response generation
├── generator.py           # Research or molecule-concept generation
├── validator.py           # Validation of generated outputs
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

*The filenames above reflect the current project scaffold. Adjust them if your final implementation uses different filenames.*

## ⚙️ Getting Started

Follow these steps to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/context-aware-autonomous-ai-agent-scientific-discovery.git
```

Navigate into the project directory:

```bash
cd context-aware-autonomous-ai-agent-scientific-discovery
```

Replace `YOUR_USERNAME` with your GitHub username.

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

On macOS or Linux:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file based on `.env.example`, or configure the variables directly in your terminal.

Example configuration:

```env
OPENROUTER_API_KEY=your_openrouter_api_key
OPENROUTER_MODEL=your_supported_model_id
```

Obtain an API key through the official [OpenRouter website](https://openrouter.ai/).

**Security:** Never commit your real API key, `.env` file, or other credentials to GitHub. Keep secrets in environment variables or a secure secrets manager.

### 5. Run the Application

```bash
streamlit run app.py
```

The application should open in your browser. If it does not, follow the local URL printed in the terminal.

##  Example Workflow

1. Open the application.
2. Enter a scientific research topic, such as *Alzheimer's disease*.
3. Retrieve relevant research papers.
4. Review the AI-generated research summary.
5. Explore the generated molecule concept, if supported by the configured workflow.
6. Examine the generated results and validation feedback.

##  How It Works

### 1. Research Query

The user enters a scientific topic through the Streamlit interface.

### 2. Literature Retrieval

The application queries Semantic Scholar to find relevant academic papers and retrieve available metadata.

### 3. AI-Based Research Synthesis

Retrieved information is passed to the configured language model to produce a summary of relevant research findings.

### 4. Exploratory Concept Generation

The generation module can propose preliminary molecule concepts based on the research topic and the information supplied to the model.

### 5. Validation and Presentation

The validation module checks generated outputs according to the implemented validation rules. Results are then presented through the application interface.

**Important:** LLM-generated summaries and molecule concepts may contain inaccuracies. Generated molecule concepts should not be treated as validated drug candidates or experimentally confirmed discoveries.

##  Testing

Run the automated tests with:

```bash
pytest
```

The tests help verify the behavior of supported validation functions.

##  Future Improvements

Potential directions for extending the project include:

- Multi-agent collaboration for specialized research tasks.
- Improved scientific-paper ranking and relevance filtering.
- Citation-aware summaries with source references.
- Persistent research sessions and conversation memory.
- More robust API error handling and rate-limit management.
- Integration with scientific databases and molecular chemistry tools.
- Structure validation using cheminformatics libraries such as RDKit.
- Evaluation of generated outputs against scientific references.
- Deployment through a suitable cloud hosting platform.

These are potential extensions and should not be interpreted as already implemented features.

##  Limitations

- Research-paper availability depends on the external literature API.
- API rate limits and network connectivity can affect retrieval.
- LLM responses may be incomplete, inaccurate, or unsupported by retrieved sources.
- Molecule concepts are exploratory outputs, not validated compounds.
- The application is intended for research assistance and educational experimentation, not autonomous clinical or drug-development decisions.

## 🔐 Responsible Use

This project is an academic demonstration of AI-assisted scientific exploration. Users should independently verify generated claims against original scientific publications.

It should not be used as a substitute for expert scientific review, experimental validation, medical advice, or regulatory assessment.

##  Project Applications

- AI and Machine Learning
- Natural Language Processing
- Large Language Model Applications
- Scientific Literature Mining
- AI-Assisted Research
- Modular AI Agent Development

⭐ If you find this project interesting, consider starring the repository.
