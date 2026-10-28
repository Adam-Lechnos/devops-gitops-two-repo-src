# Enterprise App Source & CI Pipeline (`devops-gitops-two-repo-src`)

[![CI & Release Pipeline](https://github.com/adam-lechnos/devops-gitops-two-repo-src/actions/workflows/ci.yml/badge.svg)](https://github.com/adam-lechnos/devops-gitops-two-repo-src/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository houses the application source code and continuous integration (CI) workflows for a secure, enterprise-grade **Two-Repo GitOps architecture**. It decouples application development from cluster configuration, pairing with the [Infrastructure & GitOps Repo](https://github.com/adam-lechnos/devops-gitops-two-repo-infra) to manage automated deployments.

---

## 🏗️ Architectural Overview

* **Separation of Duties:** Developers push application code here; environment configuration and Kubernetes manifests live strictly in the [Infra Repo](https://github.com/adam-lechnos/devops-gitops-two-repo-infra).
* **Dual-Path Versioning Strategy:**
  * **Development (Bleeding Edge):** Every push to `main` builds a container image tagged with a short Git SHA (`sha-abc1234`) and automatically updates the Dev overlay.
  * **Releases (Stable):** Pushing a Semantic Version tag (`v*.*.*`) triggers a dedicated release pipeline to build immutable artifacts for QA and Production promotion.

---

## 🚀 CI/CD Workflows

1. **`ci.yml` (Continuous Integration):** Triggered on pushes to `main` and Pull Requests. Runs unit tests, builds container images, pushes to GitHub Container Registry (GHCR), and automatically updates the Dev Kustomize overlay in the [Infra Repo](https://github.com/adam-lechnos/devops-gitops-two-repo-infra) via a Fine-Grained PAT.
2. **`release.yml` (Release Management):** Triggered exclusively by SemVer tag pushes (`v1.0.0`), building formal release candidate images for pre-production testing.

---

## 🛠️ Tech Stack
* **Language:** Python / Flask
* **CI/CD:** GitHub Actions
* **Registry:** GitHub Container Registry (GHCR)
* **GitOps Target:** [devops-gitops-two-repo-infra](https://github.com/adam-lechnos/devops-gitops-two-repo-infra)