import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables (optional but safe)
load_dotenv()

# ✅ Initialize OpenRouter client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key= ("YOUR_OPENOUTER_API_KEY")

def call_llm(prompt, temperature=0.6, max_tokens=700):
    """
    Sends a prompt to an OpenRouter model and returns the response.
    """
    try:
        response = client.chat.completions.create(
            model="qwen/qwen3-coder:free",  # Or change to another model if needed
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"⚠️ LLM request failed: {e}"


def summarize(papers, topic=None):
    """
    Summarizes the list of research papers into a structured scientific insight.
    Each paper dict should have 'title' and 'abstract' keys.
    Safely handles None entries.
    """
    if not papers:
        return "❌ No papers found to summarize."

    # Filter out None and ensure each paper is a dict
    paper_summaries = "\n\n".join([
        f"Title: {p.get('title', 'N/A')}\nAbstract: {p.get('abstract', 'No abstract available.')}"
        for p in papers if isinstance(p, dict)
    ])

    if not paper_summaries:
        return "❌ No valid papers to summarize."

    prompt = f"""
    You are a research assistant helping summarize scientific literature.

    Topic: {topic if topic else "General"}

    Given the following papers related to this scientific topic, generate:
    1. A concise scientific summary (2–3 paragraphs)
    2. Highlight key findings or trends
    3. Suggest potential research directions

    Papers:
    {paper_summaries}
    """

    return call_llm(prompt)

