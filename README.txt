Text-to-SQL with Sub-4B Language Models: Evidence Register

Companion extraction materials for:
Improving Text-to-SQL with Sub-4B Language Models: A Survey of Data, Structure,
Reasoning, and Deployment Techniques
Hyojin Park, Nam-Hyun Yoo, Jinhong Yang

The register contains published numerical endpoints and within-study contrasts,
with benchmark metrics, input conditions, inference budgets, source versions
and bibliographic provenance. It supports inspection of the survey's tables;
the reported model results belong to the cited primary studies.

CONTENTS
S1 data/scale_effects_49_contrasts.csv: 49 within-study contrasts; main_table=True
selects the 16 contrasts in main Table 4. Larger generators are scale-comparison
arms; they are not counted as sub-4B configurations.
S2 data/compact_configurations_24.csv: the 24 exact generator configurations in
main Table 9, with BIRD dev EX, Spider dev EX and inference/auxiliary conditions.
S3 metadata/source_manifest.json: 33 retrieved primary-source URLs, PDF names,
file sizes, page counts and SHA-256 values. The PDFs themselves are not bundled.
S4 metadata/core_evidence.json: core raw endpoints, conditions and source issues.
Its original 16-condition draft inventory is supplemented by the additional
extraction; S2 is the authoritative full 24-condition Table 9 inventory.
S5 metadata/additional_evidence.json: added synthesis, SENSE, MCTS, LitE,
contamination conditions and evidence limits.
S6 metadata/reference_renumbering.json: maps working citation IDs to the
58-reference list in first-appearance order; includes bibliographic entries.

INTERPRETATION
Scores are percentages and differences are percentage points. Different metrics,
splits, schema conditions, knowledge access, architectures and candidate budgets
are not interchangeable. NR/null means unreported or not established for that
configuration, never zero or an assumed single candidate. A beam width and a
rollout cap are not counts of independently sampled completed SQL queries.

The compact cutoff is strictly fewer than 4 billion total generator parameters.
It is not a complete memory/latency budget or a claim that online auxiliaries fit
that cutoff. S1 includes larger-model comparison arms. CodeS BIRD pairs preserve
no-external-knowledge / with-external-knowledge order; CodeS Spider 3-shot TS is
not inserted as EX. LitE ordinary rows use retrieved top-25 schema conditions;
its Spider test scores are not inserted in the Spider dev column.

SOURCE SCOPE
The original literature cutoff was 8 May 2026, with a targeted primary-source
update on 15 October 2026. This is a structured narrative survey, not a registered
systematic review or an independent reproduction. Pinned numerical PDFs are
distinguished from later archival metadata. Known conflicting cells, incomplete
candidate budgets and uncovered benchmark configurations remain explicit.

CHECKS
Run: python scripts/validate_evidence.py
Python 3 standard library only. Checks cover arithmetic, table sizes, selected
contrasts, compact generator labels, citation mapping, source metadata and file
hashes. They do not establish semantic correctness of the original experiments,
absence of benchmark contamination or common-hardware superiority.

AVAILABILITY
Public evidence repository: https://github.com/Jinhong-Yang/nlpj-sub4b-text-to-sql-evidence
Initial evidence release: 15 October 2026. The manuscript identifies the
exact repository commit used for its data-availability statement.
Only extraction tables, source metadata and validation materials are included.
