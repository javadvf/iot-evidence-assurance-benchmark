# Threat Model

Version: 0.1
Status: Draft

## 1. Protected Assets

- Measurement records
- Source identities and signing keys
- Batch commitments
- Commitment history
- Supporting evidence
- Verification outcomes

## 2. Threat Categories

T01: Post-commitment modification
T02: Incorrect pre-commitment measurement
T03: Missing records
T04: Duplicate records
T05: Replay of old evidence
T06: Unauthorized issuer
T07: Compromised signing key
T08: Invalid measurement unit
T09: Conflicting commitment histories
T10: Invalid supporting certificate
T11: Unavailable supporting evidence
T12: Combined failures

## 3. Common Assumptions

All comparable architectures use equivalent signed
batch content, source identity information and
authorization policies.

Cryptographic primitives are assumed secure.

Key compromise is evaluated separately from
cryptographic primitive failure.

Evidence-validation rules are identical across
architectures where applicable.

Available evidence and retained verifier history
must be controlled across comparisons.

Original measurement accuracy is not assumed.

## 4. Architecture-Specific Assumptions

### A: Digital Signatures

Trust the registered signing keys.

Signatures authenticate signed content but do not
independently establish globally consistent history.

Locally retained commitments must be considered.

### B: Witnessed Transparency Log

Trust the configured witness policy.

Witnesses check consistency before cosigning
new checkpoints.

Witness compromise and witness unavailability
must be evaluated separately.

The witness configuration and quorum assumptions
must be justified before implementation.

### C: Blockchain Anchoring

Trust the specified consensus and finality assumptions,
contract logic and authenticated chain access.

Transaction inclusion does not establish the
truth of off-chain measurements.

A finalized blockchain history does not prevent
conflicting claims from being recorded by issuers.

Local blockchain execution tests contract behavior,
not decentralized network security.

## 5. Threat Boundaries

Distinguish:

- Pre-commitment and post-commitment failures
- Honest and compromised issuers
- Honest and compromised infrastructure
- Available and unavailable evidence
- Conflicting claims and conflicting ledger histories

All experimental failures must be introduced into
controlled research copies of the data.

No attacks against external production systems
are included.

## 6. Verification Outcomes

ACCEPT:
The available evidence satisfies the defined policy.

REJECT:
The available evidence violates the defined policy.

INDETERMINATE:
Insufficient evidence exists to establish an outcome.

Acceptance does not establish physical measurement truth.

## 7. Technical References

IETF RFC 9943:
https://doi.org/10.17487/RFC9943

IETF RFC 9162:
https://doi.org/10.17487/RFC9162

C2SP Transparency Log Witness Protocol v1.1.0:
https://c2sp.org/tlog-witness@v1.1.0

Ethereum proof-of-stake:
https://ethereum.org/developers/docs/consensus-mechanisms/pos/

## 8. Limitations

The benchmark evaluates defined failure scenarios.

It does not estimate real-world attack probabilities
or establish universal security guarantees.
