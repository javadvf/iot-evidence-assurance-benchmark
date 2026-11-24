# Research Protocol

## Project Title
When Does Blockchain Add Value to IoT Evidence Assurance?
A Comparative Benchmark of Cryptographic Verification
and Decision Reliability

## Protocol Status
Version: 0.1
Status: Draft - pending scientific approval

## 1. Research Objective
Determine the additional assurance provided by blockchain
compared with conventional cryptographic verification
under controlled evidence failure conditions.

## 2. Research Questions
RQ1: Which evidence failures can different verification
architectures detect?

RQ2: Under which trust and failure conditions does
blockchain provide additional assurance?

RQ3: How do independent evidence-validation rules affect
incorrect acceptance, rejection, and unresolved outcomes?

## 3. Data Source
https://github.com/javadvf/solar_logger

Preliminary audit:
- 10,268 stored measurement rows
- 8,106 unique measurement records
- 2,162 duplicate rollover rows
- 130 Merkle batches
- 8,085 records referenced by proof metadata
- 21 unsubmitted records

All preliminary results must be independently reproduced
within this repository.

Original source files must remain unchanged.
The source commit and file hashes must be recorded.

## 4. Verification Architectures
A1: Digital signatures
A2: Digital signatures + evidence-validation rules
B1: Witnessed transparency log
B2: Witnessed transparency log + evidence-validation rules
C1: Blockchain anchoring
C2: Blockchain anchoring + evidence-validation rules

Equivalent source authentication and evidence rules
must be applied across comparable architectures.

Architecture-specific trust assumptions must be explicit.

## 5. Evaluation Method
- Controlled fault injection
- Paired comparison of verification architectures
- Independent reference outcomes
- Protected evaluation scenarios
- Combined failure scenarios
- Sensitivity and robustness analysis

The primary evaluation unit is the verification scenario
or measurement batch, not individual sensor rows.

## 6. Evaluation Metrics
- Failure detection rate
- False acceptance rate
- False rejection rate
- Indeterminate outcome rate
- Verification latency
- Storage overhead
- Trust dependencies

## 7. Scientific Integrity
- No unsupported novelty claims
- No unjustified hardcoding
- No fabricated experimental data
- Explicit identification of synthetic scenarios
- No evaluation leakage
- No selective reporting
- No undocumented protocol deviations
- No claims of physical accuracy based solely on hashes

## 8. Reproducibility
- Preserve original data and provenance
- Record software dependencies and versions
- Use minimal, documented code
- Separate development and evaluation scenarios
- Use APA 7 references with verified DOI or URL
- Prepare reproducibility materials for GitHub and Zenodo

## 9. Known Limitations
- Single-device measurement dataset
- Independent physical calibration not established
- On-chain transaction verification pending
- Synthetic failures do not establish real-world prevalence
- Local blockchain execution cannot establish public
  network security guarantees

## 10. Outstanding Approval Requirements
- Complete standards-to-requirements mapping
- Define threat models and trust assumptions
- Finalize independent validation procedure
- Finalize evaluation partition and metrics
- Confirm scientific novelty
- Confirm publication conditions

Implementation must not begin before protocol approval.
