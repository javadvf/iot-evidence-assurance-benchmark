# Protocol Amendment 01

Date: 2026-11-24
Status: Approved by researcher

## Scope

Extend T05 (freshness and replay) with:

T05b - Temporal inconsistency.

## Empirical Justification

Historical verification identified inconsistent
application-generated timestamps in all 130 batches,
despite matching cryptographic commitments.

The discrepancy is consistent with timezone-naive
datetime conversion.

The historical device timezone remains unverified.

## Experimental Treatment

- Evaluate temporal inconsistency across all six
  approved verification architectures.
- Preserve original historical timestamps.
- Use the historical discrepancy as descriptive evidence.
- Generate separately labelled synthetic temporal failures.
- Apply identical temporal validation policies across
  comparable architectures.
- Define reference outcomes independently.
- Do not automatically apply the observed two-hour offset.
- Do not treat previously inspected historical evidence
  as independent holdout results.

## Scope Preservation

All other approved research requirements, evaluation
methods and interpretation boundaries remain unchanged.
