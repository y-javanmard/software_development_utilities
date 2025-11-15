# 🧪⚛️ Commit Messages — Quick Guide for Quantum/AI software engineering

A tiny, skimmable guide with icons. Keep it fast, clear, and useful for `git log` and releases.

## 🧭 Table of Contents
- 🎯 Motivation
- 🧱 Format
- ✍️ Header / 🧠 Body / 🔖 Footer
- 🧩 Common Types
- ✅ Examples (TFI/ED/Hamiltonian)
- 🧰 Template

---

## 🎯 Motivation
Consistent messages → readable history, reliable changelogs, painless reviews.

---

## 🧱 Commit Message Format
```
<type>(<scope>)!: <subject>

<body>

<footer>
```
- **Header required**; **scope optional**; `!` = breaking change.
- **Wrap at 100 chars** (aim ≤72 for the subject).

### ✍️ The Header (Subject)
- Imperative, present: **“add”, “fix”, “rename”**
- lowercase first letter; **no period**

### 🧠 The Body (optional, encouraged)
- Why + what changed; contrast previous vs new. If perf: note **hw/env + runs**.

### 🔖 The Footer
- `Closes #123`, `Refs #456`, `Co-authored-by:`
- **Breaking**: `feat(api)!: ...` **and/or** add
  ```
  BREAKING CHANGE: explain migration
  ```

---

## 🧩 Common Types

- 🏗️ **build** — build system, deps (CMake, conda, pyproject)
- 🧪 **test** — tests/fixtures/regressions
- 📚 **docs** — docs/tutorials/comments
- ✨ **feat** — new capability
- 🐛 **fix** — bug fix
- ⚡ **perf** — speed/scale (e.g., MPO contraction, caching)
- 🔧 **refactor** — code moves/renames w/o behavior change
- 🧹 **chore** — repo maintenance
- 🤖 **ci** — CI/CD configs (Actions, runners, cache)

**Extra (when useful):** 🔐 **security**, 🧪 **bench**, 📦 **data**

### 🔬 Suggested Scopes
`ed`, `hamiltonian`, `tfi`, `qpe`, `qsvt`, `lcu`, `qubitization`, `mps`, `mpo`, `sim`, `noisy-sim`,
`decoder`, `surface-code`, `xzzx`, `ldpc`, `qchem`, `pyscf`, `dmrg`, `block2`, `api`, `viz`, `deps`, `docker`

> If unsure, use a package/dir name: `feat(sim)`.

---

## ✅ Examples (TFI project)

**Feature**
```
feat(tfi): implement system+bath Hamiltonian builder

- J $\sigma^x \sigma^x$ NN coupling + local $h_z$ fields
- bath qubit with detuning $\Delta$ and XYZ interaction
- unit tests: $n=4$; spectra match ED baseline

Closes #42
```

**Fix**
```
fix(ed): correct tensor placement of σy at site i (zero-based index)

previous: off-by-one; wrong operator location
now: aligned with index; add shape check test
```

**Perf**
```
perf(mpo): cache environments; fuse legs in contraction

- 2.1× median speedup (RTX 6000 Ada, χ=256, L=512, 5 runs)
```

**Breaking**
```
feat(api)!: rename ED.sx -> ED.sigmax_list

BREAKING CHANGE: update imports and attribute names in callers.
```

---

## 🧰 Tiny Template (`.gitmessage`)
```
<type>(<scope>)!: <subject>

Why:
- 

What changed:
- 

Perf (if relevant):
- hw/env:
- runs:

Refs: #
BREAKING CHANGE:
```

---

### 📝 One-liners examples
- `feat(ed): add n-qubit spin-operator factory`
- `fix(hamiltonian): correct hx sign in TFI field`
- `perf(mpo): reuse env tensors for 2x faster sweeps`
- `refactor(api): split qsvt utilities into prep/select/signal`
- `docs(viz): clarify M1/M2 definitions`

