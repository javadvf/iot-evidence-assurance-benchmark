# Final Evaluation Protocol

Status: Approved by the author
Date: 2026-11-24

## 1. Frozen Development Implementation

Git commit:
ab7bd0ca8a555afdac9ddefb184c2b2dcc895446

Development code SHA-256:
d454f92af595566d62ba570d194226516fe74afdffebb525d681160693da59d4

Scenario and reference SHA-256:
e438851e88dc6efc6d150ae8993e6da3b4f70bb25e6c8c97493f0964be564233

Core development results SHA-256:
2398af4d60a5f506dcb373b0a4a51031ce619bec3f986acba712d4eece5568cf

All 27 development cells reproduced successfully
in a fresh Python process.

## 2. Reserved Evaluation Partition

- Batch indices: 65–129.
- Batches: 65.
- Original measurement records: 4,211.
- Preserve the original 65-batch commitment prefix.
- Preserve the verified original data and provenance.
- No parameter adjustment using evaluation outcomes.

The reserved partition is not fully blinded because
historical verification previously inspected all batches.

## 3. Comparative Evaluation

- Six unchanged architectures: A1, A2, B1, B2, C1, C2.
- All 19 approved core scenarios.
- Expected core architecture decisions: 7,410.
- Retain all approved reference outcomes.
- Repeat T09a–T09e experiments.
- Repeat all six boundary-condition scenarios.
- Repeat witness availability and compromise sensitivity.
- Repeat infrastructure sensitivity experiments.

Reference outcomes must remain independent of
observed verifier decisions.

## 4. Performance Evaluation

- Timing instrument: Python perf_counter_ns().
- One warm-up and five measured repetitions.
- Deterministically rotate architecture execution order.
- Measure all evaluation control batches.
- Report median and interquartile range.
- Exclude scenario construction, contract deployment
  and infrastructure preparation from verification timing.
- Include required local backend queries.

Report evidence size, verification support size and
persistent application-state storage separately.

Local backend performance must not be interpreted
as public Ethereum network performance.

## 5. Statistical Analysis

- Paired descriptive comparisons.
- Batch-level experimental organization.
- Preserve metric numerators and denominators.
- Do not treat repeated scenarios or architectures
  as independent observations.
- Keep core, robustness and sensitivity results separate.
- Preserve unexpected results and document deviations.

## 6. Reproducibility and Open Science

- Preserve the audited development notebook.
- Archive evaluation-runner source before execution.
- Preserve essential machine-readable results.
- Record SHA-256 fingerprints and software versions.
- No undocumented methodological modifications.

## 7. Interpretation Boundaries

- No universal blockchain superiority claims.
- No physical measurement accuracy claims.
- No real-world attack probability estimates.
- No public-network consensus security claims.
- Single-author study.
- No external replication or independent annotation claims.

## 8. Freeze Status

Evaluation specifications: APPROVED.
Development implementation: ARCHIVED AND REPRODUCED.
Evaluation-runner implementation: PENDING.
Final experimental freeze: PENDING.
Reserved comparative evaluation: NOT STARTED.
