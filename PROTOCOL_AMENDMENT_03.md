# Protocol Amendment 03

Date: 2026-11-24
Status: Approved by researcher

## 1. Core Experimental Scenarios

ID    | Intervention                          | Reference
------|---------------------------------------|--------------
T00   | Unmodified control                    | ACCEPT
T01   | Post-commitment modification          | REJECT
T02   | Pre-commitment measurement alteration | ACCEPT
T03   | Record omission                       | REJECT
T04   | Duplicate record                      | REJECT
T05   | Replay of previously accepted evidence| REJECT
T05b  | Temporal inconsistency                | REJECT
T06   | Unauthorized signing key              | REJECT
T07   | Compromised authorized signing key    | ACCEPT
T08   | Incorrect measurement unit            | REJECT
T10a  | Expired certificate                   | REJECT
T10b  | Tampered certificate                  | REJECT
T10c  | Unauthorized certificate issuer       | REJECT
T11a  | Missing certificate                   | INDETERMINATE
T11b  | Unavailable evidence payload          | INDETERMINATE
T11c  | Unavailable retained history          | INDETERMINATE
T11d  | Missing source signature              | INDETERMINATE
T12a  | Incorrect unit and missing certificate| REJECT
T12b  | Invalid signature and missing cert.   | REJECT

These reference decisions concern the common target
evidence policy, not the capabilities of a particular
architecture.

T02 and T07 are accepted only when all observable
mandatory conditions are satisfied.

Acceptance does not establish physical measurement
truth or absence of signing-key compromise.

Record underlying failures, observable evidence and
verification decisions separately.

## 2. Conflicting-History Experiments

T09a: Conflicting signed batches with identical
sequence identifiers and previous commitments.

T09b: Conflicting histories presented to isolated
verifiers.

T09c: Conflicting witness-quorum attempts with one
compromised witness.

T09d: Conflicting commitments submitted to the same
Ethereum contract position.

T09e: Different local blockchain histories presented
to isolated verifiers.

Distinguish conflicting claims from conflicting
infrastructure histories.

Distinguish detection from prevention.

T09e evaluates trust assumptions, not public Ethereum
consensus security.

Multi-party reference outcomes must be specified
independently before comparative evaluation.

## 3. Boundary Conditions

BC01: Application timestamp equals final measurement.
Reference: ACCEPT.

BC02: Application timestamp equals window end.
Reference: ACCEPT.

BC03: Certificate exactly covers required interval.
Reference: ACCEPT.

BC04: Unusual but structurally valid finite value.
Reference: ACCEPT.

BC05: Application timestamp immediately outside window.
Reference: REJECT.

BC06: Certificate expires immediately before the
required interval ends.
Reference: REJECT.

One-microsecond offsets are implementation boundary
tests, not physical accuracy thresholds.

## 4. Sensitivity Analysis

Evaluate:

- Witness availability: zero to four witnesses.
- Witness compromise: zero to four witnesses.
- Retained history availability.
- Inclusion-proof validity and availability.
- Consistency-proof validity and availability.
- Ethereum transaction-reference validity and availability.
- Ethereum backend availability.
- Observed batch size variation.

The primary witness assumption remains at most one
compromised witness with a three-of-four quorum.

Higher compromise counts are explicitly outside
the primary trust assumption.

Report infrastructure-specific failures separately
from the common-policy comparison.

## 5. Experimental Controls

For post-commitment failures, preserve original
signatures and infrastructure commitments.

For pre-commitment failures, create valid signatures
and commitments for the modified evidence.

Regenerate affected record hashes where required
to avoid unintended additional integrity failures.

Use equivalent evidence and retained history across
comparable architectures.

Restrict ledger access to the relevant experimental
verification point.

Prevent access to future ledger state.

Reset scenario-specific state where required.

Preserve original historical data.

## 6. Planned Experimental Scale

Development batches: 65.
Evaluation batches: 65.

Core scenarios per evaluation batch: 19.
Core evaluation cases: 1235.
Architecture decisions: 7410.

These counts exclude separate conflicting-history,
boundary-condition, sensitivity and performance tests.

Repeated scenarios and architecture decisions from
the same batch are statistically dependent.

## 7. Outstanding Pre-Evaluation Requirements

- Implement temporally restricted ledger verification.
- Finalize deterministic scenario interventions.
- Define independent scenario reference outcomes.
- Define failure-specific detection attribution.
- Distinguish batch inclusion from selective record inclusion.
- Validate all scenarios using development data.
- Freeze scenarios, references and implementation versions.

This amendment records approval of the experimental
design. It does not constitute the final evaluation freeze.

## 8. Interpretation Boundaries

No claims of universal blockchain superiority,
physical measurement accuracy, real-world attack
prevalence or public-network consensus security.

All previous approved protocol constraints remain
applicable.
