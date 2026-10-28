# Enterprise App Source & CI Pipeline (`devops-gitops-two-repo-src`)

[![CI & Release Pipeline](https://github.com/adam-lechnos/devops-gitops-two-repo-src/actions/workflows/ci.yml/badge.svg)](https://github.com/adam-lechnos/devops-gitops-two-repo-src/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository houses the application source code and continuous integration (CI) workflows for a secure, enterprise-grade **Two-Repo GitOps architecture**. It decouples application development from cluster configuration, pairing with the [Infrastructure & GitOps Repo](https://github.com/adam-lechnos/devops-gitops-two-repo-infra) to manage automated deployments.

---

## 🏗️ Architectural Overview

- **Separation of Duties:** Developers push application code here; environment configuration and Kubernetes manifests live strictly in the [Infra Repo](https://github.com/adam-lechnos/devops-gitops-two-repo-infra).
- **Shift-Left Quality Gates:** Automated unit testing runs on every PR and push. Code must pass all tests before any container builds or GitOps promotions can occur.
- **Dual-Path Versioning Strategy:**
  - **Development (Bleeding Edge):** Every push to `main` executes unit tests, builds a container image tagged with a short Git SHA (`sha-abc1234`), and automatically updates the Dev overlay in the infra repo.
  - **Releases (Stable):** Pushing a Semantic Version tag (`v*.*.*`) triggers a dedicated release pipeline to build immutable artifacts for QA and Production promotion.

---

## 🧪 Testing & Local Development

This project uses `pytest` for robust route and environment variable testing. 

To run the unit test suite locally, execute:

    PYTHONPATH=. pytest -v

---

## 🚀 CI/CD Workflows

1. **`ci.yml` (Continuous Integration & Promotion):** Triggered on pushes to `main` and Pull Requests.
   - **Step 1 (Test):** Sets up Python 3.10 and runs the `pytest` suite. **If tests fail, the pipeline halts immediately.**
   - **Step 2 (Build & Push):** *Only runs if tests pass.* Builds an immutable Docker image and pushes it to the **GitHub Container Registry (GHCR)**.
   - **Step 3 (GitOps Update):** Automatically updates the Kustomize image tag (`overlays/dev/kustomization.yaml`) in the [Infra Repo](https://github.com/adam-lechnos/devops-gitops-two-repo-infra) via a Fine-Grained PAT, driving automated synchronization.

2. **`release.yml` (Release Management):** Triggered exclusively by SemVer tag pushes (`v1.0.0`), building formal release candidate images for pre-production testing.

---

## 🛠️ Tech Stack
- **Language & Framework:** Python / Flask
- **Testing:** Pytest
- **CI/CD Orchestration:** GitHub Actions
- **Registry:** GitHub Container Registry (GHCR)
- **GitOps Target:** [devops-gitops-two-repo-infra](https://github.com/adam-lechnos/devops-gitops-two-repo-infra)