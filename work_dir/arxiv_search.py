# filename: arxiv_search.py
import arxiv
import json

search = arxiv.Search(
  query="trust calibration AND AI systems",
  max_results=20,
  sort_by=arxiv.SortCriterion.Relevance
)

results = []
for result in search.results():
    results.append({
        "title": result.title,
        "authors": [str(author) for author in result.authors],
        "abstract": result.summary,
        "pdf_url": result.pdf_url,
        "published": str(result.published)
    })

print(json.dumps(results, indent=4))