# Protocol Addendum

Version: 1.0
Status: Pending approval

This addendum takes precedence where earlier draft
documents contain conflicting methodological details.

## 1. Fair Architecture Comparison

Use equivalent canonical signed batch content,
source authorization and evidence availability.

Include sequence identifiers and previous commitments
in the common signed batch representation.

Control verifier history across comparisons.

Distinguish detection of conflicting histories from
prevention of conflicting accepted histories.

## 2. Evaluation Policy

Separate three analytical dimensions:

- Cryptographic verification
- Evidence-policy satisfaction
- Underlying injected failure

Do not use hidden scenario labels as verifier inputs.

A cryptographically valid record can remain
physically incorrect.

Use explicitly declared synthetic policies for
freshness, authorization and certificate validity.

Do not introduce unsupported sensor accuracy thresholds.

## 3. Reference Outcomes

ACCEPT:
All mandatory policy conditions are satisfied.

REJECT:
At least one mandatory condition is demonstrably violated.

INDETERMINATE:
No violation is established, but mandatory evidence
is missing or cannot be verified.

A proven violation takes precedence over missing evidence.

Reference outcomes must be independently reviewed
and frozen before comparative evaluation.

## 4. Evaluation Metrics

Failure detection rate:
Detected injected failures divided by injected failures,
reported separately for each threat category.

False acceptance rate:
Accepted cases divided by reference-rejected cases.

False rejection rate:
Rejected cases divided by reference-accepted cases.

Indeterminate rate:
Indeterminate predictions divided by all cases.

Decision coverage:
Non-indeterminate predictions divided by all cases.

Overall agreement:
Correct three-class predictions divided by all cases.

Also report acceptance of reference-indeterminate cases.

Report undefined metrics as NA when denominators are zero.

Report paired architecture differences and batch-level
variation without assuming scenario independence.

## 5. Evaluation Independence

Use the first 65 chronological batches for development
and the remaining 65 batches for evaluation.

Freeze scenario definitions, reference outcomes and
implementation versions before evaluation.

The original public dataset is not a blinded holdout.

Document protocol deviations before rerunning experiments.

## 6. Performance Evaluation

Report local verification latency and storage overhead.

Use equivalent workloads and execution conditions.

Separate local execution costs from network-dependent
submission and finality costs.

Do not extrapolate local measurements to public networks.

## 7. Publication Claims

The contribution is a reproducible comparative benchmark.

Do not claim universal blockchain superiority,
physical measurement accuracy or standards compliance.

Distinguish historical source commitments from newly
generated experimental commitments.

Historical on-chain verification remains outstanding.

## 8. Approval

Literature and novelty: Conditional GO.
Data feasibility: GO based on preliminary audit.
Methodology: Conditional GO pending approval and tests.
Scientific contribution: GO for chapter development.

Implementation requires explicit protocol approval.
