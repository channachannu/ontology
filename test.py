"""
Compares Claude's response to a finance query with vs without
the ontology/dictionary injected as system context.

Usage:
    export ANTHROPIC_API_KEY=your_key
    python compare_ontology.py
"""

import os
import json
from pathlib import Path
from anthropic import Anthropic
from dotenv import load_dotenv
load_dotenv()


client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

# Load the metric ontology from the schema files (single source of truth —
# avoids the ontology drifting out of sync with a hardcoded inline copy).
SCHEMA_DIR = Path(__file__).parent / "Schemas"
ONTOLOGY_PATH = SCHEMA_DIR / "fin_metrics_ontology_v2.json"

with open(ONTOLOGY_PATH, encoding="utf-8") as f:
    full_ontology = json.load(f)

# Only pull in the metrics relevant to this test query, so the system prompt
# doesn't balloon with the entire ontology on every call.
RELEVANT_METRICS = {"current_ratio"}
ONTOLOGY = [m for m in full_ontology if m["metric"] in RELEVANT_METRICS]

if len(ONTOLOGY) != len(RELEVANT_METRICS):
    found = {m["metric"] for m in ONTOLOGY}
    missing = RELEVANT_METRICS - found
    raise ValueError(f"Expected metrics not found in {ONTOLOGY_PATH.name}: {missing}")


QUERY = ("""
A company's current ratio dropped from 1.8 to 0.9 this quarter, and its loan covenant requires current ratio to stay above 1.0 at each quarter-end. 
Has the covenant been breached, and what does that trigger contractually?
"""
)
def ask(query: str, system: str = "") -> str:
    resp = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=500,
        system="""Keep the response concise and simple """+system,
        messages=[{"role": "user", "content": query}],
    )
    return resp.content[0].text


def main():
    # 1. No ontology — plain query
    plain_answer = ask(QUERY)

    # 2. With ontology — inject definitions/formulas as system context
    ontology_system = (
        "You must ground all reasoning strictly in the following finance "
        "definitions and formulas. Do not use outside definitions:\n\n"
        f"{ONTOLOGY}"
    )
    grounded_answer = ask(QUERY, system=ontology_system)

    print("=" * 60)
    print("WITHOUT ONTOLOGY")
    print("=" * 60)
    print(plain_answer)

    print("\n" + "=" * 60)
    print("WITH ONTOLOGY")
    print("=" * 60)
    print(grounded_answer)


if __name__ == "__main__":
    main()