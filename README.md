# IoT Evidence Assurance Benchmark

Reproducibility materials for the manuscript:

**When Does Blockchain Add Value to IoT Evidence Assurance?
A Comparative Benchmark of Cryptographic Verification
and Decision Reliability**

Author: Javad Vasheghani Farahani

## Overview

This repository provides a controlled comparative benchmark
of six IoT evidence-assurance architectures.

| ID | Infrastructure | Additional evidence rules |
|---|---|---|
| A1 | Digital signatures | No |
| A2 | Digital signatures | Yes |
| B1 | Witnessed transparency log | No |
| B2 | Witnessed transparency log | Yes |
| C1 | Ethereum anchoring | No |
| C2 | Ethereum anchoring | Yes |

The benchmark distinguishes cryptographic verification,
shared-history assurance, and evidence appraisal.

## Dataset

The benchmark uses historical solar energy measurements
from the original solar logger repository:

https://github.com/javadvf/solar_logger

Pinned source commit:

ec34ea5dc21642744d39eb436b787ac092505d0f

- Historical observation duration: 135.08 hours
- Unique measurement records: 8,106
- Committed measurement records: 8,085
- Measurement batches: 130
- Development batches: 65
- Reserved evaluation batches: 65
- Core scenarios per batch: 19
- Reserved core verification decisions: 7,410

Historical Ethereum receipts and block responses are
archived separately from the newly generated experimental
commitments.

## Principal findings

| Metric | Without evidence rules | With evidence rules |
|---|---:|---:|
| Reference agreement | 52.63% | 100% |
| False acceptance | 66.67% | 0% |
| Acceptance with insufficient evidence | 25% | 0% |
| Hidden-failure acceptance | 100% | 100% |

These core results apply individually to each infrastructure
family under the corresponding evidence-policy configuration.

Shared-history infrastructures provide additional protection
against conflicting commitments under specified trust
assumptions.

Complete reference agreement represents conformance to
the experimental policy, not physical measurement accuracy.

## Repository structure

    notebooks/
      01_baseline_verification.ipynb
      02_benchmark_development.ipynb
      03_benchmark_evaluation.ipynb
      04_publication_finalization.ipynb

    data/
      SHA256SUMS
      source_url.txt
      source_commit.txt
      sepolia_blocks.json
      sepolia_receipts.json

    results/reserved_evaluation/
      evaluation_results.json
      SHA256SUMS
      figure_01_architectures.svg
      figure_02_experimental_design.svg
      figure_03_decision_reliability.svg
      figure_04_witness_sensitivity.svg
      figure_05_conflicting_evidence.svg
      figure_06_verification_cost.svg

    tools/
      finalize_publication_figures.py
      solidity/
        package.json
        package-lock.json

    EVALUATION_FREEZE.json
    EVALUATION_PROTOCOL.md
    EXPERIMENTAL_DESIGN.md
    PROTOCOL.md
    PROTOCOL_ADDENDUM.md
    PROTOCOL_AMENDMENT_01.md
    PROTOCOL_AMENDMENT_02.md
    PROTOCOL_AMENDMENT_03.md
    REQUIREMENTS.md
    THREAT_MODEL.md
    requirements.txt

## Reproduction

### 1. Environment

The original evaluation uses:

- ARM64 macOS
- Python 3.12.2
- PyCryptodome 3.24.1
- EthereumTester 0.14.0b1
- Py-EVM 0.12.1b1
- Solidity 0.8.36
- Node.js and npm

Python dependencies are pinned in requirements.txt.
Solidity dependencies are pinned in package-lock.json.

From a fresh checkout of this repository:

    python3.12 -m venv .venv
    .venv/bin/python -m pip install -r requirements.txt
    npm ci --prefix tools/solidity

Register the Python kernel:

    .venv/bin/python -m ipykernel install --user \
      --name iot-evidence-assurance \
      --display-name "Python (IoT Evidence Assurance)"

A separate Jupyter frontend is required.

### 2. Retrieve the original dataset

From a fresh checkout, run:

    git clone https://github.com/javadvf/solar_logger.git data/raw

    git -C data/raw checkout --detach \
      ec34ea5dc21642744d39eb436b787ac092505d0f

The raw source repository is excluded from version control.
Preserve the original source files without modification.

### 3. Execute the notebooks

Use the registered IoT Evidence Assurance Python kernel.

Execute the notebooks in numerical order:

1. Historical evidence verification.
2. Benchmark development and validation.
3. Reserved comparative evaluation.
4. Publication figure finalization.

Use a separate working checkout for reproduction.
Preserve the frozen development notebook byte-for-byte,
including its archived contents, because its SHA-256
fingerprint is part of the evaluation freeze.

Do not save changes to the frozen notebook before running
the reserved evaluation.

Inspect the verification and integrity checks in each
notebook before proceeding.

### 4. Verify results

The archived numerical results and publication figures
are located in results/reserved_evaluation/.

SHA-256 manifests document source-file integrity and
archived result integrity.

EVALUATION_FREEZE.json records the frozen experimental
specification and implementation fingerprints.

Verification latency may vary across hardware,
software environments, and repeated executions.

## Experimental limitations

- The historical dataset represents one IoT deployment.
- Evidence failures and institutional certificates are synthetic.
- The reserved partition is not a blinded external holdout.
- Reference agreement measures experimental policy conformance.
- Local Ethereum execution does not establish public-network
  consensus security or performance.
- External replication has not yet been established.

## License

Original software and notebook code: MIT.

Original research outputs and documentation:
Creative Commons Attribution 4.0 International (CC BY 4.0).

See LICENSE and LICENSE-DATA.md for licensing boundaries.
Third-party materials retain their respective rights.

## Citation

Please cite the repository using CITATION.cff.

The associated manuscript citation and permanent archival
DOI will be added when available.
