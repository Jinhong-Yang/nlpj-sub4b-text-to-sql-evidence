Text-to-SQL with Sub-4B Language Models: Evidence Register

Companion extraction materials for:
Improving Text-to-SQL with Sub-4B Language Models: A Survey of Data, Structure,
Reasoning, and Deployment Techniques
Hyojin Park, Nam-Hyun Yoo, Jinhong Yang

Updated 15 October 2026. The register records source-reported facts and calculated
differences; it does not reproduce the original model experiments. It contains
no manuscript, reviewer correspondence, author portraits, or third-party PDFs.

CONTENTS
S1 data/scale_effects.csv: 85 within-paper contrasts; main_table=True selects the
22 main Table 4 rows. Includes larger-model comparison arms. Published baselines
and unmatched computation are qualified in conditions; these are not universal
causal size effects.
S2 data/compact_configurations.csv: 37 exact Table 9 configurations. Scores are
BIRD dev EX and Spider dev EX. Sampling, external evidence, and online helpers
remain explicit; no TS, dialogue, oracle-schema, or test scores enter these EX
columns. Untuned SC means 16-sample self-consistency, not single-shot.
S3 metadata/source_manifest.json: 37 pinned primary-source PDF identities with
URLs, bytes, pages and SHA256; PDF contents are not redistributed.
S4 metadata/core_evidence.json: core raw endpoints, all 85 contrasts and source
issues. legacy_table9_16 is a historical extraction subset; S2 is authoritative
for the full current inventory. New primary sources include Graphix, RASAT,
the original T5 paper, and Meta-Tool.
S5 metadata/additional_evidence.json: dialogue metrics, source inconsistencies,
baseline checks, data amount and cost disclosures, and bounded Spider2 search.
RASAT match QEM/IEM is distinct from QEX/IEX execution. Meta-Tool's 50 selected
enterprise tasks are distinct from a full official Spider2.0-SQLite/Lite score.
OmniSQL student GPU-hours are derived from reported duration/hardware; synthesis
costs remain unreported and must not be replaced by student training time.
S6 metadata/reference_renumbering.json: 61 current references, a composed mapping
from original working IDs, the previous-release map, and the explicitly retired
secondary T5-size citation. New references have distinct source identities.

INTERPRETATION
Scores are percentages; gain_pp is result minus baseline in percentage points.
Different architectures, metrics, splits, schema conditions, evidence access,
and search budgets are not interchangeable. NR/null is unknown, never zero or
an assumed single candidate. Beam width and rollout cap are not independent
completed-SQL sample counts. The cutoff is strictly below 4B total generator
parameters, not a complete system resource guarantee. Graphix's total count
is nominal 3B plus graph layers (exact total not reported); RASAT reports its
2,851,610,624-parameter implementation explicitly.

SOURCE SCOPE
Original cutoff: 8 May 2026. Targeted primary-source update: 15 October 2026.
The search is narrative and bounded, not an exhaustive post-May census. Table
and version disagreements are preserved in S4/S5. Source labels do not claim
independent replication, absence of contamination, or common-hardware dominance.

CHECKS
Run: python scripts/validate_evidence.py
Standard library only. Checks arithmetic, compact configuration uniqueness,
metrics and selected source conditions, reference identities, source hashes,
an exact public-file allowlist, and the release manifest. The local authoring
audit additionally compares S1/S2 to the manuscript and verifies original PDFs.

AVAILABILITY
https://github.com/Jinhong-Yang/nlpj-sub4b-text-to-sql-evidence
The manuscript identifies the exact immutable commit used for this update.
The repository and its existing commit history identify the authors. An optional
anonymous manuscript withholds this link; the journal uses single anonymized
review, so the named manuscript is the normal submission candidate.
Only extraction tables, source metadata, and validation material are public.
