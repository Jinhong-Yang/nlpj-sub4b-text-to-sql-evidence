Compact Text-to-SQL: Anonymous Review Evidence

S1 data/scale_effects.csv contains 85 source-reported contrasts; main_table=True
selects the 22 comparisons in main Table 4. Published baselines and unmatched
compute remain explicit. Graphix/RASAT comparisons include DB content; PICARD's
schema-only rows use different baseline inputs.
S2 data/compact_configurations.csv contains all 37 exact Table 9 configurations,
with metric, input, sampling/beam and online auxiliary conditions. Untuned SC
means 16-sample self-consistency. SLM-SQL source labels consistently use arXiv v1.
S3 metadata/source_manifest.json records 37 primary PDF identities, URLs and
checksums. The original PDFs are not redistributed.
S4 metadata/core_evidence.json retains raw endpoints, all 85 contrasts, conditions
and known source issues. legacy_table9_16 is historical; S2 is authoritative.
S5 metadata/additional_evidence.json adds dialogue metrics, baseline and data-cost
checks, bounded search, and pinned public-code provenance checks. Meta-Tool's
paper-selected 50-task claim is NOT verified official Spider2 evidence: released
loaders use legacy Spider and synthetic fallbacks. Its claimed 64 percent score
is not comparable to official split scores. Graphix released settings use DB
content and beams 1/4 without/with PICARD; exact table reconstruction is unverified.
Publication records for six 2026 papers were compared. The FINER proceedings
pagination and publisher-deposited internal pagination discrepancy is retained.
S6 metadata/reference_renumbering.json records 61 current references and retained,
retired and new source identities. It is an attribution map, not new experiments.

All scores are source-reported percentages; gain_pp is result minus baseline.
Different splits, metrics, schema/evidence access, architectures and inference
budgets are not interchangeable. NR/null is unknown, never an imputed value.
Synthesis cost differs from student-training GPU-hours. No original model result
has been independently reproduced by these extraction materials.

Run python scripts/validate_evidence.py with Python standard library only.
Checks cover counts, arithmetic, selected conditions, citation identities, file
hashes and the exact public-file allowlist. The mirror contains the same 11 text
files; MANIFEST.json identifies all other files. Identifying details and original
repository links are omitted from this review copy. Bibliographic author names
and third-party primary-source repository links remain for correct attribution.

Original literature cutoff: 8 May 2026; targeted source checks: 15 October 2026.
This is a bounded narrative extraction, not an exhaustive systematic census.
Only extraction tables, primary-source metadata and validation material are
included. No manuscript, review correspondence, author images or source PDFs.
