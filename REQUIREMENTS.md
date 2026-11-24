# Scientific and Technical Requirements

Status: Draft
Version: 0.1

## 1. Assurance Requirements

R01 - Data integrity
Detect changes to cryptographically committed records.

R02 - Source authentication
Verify the identity associated with a signing key.
Evaluate authorization separately from authentication.

R03 - Inclusion
Verify whether a record belongs to a committed batch.

R04 - History consistency
Evaluate whether successive commitments preserve
an append-only history.

R05 - Non-equivocation
Evaluate conflicting histories presented to
different relying parties under explicit trust assumptions.

R06 - Evidence completeness
Evaluate whether the required records and supporting
evidence are available.

R07 - Freshness
Evaluate evidence against the applicable time requirements.

R08 - Semantic validity
Evaluate data structure, measurement units and
documented consistency constraints.

R09 - Institutional validity
Evaluate applicable issuer authorization, certificate
validity and supporting evidence.

R10 - Decision reliability
Distinguish accepted, rejected and indeterminate outcomes.

## 2. Requirement Sources

R01-R02:
National Institute of Standards and Technology. (2023).
Digital signature standard (DSS). FIPS 186-5.
https://doi.org/10.6028/NIST.FIPS.186-5

R03-R04:
Laurie, B., Messeri, E., & Stradling, R. (2021).
Certificate transparency version 2.0. RFC 9162.
Sections 2.1.3 and 2.1.4.
https://doi.org/10.17487/RFC9162

R04-R05:
Birkholz, H., Delignat-Lavaud, A., Fournet, C.,
Deshpande, Y., & Lasker, S. (2026).
An architecture for trustworthy and transparent
digital supply chains. RFC 9943.
Sections 4 and 5.1.3.
https://doi.org/10.17487/RFC9943

R06-R10:
World Wide Web Consortium. (2025).
Verifiable credentials data model v2.0.
https://www.w3.org/TR/vc-data-model-2.0/

United Nations Economic Commission for Europe. (n.d.).
Transparency graphs.
https://untp.unece.org/docs/design-patterns/TrustGraphs/

Blockchain consensus assumptions:
Ethereum.org. (n.d.). Proof-of-stake (PoS).
Section: Finality.
https://ethereum.org/developers/docs/consensus-mechanisms/pos/

## 3. Experimental Constraints

- Apply equivalent source authentication across architectures.
- Apply identical evidence rules where applicable.
- Explicitly document architecture-specific trust assumptions.
- Separate observed failures from synthetic failures.
- Do not equate cryptographic validity with physical accuracy.
- Do not assume that missing evidence is fraudulent.
- Do not treat indeterminate outcomes as successful verification.
- Do not claim standards compliance without conformance testing.
- Justify all numerical thresholds before implementation.

## 4. Scope

These requirements are research operationalizations informed
by the cited sources. They are not a formal certification
or standards-conformance checklist.

Measurement-specific thresholds and threat models remain
subject to scientific approval.
