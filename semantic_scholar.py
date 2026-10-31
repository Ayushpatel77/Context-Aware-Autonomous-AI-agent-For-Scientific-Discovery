import requests
import time


def fetch_research_papers(topic, limit=5):
    url = "https://api.semanticscholar.org/graph/v1/paper/search"
    params = {
        "query": topic,
        "limit": limit,
        "fields": "title,abstract,year,authors,url"
    }
    headers = {
        "User-Agent": "BeastResearchBot/1.0 (https://github.com/beast-ai)"
    }

    print(f"\n🔍 Searching papers on: {topic}\n")

    response = requests.get(url, params=params, headers=headers)

    # If too many requests, wait a bit and retry once
    if response.status_code == 429:
        print("⚠️ Rate limit hit. Waiting 10 seconds and retrying...")
        time.sleep(10)
        response = requests.get(url, params=params, headers=headers)

    if response.status_code != 200:
        print("❌ Error fetching papers:", response.status_code)
        return []

    data = response.json().get("data", [])

    for i, paper in enumerate(data, 1):
        print(f"\n Paper {i}: {paper['title']}")
        print(f" Year: {paper.get('year', 'Unknown')}")
        print(f" Authors: {[a['name'] for a in paper.get('authors', [])]}")
        print(f" Link: {paper.get('url', 'N/A')}")
        print(f" Abstract:\n{paper.get('abstract', 'No abstract available')}")
        print("-" * 100)

    return data



