# Protocol Amendment 02

Date: 2026-11-24
Status: Approved by researcher

## 1. Canonical Evidence Refinement

Extend the common signed evidence representation
with explicit measurement-unit declarations.

Required units:

- voltage: V
- current: A
- power: W
- energy_Wh: Wh
- cumulative_energy_Wh: Wh

Increment the benchmark evidence schema version.

Recalculate development commitments and revalidate
all three cryptographic infrastructures.

Preserve the original historical data and commitments.

## 2. Evidence Completeness (R06)

Compare available records with an independently
supplied expected record count.

Evaluate the availability of mandatory supporting
evidence.

## 3. Freshness (R07)

Evaluate chronological ordering, expected sequence,
application timestamp consistency and independently
supplied synthetic time windows.

The first original measurement defines the window start.
The original submission proof timestamp defines its end.

Require:

window_start <= first_measurement <= last_measurement
<= application_timestamp <= window_end

These boundaries are experimental policy parameters,
not operational service-level requirements.

Do not automatically correct inconsistent timestamps.

## 4. Semantic Validity (R08)

Evaluate required fields, finite numerical values,
declared units, source consistency and duplicate
measurement identifiers.

Do not introduce unsupported physical accuracy
or sensor thresholds.

## 5. Institutional Validity (R09)

Use independently signed synthetic certificates.

Evaluate:

- Issuer identity and authorization
- Certificate signature
- Subject identity
- Subject public key binding
- Validity period
- Authorized scope

Certificate validity must cover the measurement
and application timestamp interval.

Certificates do not establish physical sensor accuracy.

## 6. Decision Reliability (R10)

ACCEPT: All mandatory conditions are satisfied.

REJECT: At least one mandatory condition is
demonstrably violated.

INDETERMINATE: Mandatory evidence is missing or
unverifiable, with no demonstrated violation.

A proven violation takes precedence over missing evidence.

## 7. Experimental Controls

Apply identical policy conditions across A2, B2 and C2.

Preserve equivalent source authentication across
all six architectures.

Keep independent policy context separate from
submitted evidence and hidden scenario labels.

Document synthetic metadata and certificate provenance.

Complete development validation before freezing
evaluation scenarios and reference outcomes.

## 8. Interpretation Boundaries

The policy is a research operationalization.

It does not establish standards compliance,
physical measurement accuracy or institutional
certification in real-world environments.
