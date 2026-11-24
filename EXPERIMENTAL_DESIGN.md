# Experimental Design

Version: 0.1
Status: Draft

## 1. Study Design

Controlled, paired comparative experiments using
real measurement data and synthetic evidence failures.

The primary evaluation unit is a verification scenario
associated with a measurement batch.

All architectures receive equivalent evidence and
scenario conditions.

## 2. Data Partition

Expected source dataset: 130 measurement batches.

Development: first 65 chronological batches.
Evaluation: remaining 65 chronological batches.

This equal allocation is a research design choice.

Confirm batch counts and chronological ordering
during baseline reproduction.

Preserve the original batch boundaries.

Evaluation scenarios and reference outcomes must be
frozen before comparative testing.

Public source data are not a blinded holdout.

## 3. Architecture Configuration

All architectures use equivalent signed evidence.

A1: Digital signatures.
A2: Digital signatures with evidence rules.

B1: Witnessed transparency log.
B2: Witnessed transparency log with evidence rules.

C1: Blockchain anchoring.
C2: Blockchain anchoring with evidence rules.

Use equivalent authorization policies and verifier
history where applicable.

Use the same canonical evidence representation
across comparable architectures.

Original logger commitments must be reproduced
separately from new benchmark commitments.

## 4. Witness Configuration

Primary configuration:
- Four witnesses
- Three cosignatures required
- At most one compromised witness

Any two quorums intersect in at least two witnesses.

Under the stated fault assumption, the intersection
contains at least one honest witness.

Evaluate witness compromise and unavailability
separately.

Document quorum safety and availability limitations.

This configuration is a research choice, not a
mandatory requirement of the witness protocol.

## 5. Blockchain Configuration

Use local Ethereum execution for contract-level tests.

Evaluate transaction inclusion, commitment ordering
and contract behavior.

Treat consensus security and finality assumptions
separately from measured contract behavior.

Do not generalize local execution results to the
security or performance of public Ethereum.

## 6. Scenario Design

Derive scenarios from requirements R01-R10
and threat categories T01-T12.

Include:
- Unmodified controls
- Single evidence failures
- Combined evidence failures
- Boundary conditions
- Valid but unusual evidence
- Unavailable evidence
- Infrastructure compromise assumptions

Synthetic metadata must be explicitly labelled.

Do not assign physical measurement truth without
independent reference evidence.

## 7. Reference Outcomes

Define expected outcomes independently of the
verification implementation.

ACCEPT:
Evidence satisfies the declared decision policy.

REJECT:
Evidence demonstrates a policy violation.

INDETERMINATE:
Available evidence is insufficient for a decision.

Reference outcomes must be justified and recorded
before comparative testing.

Separate underlying injected failures from the
evidence available to each verifier.

A hidden failure is not necessarily detectable.

## 8. Evaluation Metrics

Report:
- Failure detection rate by threat category
- False acceptance rate
- False rejection rate
- Indeterminate outcome rate
- Three-class confusion matrices
- Verification latency
- Storage overhead
- Trust dependencies

Define all metric denominators explicitly.

Report paired differences between architectures.

Do not treat repeated scenarios from the same batch
as independent observations.

Report decision coverage separately from correctness.

## 9. Independent Validation

Separate scenario generation, reference outcomes
and verification logic.

Include independent reference tests for cryptographic
primitives and verification functions.

Freeze evaluation scenarios before comparative tests.

Reset scenario-specific state where independence
is required.

Preserve explicit history for sequential scenarios.

Document all exclusions and failed tests.

## 10. Sensitivity Analysis

Evaluate the effects of:
- Witness availability and compromise
- Verifier history availability
- Missing evidence
- Combined failures
- Batch size variation

Additional numerical parameters require
documented justification before implementation.

## 11. Interpretation Boundaries

The study evaluates defined verification mechanisms
under explicit assumptions.

It does not estimate real-world attack prevalence.

It does not establish universal blockchain superiority.

It does not establish physical measurement accuracy.

## 12. References

RFC 9162, Certificate Transparency Version 2.0.
https://doi.org/10.17487/RFC9162

RFC 9943, An Architecture for Trustworthy and
Transparent Digital Supply Chains.
https://doi.org/10.17487/RFC9943

C2SP Transparency Log Witness Protocol v1.1.0.
https://c2sp.org/tlog-witness@v1.1.0

W3C Verifiable Credentials Data Model v2.0.
https://www.w3.org/TR/2025/REC-vc-data-model-2.0-20250515/
