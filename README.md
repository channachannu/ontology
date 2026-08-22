# Financial Ontology

A structured financial knowledge base for representing both **financial metrics** and **non-numeric financial concepts** in machine-readable form.

The project is intended to support financial reasoning, retrieval, semantic search, knowledge graphs, and AI applications by separating:

- **Conceptual knowledge** — what financial terms mean and how they relate
- **Quantitative knowledge** — how financial metrics are defined, calculated, and connected

---

## Repository Structure

```text
Ontology/
├── Datasource/
│   └── Thomas-Willing-financial-history-glossary2.pdf
│
├── Schemas/
│   ├── fin_concept_ontology_full_v2.json
│   ├── fin_concept_ontology_full.json
│   ├── fin_metrics_ontology_v2.json
│   ├── fin_metrics_ontology.json
│   └── schema.json
│
├── .gitignore
├── README.md
├── test.ipynb
└── test.py
```

---

## Project Objective

The goal is to build a reliable financial ontology that can provide structured context to AI systems instead of relying only on pretrained model knowledge.

The ontology is designed to answer four different questions:

```text
What does this financial concept mean?
        ↓
How is it related to other concepts?
        ↓
How can it be measured?
        ↓
What evidence is required to reason about it?
```

The long-term direction is:

```text
Financial Concepts
        ↓
Financial Metrics
        ↓
Financial Evidence
        ↓
Grounded Financial Reasoning
```

---

# 1. Financial Metrics Ontology

The metrics ontology represents measurable financial quantities.

Examples include:

- Revenue
- Net income
- Cash flow from operations
- Current ratio
- Quick ratio
- Debt-to-equity
- ROE
- ROA
- ROIC
- Free cash flow

The ontology distinguishes between:

### Actual metrics

Values directly sourced from financial statements or company filings.

```json
{
  "metric": "revenue",
  "type": "actual"
}
```

### Derived metrics

Values calculated using other ontology metrics.

```json
{
  "metric": "current_ratio",
  "type": "derived",
  "formula": {
    "expression": "current_assets / current_liabilities"
  }
}
```

---

## Metric Schema

The canonical metric structure is defined in `Schemas/schema.json`.

```json
{
  "metric": "",
  "type": "actual | derived",
  "definition": "",
  "unit": "",
  "statement": "balance_sheet | income_statement | cash_flow | cross_statement",
  "period_type": "point_in_time | period",
  "formula": {
    "expression": "",
    "inputs": [
      {
        "metric": "",
        "alignment": "as_is | average_over_period | period_end | period_start"
      }
    ],
    "op": "identity | arithmetic",
    "source_line_item": []
  },
  "influenced_by": [
    {
      "metric": "",
      "direction": "positive | negative | conditional"
    }
  ],
  "valid_range": {
    "min": null,
    "max": null
  },
  "gaap_ifrs_variance": null,
  "source": ""
}
```

### Important metric attributes

| Attribute | Purpose |
|---|---|
| `metric` | Canonical machine-readable metric identifier |
| `type` | Distinguishes reported values from calculated metrics |
| `definition` | Meaning of the metric |
| `unit` | Currency, ratio, count, days, etc. |
| `statement` | Financial statement where the metric belongs |
| `period_type` | Point-in-time or period-based value |
| `formula` | Calculation logic |
| `inputs` | Metrics required by the formula |
| `alignment` | Defines how point-in-time and period values should align |
| `influenced_by` | Directional relationship between drivers and the metric |
| `valid_range` | Optional numerical constraints |
| `gaap_ifrs_variance` | Accounting-framework differences |
| `source` | Filing, derived logic, internal definition, etc. |

---

# 2. Financial Concepts Ontology

The concepts ontology represents non-numeric financial knowledge.

Examples include:

- Bond
- Commercial bank
- Investor
- Liquidity
- Bankruptcy
- Financial crisis
- Derivative
- Monetary policy
- Insurance
- Market failure

---

## Concept Schema

The canonical concept structure is also maintained in `Schemas/schema.json`.

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
  "related_terms": [],
  "broader_term": null,
  "relationships": [
    {
      "relation": "is_a | related_to | references | part_of | superseded_by",
      "target": ""
    }
  ],
  "participants": [
    {
      "role": "",
      "concept": ""
    }
  ],
  "conditions": [],
  "possible_outcomes": [],
  "linked_metrics": [],
  "usage_status": "current | archaic | historical | jurisdiction_specific",
  "jurisdiction": [],
  "historical_period": null,
  "source": {
    "name": "",
    "source_type": ""
  }
}
```

---

## Why `sense_number` Exists

Financial language is frequently polysemous.

For example, **capital** may refer to:

1. Net worth
2. Shareholder contributions
3. Productive physical assets

Instead of combining these meanings into one record, they can be represented separately:

```json
{
  "concept": "capital",
  "sense_number": 1
}
```

```json
{
  "concept": "capital",
  "sense_number": 2
}
```

This helps prevent ambiguous retrieval and reasoning.

---

## Concept Types

The ontology currently supports the following top-level concept categories:

```text
instrument
institution
role
process
condition
concept
event
```

Examples:

```text
bond                -> instrument
commercial_bank     -> institution
investor            -> role
intermediation      -> process
liquidity           -> condition
opportunity_cost    -> concept
financial_crisis    -> event
```

---

## Relationship Types

Concept-to-concept relationships currently include:

| Relationship | Meaning |
|---|---|
| `is_a` | Taxonomic relationship |
| `related_to` | General semantic association |
| `references` | Explicit conceptual dependency/reference |
| `part_of` | Structural relationship |
| `superseded_by` | Historical term or structure replaced by another |

Example:

```text
call_option
    is_a -> option
    references -> underlying_asset
    references -> strike_price
```

---

## Linking Concepts to Metrics

One of the central goals is to connect conceptual understanding with measurable evidence.

For example:

```text
Liquidity
    ├── current_ratio
    ├── quick_ratio
    └── cash_ratio
```

```text
Leverage
    ├── debt_to_equity
    ├── debt_to_assets
    └── interest_coverage
```

```text
Profitability
    ├── gross_margin
    ├── operating_margin
    ├── net_margin
    ├── ROE
    ├── ROA
    └── ROIC
```

The concept schema provides the `linked_metrics` attribute for these mappings.

> The examples above describe the intended semantic layer. They should not be interpreted as confirmation that every mapping is already populated in the current concept ontology.

---

# Data Source

## `Datasource/Thomas-Willing-financial-history-glossary2.pdf`

The initial financial concepts ontology was derived from:

**Glossary of Important Business, Economic, and Financial History Terms**  
Robert E. Wright  
Thomas Willing Institute for the Study of Financial Markets, Institutions, and Regulations

The glossary provides terminology across areas including:

- Banking
- Financial markets
- Securities
- Insurance
- Accounting
- Monetary systems
- Economic history
- Financial crises
- Business organizations

Source provenance is retained in ontology records instead of silently replacing source definitions with model-generated knowledge.

---

# Schema Files

## `Schemas/fin_metrics_ontology.json`

Initial financial metrics ontology.

## `Schemas/fin_metrics_ontology_v2.json`

Revised and validated metrics ontology.

The v2 dataset improves treatment of areas including:

- Weighted-average shares
- EPS
- Debt composition
- Total debt
- NOPAT
- Invested capital
- ROIC
- Quick ratio
- Receivables turnover
- Days Sales Outstanding
- Cash-flow conventions

## `Schemas/fin_concept_ontology_full.json`

Initial financial concepts ontology.

## `Schemas/fin_concept_ontology_full_v2.json`

Revised financial concepts ontology.

## `Schemas/schema.json`

Canonical schema reference for both ontology families.

It currently contains two top-level schema groups:

```text
Metric
Concept
```

> `schema.json` is currently a **canonical schema template/reference**, not a formal JSON Schema specification with validation keywords such as `$schema`, `type`, `required`, and `properties`.

---

# Testing the Ontology with an LLM

The repository includes [`test.py`](./test.py), an early controlled experiment that compares the same financial question under two conditions:

1. **Without ontology context**
2. **With relevant ontology context injected into the system prompt**

The current test uses the Anthropic Python SDK with `claude-sonnet-4-6`.

**Query**
```
A company's current ratio dropped from 1.8 to 0.9 this quarter, and its loan covenant requires current ratio to stay above 1.0 at each quarter-end.  Has the covenant been breached, and what does that trigger contractually?
```

```text
Schemas/fin_metrics_ontology_v2.json
```

This keeps the ontology file as the source of truth and avoids maintaining a separate hard-coded copy of metric definitions inside the test.

For the current experiment, the script selects:

```python
RELEVANT_METRICS = {"current_ratio"}
```

and injects only the matching ontology record into the grounded prompt.

This is **targeted context selection**, but it is not yet semantic retrieval: the relevant metric is still chosen manually in the test code.

---

## Current Test Question

The current experiment asks whether a company breaches a loan covenant when:

```text
Previous current ratio: 1.8
Current quarter ratio: 0.9
Covenant minimum: > 1.0
Measurement point: quarter-end
```

It also asks what the breach triggers contractually.

This intentionally combines two types of knowledge:

```text
Current-ratio interpretation
        ↓
Financial Metrics Ontology

Contractual consequences of covenant breach
        ↓
Loan agreement / contractual knowledge
```

The metric ontology contains evidence for the first part, but not for the second.

---

## Test Flow

```text
                    Financial Question
                           │
             ┌─────────────┴─────────────┐
             │                           │
             ▼                           ▼
       Plain LLM                  Ontology-Grounded LLM
             │                           │
       No ontology                Load metric ontology
                                     │
                                     ▼
                              Select current_ratio
                                     │
                                     ▼
                              Inject as context
             │                           │
             └───────────── compare ─────┘
```

The grounded system prompt instructs the model to reason strictly from the supplied finance definitions and formulas and not use outside definitions.

---

## Experiment 01 — Current Ratio Covenant

### Observed result

Both responses correctly concluded that a quarter-end current ratio of `0.9` is below the covenant threshold of `1.0`.

The ontology-grounded response improved the traceability of the financial reasoning by explicitly using:

```text
current_ratio = current_assets / current_liabilities
period_type = point_in_time
```

This allowed the answer to connect the covenant's quarter-end measurement condition to the ontology's point-in-time classification.

The grounded response also correctly recognized an evidence boundary by stating that the specific contractual consequences were defined by the loan agreement rather than by the supplied financial metric definition.

### Important failure observed

After recognizing that boundary, the grounded response still supplied outside contractual knowledge such as:

- Event of default
- Cure period
- Waiver
- Debt acceleration
- Debt reclassification risk

Those consequences were **not present in the injected ontology or the user-provided facts**.

Therefore, the test currently demonstrates:

```text
Ontology grounding
      ↓
Improved definition and period reasoning
      ↓
Better recognition of missing evidence
      ↓
BUT
      ↓
Prompt alone did not fully stop unsupported inference
```

This is a key finding for the project.

The desired behavior is not simply for the model to know the correct financial answer. It should also distinguish between:

```text
Supported claim
    → answer or derive it

Unsupported claim
    → identify the missing evidence
    → do not fill the gap from pretrained knowledge
```

For this test, an evidence-bounded answer should conclude that the covenant threshold is breached, while stating that the contractual consequences cannot be determined without the applicable loan agreement or an ontology/source containing those provisions.

---

## What the Test Establishes

The current experiment provides evidence that the ontology can help with:

- Explicit definition grounding
- Formula grounding
- Point-in-time versus period interpretation
- Traceability of financial reasoning
- Recognition of an evidence boundary

It also exposes an unresolved problem:

- The model may continue using pretrained knowledge after correctly identifying that the supplied evidence is insufficient.

This means **ontology injection alone is not yet sufficient for strict evidence-only reasoning**.

A more reliable system will require an explicit evidence-control layer in addition to ontology retrieval.

Conceptually:

```text
User Question
      ↓
Retrieve Relevant Knowledge
      ↓
Build Evidence Context
      ↓
Can the requested claim be supported?
      │
   ┌──┴──┐
   │     │
  Yes    No
   │     │
   ▼     ▼
Reason   State what evidence is missing
   │
   ▼
Answer with provenance
```

---

## Experiment Limitations

This is an early qualitative test, not a benchmark.

The current test:

- Uses one financial question
- Uses one selected metric
- Manually specifies the relevant metric name
- Does not retrieve from the concepts ontology
- Does not provide the underlying loan agreement
- Does not score factuality or unsupported inference automatically
- Does not yet enforce a deterministic refusal when evidence is missing

Accordingly, the result should be interpreted as an **initial grounding experiment**, not proof that ontology grounding improves all financial reasoning tasks.

---

## Running `test.py`

Install the required packages:

```bash
pip install anthropic python-dotenv
```

Provide the API key either through the environment:

```bash
export ANTHROPIC_API_KEY=your_key
```

or through a local `.env` file:

```text
ANTHROPIC_API_KEY=your_key
```

Then run:

```bash
python test.py
```

The script prints two sections:

```text
WITHOUT ONTOLOGY
...

WITH ONTOLOGY
...
```

---

## Next Test Improvements

The next iterations of the grounding test can focus on:

- Replacing manual `RELEVANT_METRICS` selection with retrieval
- Retrieving from both metric and concept ontologies
- Adding contractual/source documents when the question requires them
- Adding a strict rule: unsupported claims must return insufficient evidence
- Separating source facts from model interpretation
- Capturing which ontology records support each conclusion
- Building repeatable test cases across liquidity, leverage, profitability, solvency, and valuation
- Measuring unsupported-inference rates rather than relying only on qualitative comparison

---

# Example: Loading the Metrics Ontology

```python
import json

with open("Schemas/fin_metrics_ontology_v2.json") as f:
    metrics = json.load(f)

roic = next(
    item
    for item in metrics
    if item["metric"] == "roic"
)

print(roic["definition"])
print(roic["formula"]["expression"])
```

---

# Example: Loading the Concepts Ontology

```python
import json

with open("Schemas/fin_concept_ontology_full_v2.json") as f:
    concepts = json.load(f)

results = [
    item
    for item in concepts
    if item["concept"] == "liquidity"
]

for item in results:
    print(item["sense_number"], item["definition"])
```

---

# Design Principles

## 1. Evidence over assumptions

Definitions, relationships, and calculations should be grounded in explicit sources or clearly documented transformation rules.

## 2. Separate concepts from measurements

A **concept** explains what something means.

A **metric** explains how something is measured.

## 3. Preserve semantic ambiguity

Legitimate alternative meanings are retained using `sense_number`.

## 4. Avoid silent inference

Unsupported relationships, formulas, or conclusions should not be silently generated.

## 5. Preserve provenance

Source-derived knowledge should retain information about where it originated.

## 6. Machine-readable first

The ontology is designed to be usable directly by:

- Python applications
- Knowledge graphs
- Vector databases
- RAG systems
- LLM pipelines
- Financial AI agents
- Semantic search systems

---

# Intended Architecture

```text
Financial Knowledge Base
│
├── Financial Concepts Ontology
│   ├── Instruments
│   ├── Institutions
│   ├── Roles
│   ├── Processes
│   ├── Conditions
│   ├── Concepts
│   └── Events
│
├── Financial Metrics Ontology
│   ├── Actual Metrics
│   └── Derived Metrics
│
├── Semantic Layer
│   ├── Concept -> Concept
│   ├── Metric -> Metric
│   └── Concept -> Metric
│
└── AI / Reasoning Layer
    ├── Retrieval
    ├── Context Construction
    ├── LLM Reasoning
    └── Grounding Evaluation
```

---

# Current Status

The project is currently in the **ontology construction, validation, and early grounding-experiment stage**.

### Completed

- Financial metric schema designed
- Financial metrics ontology created
- Metrics ontology revised and validated
- Financial concepts schema designed
- Polysemy handling introduced
- Financial glossary converted into structured concepts
- Concept relationship structure established
- Source provenance retained
- Repository separated into `Datasource` and `Schemas`
- Ontology-vs-no-ontology LLM experiment created
- `test.py` updated to load `fin_metrics_ontology_v2.json` dynamically
- First grounding test documented: current-ratio covenant breach

### Next Areas of Work

Potential next steps include:

- Replace manually selected `RELEVANT_METRICS` with semantic retrieval
- Retrieve relevant concepts and metrics per query
- Add an explicit evidence-boundary / insufficient-evidence policy
- Link conceptual terms to measurable metrics
- Validate semantic classifications
- Add additional authoritative financial sources
- Build graph representations
- Introduce ontology consistency tests
- Evaluate retrieval quality
- Evaluate grounded reasoning quality
- Measure unsupported inference / hallucination rates

---

# Potential Extensions

Future sources and domains may include:

- CFA curriculum
- IFRS
- US GAAP
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

---

# Documentation Validation

This README has been checked against the current repository structure, `Schemas/schema.json`, the revised metrics ontology, and the current `test.py` experiment.

Validated points include:

- The repository paths shown above match the current project structure.
- `schema.json` contains separate `Metric` and `Concept` schema templates.
- `fin_metrics_ontology_v2.json` contains **74 metrics: 49 actual and 25 derived**.
- `test.py` loads `Schemas/fin_metrics_ontology_v2.json` rather than maintaining an inline ontology copy.
- The current test injects only `current_ratio`.
- Relevant metric selection is still manual rather than retrieval-driven.
- The observed covenant experiment shows improved grounding but also continued unsupported contractual inference.

Documentation should be updated whenever the schema, file structure, model configuration, or evaluation design changes.

---

# License

The ontology structure and project code can be licensed independently.

The initial conceptual source material states that the glossary is distributed under a **Creative Commons BY-NC-SA** license. Redistribution or derivative use of source-derived content should comply with the applicable license terms.
