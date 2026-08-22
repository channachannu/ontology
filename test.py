"""
Compares Claude's response to a finance query with vs without
the ontology/dictionary injected as system context.

Usage:
    export ANTHROPIC_API_KEY=your_key
    python compare_ontology.py
"""

import os
from anthropic import Anthropic
from dotenv import load_dotenv
load_dotenv()


client = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
ONTOLOGY =[{
    "metric": "current_ratio",
    "type": "derived",
    "definition": "Ability to cover short-term liabilities with short-term assets.",
    "unit": "ratio",
    "statement": "cross_statement",
    "period_type": "point_in_time",
    "formula": {
      "expression": "current_assets / current_liabilities",
      "inputs": [
        {"metric": "current_assets", "alignment": "as_is"},
        {"metric": "current_liabilities", "alignment": "as_is"}
      ],
      "op": "arithmetic",
      "source_line_item": []
    },
    "influenced_by": [
      {"metric": "current_assets", "direction": "positive"},
      {"metric": "current_liabilities", "direction": "negative"}
    ],
    "valid_range": {"min": 0, "max": None},
    "gaap_ifrs_variance": None,
    "source": "derived"
  },
  {
    "metric": "roe",
    "type": "derived",
    "definition": "Net income generated per unit of shareholder equity.",
    "unit": "ratio",
    "statement": "cross_statement",
    "period_type": "period",
    "formula": {
      "expression": "net_income / equity",
      "inputs": [
        {"metric": "net_income", "alignment": "as_is"},
        {"metric": "equity", "alignment": "average_over_period"}
      ],
      "op": "arithmetic",
      "source_line_item": []
    },
    "influenced_by": [
      {"metric": "net_income", "direction": "positive"},
      {"metric": "equity", "direction": "negative"}
    ],
    "valid_range": {"min": None, "max": None},
    "gaap_ifrs_variance": None,
    "source": "derived"
  },
  {
  "metric": "adjusted_operating_margin",
  "type": "derived",
  "definition": "Operating margin adjusted to exclude one-time restructuring costs and add back stock-based compensation, expressed as a percentage of revenue.",
  "unit": "ratio",
  "statement": "cross_statement",
  "period_type": "period",
  "formula": {
    "expression": "(operating_income + restructuring_costs + stock_based_compensation) / revenue",
    "inputs": [
      {"metric": "operating_income", "alignment": "as_is"},
      {"metric": "restructuring_costs", "alignment": "as_is"},
      {"metric": "stock_based_compensation", "alignment": "as_is"},
      {"metric": "revenue", "alignment": "as_is"}
    ],
    "op": "arithmetic",
    "source_line_item": []
  },
  "influenced_by": [
    {"metric": "operating_income", "direction": "positive"},
    {"metric": "restructuring_costs", "direction": "positive"},
    {"metric": "stock_based_compensation", "direction": "positive"},
    {"metric": "revenue", "direction": "negative"}
  ],
  "valid_range": {"min": None, "max": None},
  "gaap_ifrs_variance": None,
  "source": "internal definition"
}
]


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