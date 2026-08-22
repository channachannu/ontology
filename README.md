# Financial Ontology Project

A structured financial knowledge base that combines **numeric financial metrics** with **non-numeric financial concepts** for retrieval, reasoning, analytics, and AI applications.

## Overview

This project currently contains two complementary ontology layers:

1. **Financial Metrics Ontology** — defines measurable financial metrics such as revenue, ROIC, liquidity ratios, debt ratios, margins, and cash-flow measures.
2. **Financial Concepts Ontology** — defines non-numeric financial terms such as bonds, banks, liquidity, bankruptcy, derivatives, investors, monetary policy, and related concepts.

Together, these layers provide both **quantitative** and **conceptual** financial knowledge.

## Project Objective

The objective is to build a reliable, machine-readable financial ontology that can support:

- Financial reasoning systems
- Retrieval-augmented generation (RAG)
- Knowledge graphs
- Financial AI agents
- Evidence-based financial analysis
- Semantic search
- Financial education and research
- Concept-to-metric mapping

The ontology separates:

- **What a financial concept means**
- **How concepts relate to each other**
- **How financial metrics are calculated**
- **Which concepts can be measured using which metrics**
- **Where each definition or relationship came from**

## Project Files

```text
.
├── fin_metrics_ontology_v2.json
├── financial_concepts_ontology_thomas_willing.json
└── README.md
```

### `fin_metrics_ontology_v2.json`

Validated ontology for numeric financial measures.

Current coverage:

- 74 financial metrics
- 49 actual metrics
- 25 derived metrics

It includes corrected treatment for areas such as:

- Weighted-average shares
- EPS
- Debt composition
- ROIC
- NOPAT
- Invested capital
- Quick ratio
- Receivables turnover
- Days Sales Outstanding
- Cash-flow sign conventions

### `financial_concepts_ontology_thomas_willing.json`

Ontology for non-numeric financial concepts derived from a financial-history glossary.

Current coverage:

- 405 unique concepts
- 487 sense-level ontology records

The extraction preserves:

- Multiple meanings
- Noun / verb / adjective distinctions
- Explicit glossary cross-references
- Abbreviations
- Historical terminology
- Archaic terminology
- Selected jurisdiction context
- Source provenance

## Financial Metrics Ontology

Example:

```json
{
  "metric": "current_ratio",
  "type": "derived",
  "definition": "Ability to cover short-term liabilities with short-term assets.",
  "unit": "ratio",
  "statement": "balance_sheet",
  "period_type": "point_in_time",
  "formula": {
    "expression": "current_assets / current_liabilities",
    "inputs": [
      {
        "metric": "current_assets",
        "alignment": "as_is"
      },
      {
        "metric": "current_liabilities",
        "alignment": "as_is"
      }
    ],
    "op": "arithmetic",
    "source_line_item": []
  },
  "source": "derived"
}
```

The metrics ontology models:

- Actual financial statement items
- Derived metrics
- Formula dependencies
- Period alignment
- Units
- Statement classification
- Selected GAAP / IFRS differences

## Financial Concepts Ontology

Example:

```json
{
  "concept": "call_option",
  "name": "Call Option",
  "sense_number": 1,
  "definition": "A type of option derivative that gives the holder the right but not the obligation to purchase an underlying asset at a predetermined strike price.",
  "concept_type": "instrument",
  "subtype": "derivative",
  "domain": [
    "capital_markets",
    "derivatives"
  ],
  "part_of_speech": "noun",
  "synonyms": [],
  "abbreviations": [],
  "relationships": [
    {
      "relation": "is_a",
      "target": "option"
    },
    {
      "relation": "references",
      "target": "underlying_asset"
    },
    {
      "relation": "references",
      "target": "strike_price"
    }
  ],
  "participants": [],
  "conditions": [],
  "possible_outcomes": [],
  "linked_metrics": [],
  "usage_status": "current",
  "jurisdiction": [],
  "historical_period": null,
  "source": {
    "name": "Glossary of Important Business, Economic, and Financial History Terms",
    "source_type": "glossary"
  }
}
```

## Concept Schema

```json
{
  "concept": "",
  "name": "",
  "sense_number": 1,
  "definition": "",
  "concept_type": "instrument | institution | role | process | condition | concept | event",
  "subtype": "",
  "domain": [],
  "part_of_speech": "noun | verb | adjective",
  "synonyms": [],
  "abbreviations": [],
  "relationships": [
    {
      "relation": "is_a | related_to | references | part_of | superseded_by",
      "target": ""
    }
  ],
  "participants": [],
  "conditions": [],
  "possible_outcomes": [],
  "linked_metrics": [],
  "usage_status": "current | archaic",
  "jurisdiction": [],
  "historical_period": null,
  "source": {
    "name": "",
    "source_type": ""
  }
}
```

## Why `sense_number` Exists

Financial terminology is often polysemous.

For example, **capital** can refer to:

1. Net worth
2. Shareholder contributions
3. Productive physical assets

Each meaning is stored as a separate ontology record using `sense_number`.

This helps downstream AI systems distinguish between different semantic meanings instead of treating every occurrence of a term as identical.

## Relationship Types

The conceptual ontology currently supports:

| Relationship | Meaning |
|---|---|
| `is_a` | Taxonomic relationship |
| `related_to` | General semantic relationship |
| `references` | Concept explicitly refers to another concept |
| `part_of` | Concept is structurally part of another concept |
| `superseded_by` | Historical concept replaced by another concept |

Example:

```text
call_option
    is_a -> option
    references -> strike_price
    references -> underlying_asset
```

## Concept Types

Top-level concept types:

- `instrument`
- `institution`
- `role`
- `process`
- `condition`
- `concept`
- `event`

Examples:

```text
bond -> instrument
commercial_bank -> institution
investor -> role
intermediation -> process
liquidity -> condition
opportunity_cost -> concept
financial_crisis -> event
```

## Linking Concepts to Metrics

A core goal of the project is to connect conceptual financial knowledge with measurable financial evidence.

Example:

```text
Liquidity
    -> current_ratio
    -> quick_ratio
    -> cash_ratio
```

```text
Leverage
    -> debt_to_equity
    -> debt_to_assets
    -> interest_coverage
```

```text
Profitability
    -> gross_margin
    -> operating_margin
    -> net_margin
    -> ROE
    -> ROA
    -> ROIC
```

Conceptually:

```text
Financial Concepts
        ↓
Financial Metrics
        ↓
Financial Evidence
        ↓
Financial Reasoning
```

## Design Principles

### 1. Evidence over assumptions

Definitions, relationships, and calculations should be traceable to explicit source material wherever possible.

### 2. Concepts and metrics are separate

A concept explains **what something means**.

A metric explains **how something is measured**.

### 3. Avoid hidden inference

If a relationship, formula, or definition is not supported by a source or a clearly defined rule, it should not be silently invented.

### 4. Preserve semantic ambiguity

Financial terms with multiple meanings are represented using `sense_number`.

### 5. Machine-readable first

The schema is designed for direct use in:

- Python
- Vector databases
- Graph databases
- RAG systems
- LLM pipelines
- Financial AI agents

## Source Material

The initial conceptual ontology was derived from:

**Glossary of Important Business, Economic, and Financial History Terms**  
Robert E. Wright  
Thomas Willing Institute for the Study of Financial Markets, Institutions, and Regulations

Source provenance is preserved in ontology records instead of silently replacing source definitions with model-generated financial knowledge.

## Example Python Usage

```python
import json

with open("financial_concepts_ontology_thomas_willing.json") as f:
    concepts = json.load(f)

results = [
    item
    for item in concepts
    if item["concept"] == "liquidity"
]

for item in results:
    print(item["definition"])
```

## Possible Knowledge Graph Representation

```text
Investor
   |
   | owns
   v
Equity
   |
   | is_a
   v
Financial Instrument
```

Another example:

```text
Financial Crisis
    |
    +-- related_to --> Bank Run
    |
    +-- related_to --> Credit Crunch
    |
    +-- related_to --> Financial Panic
    |
    +-- related_to --> Stock Market Crash
```

And eventually:

```text
Liquidity
    |
    +-- measured_by --> Current Ratio
    +-- measured_by --> Quick Ratio
    +-- measured_by --> Cash Ratio
```

## Potential Future Extensions

Possible future ontology sources and domains include:

- CFA terminology
- IFRS concepts
- US GAAP terminology
- Indian Accounting Standards (Ind AS)
- Corporate finance
- Portfolio management
- Equity research
- Banking
- Insurance
- Macroeconomics
- Valuation
- Risk management
- Financial regulation
- Market microstructure
- Behavioral finance

Future iterations may also add:

- Concept-to-metric mappings
- Causal relationships
- Multiple source references
- Confidence scores
- Jurisdiction-aware definitions
- Temporal validity
- Knowledge graph exports
- Automated ontology validation

## Intended Architecture

```text
Financial Knowledge Base
│
├── Financial Concepts Ontology
│   ├── Instruments
│   ├── Institutions
│   ├── Roles
│   ├── Processes
│   ├── Conditions
│   └── Events
│
├── Financial Metrics Ontology
│   ├── Actual Metrics
│   └── Derived Metrics
│
└── Semantic Relationships
    ├── Concept -> Concept
    ├── Metric -> Metric
    └── Concept -> Metric
```

## Project Status

Current stage: **ontology construction and validation**.

Completed:

- Financial metrics schema designed
- Metrics ontology validated and revised
- Financial concepts schema designed
- Polysemy handling added
- Source glossary parsed
- Concept ontology generated
- Relationship structure established
- Source provenance retained

Next iterations can focus on:

- Semantic validation
- Additional authoritative sources
- Concept-to-metric linking
- Knowledge graph construction
- Retrieval and reasoning evaluation

## License

The ontology structure and project code can be licensed independently.

The initial conceptual source material states that the glossary is distributed under a **Creative Commons BY-NC-SA** license. Redistribution or derivative use of source-derived content should comply with the applicable license terms.
