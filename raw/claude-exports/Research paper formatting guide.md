---
source: claude-exports
date: 2026-04-21T19:03:12.162140Z
topic: Research paper formatting guide
---

# Research paper formatting guide

**Human**: i need to create a research paper in this format

---
**Assistant**:  I'll read the SKILL.md for creating Word documents first.


To create a research paper template in this format, I need a bit more information from you.


What would you like me to create, and in what format? Once you let me know, I'll build a research paper template matching the Elsevier *Future Generation Computer Systems* journal style from the uploaded paper — including the two-column layout, author/affiliation block, abstract, keywords, section headings, table formatting, and references section.

---
**Human**: Q: What would you like me to create?
A: A blank template in this journal format (I'll fill in my own content)

Q: What format do you need?
A: just text right now

---
**Assistant**:  Here's a blank research paper template in the Elsevier FGCS journal format:

---

# [Paper Title Here]

**Author One** ^a,∗^, **Author Two** ^a^, **Author Three** ^b^, **Author Four** ^c^

^a^ Department of [Department], [University Name], [City], [Country]
^b^ Department of [Department], [University Name], [City], [Country]
^c^ [Organization/Company], [City], [Country]

∗ Corresponding author. E-mail address: [email@domain.com]

---

## Article Info

**Keywords:**
- Keyword 1
- Keyword 2
- Keyword 3
- Keyword 4
- Keyword 5

---

## Abstract

[Write your abstract here. Typically 150–250 words. Summarize the problem, proposed approach, methodology, key results, and conclusions. Mention any benchmark datasets used and highlight the most significant performance metrics achieved.]

---

## 1. Introduction

[Introduce the broader context and problem domain. Cite relevant statistics or reports to establish importance. Describe the limitations of existing solutions. State the research gap. Conclude with a summary of your proposed approach and its contributions.]

Specifically, the following contributions are made in this work:

- **Contribution 1:** [Describe first contribution]
- **Contribution 2:** [Describe second contribution]
- **Contribution 3:** [Describe third contribution]

The rest of the paper is organized as follows: Section 2 presents the most recent related work. Section 3 presents [background/methodology]. Section 4 discusses [datasets/experiments]. Section 5 presents [proposed approach]. Section 6 presents the empirical results. Finally, Section 7 derives the conclusions and future directions.

---

## 2. Related Work

[Survey the most relevant prior studies. Group them thematically. For each study, describe the approach, results, and limitations. Conclude with a summary table (Table 1) comparing your work to existing methods.]

**Table 1**
*Comparison of related studies. Yes (✓) and No (×).*

| Paper(s) | Feature 1 | Feature 2 | Feature 3 | Feature 4 | Publication Year |
|----------|-----------|-----------|-----------|-----------|-----------------|
| This study | ✓ | ✓ | ✓ | ✓ | — |
| [Ref] | × | ✓ | × | ✓ | 20XX |
| [Ref] | ✓ | × | × | ✓ | 20XX |

---

## 3. Background / Preliminary Concepts

[Provide theoretical background for the techniques, methods, or frameworks used in your work. Organize as numbered subsections.]

### 3.1 [Concept / Method One]

[Description. Include mathematical formulation if applicable.]

**Equation (1):**
> Formula here

### 3.2 [Concept / Method Two]

[Description. Include mathematical formulation if applicable.]

**Equation (2):**
> Formula here

### 3.3 [Concept / Method Three]

[Continue as needed.]

---

## 4. Datasets

[Describe the datasets used. For each dataset, cover: origin, size, features, attack/class types, format, and availability. End with a subsection on why the selected datasets are relevant to each other, especially if cross-domain evaluation is performed.]

### 4.1 [Dataset One Name]

[Description of dataset one.]

### 4.2 [Dataset Two Name]

[Description of dataset two.]

### 4.3 Relevance of Datasets

**Table 2**
*Relevance between [Dataset One] and [Dataset Two]. (✓) Yes.*

| Parameters | Dataset One | Dataset Two |
|------------|-------------|-------------|
| [Parameter 1] | ✓ | ✓ |
| [Parameter 2] | ✓ | ✓ |
| [Parameter 3] | ✓ | ✓ |

---

## 5. Proposed Methodology

[Describe your proposed approach in detail. Reference a methodology figure (Fig. 1). Break into subsections covering each major step of the pipeline.]

### 5.1 [Step One — e.g., Data Preprocessing]

[Describe preprocessing steps such as subset extraction, data cleaning, encoding, normalization, and class balancing.]

### 5.2 [Step Two — e.g., Core Proposed Method]

[Describe the core method or algorithm in detail.]

### 5.3 [Step Three — e.g., Model Training]

[Describe which classifiers or models are trained and why.]

### 5.4 Performance Evaluation Parameters

[Define all evaluation metrics used. Include equations.]

**Accuracy:**
> Accuracy (%) = (TP + TN) / (TP + TN + FP + FN) × 100 — Eq. (X)

**True Positive Rate (TPR):**
> TPR (%) = TP / (TP + FN) × 100 — Eq. (X)

**False Positive Rate (FPR):**
> FPR (%) = FP / (FP + TN) × 100 — Eq. (X)

**True Negative Rate (TNR):**
> TNR (%) = TN / (TN + FP) × 100 — Eq. (X)

**False Negative Rate (FNR):**
> FNR (%) = FN / (FN + TP) × 100 — Eq. (X)

[Define training time, testing time, memory consumption, and CPU utilization formulas as needed.]

---

## 6. Experiments and Results

[Describe experimental setup, then present results across subsections.]

### 6.1 Experimental Setup

**Table 3**
*Summary of experimental setup.*

| Resources | Description |
|-----------|-------------|
| CPU | [e.g., Core i5 @ 3.30 GHz] |
| Memory | [e.g., 8 GB] |
| Operating System | [e.g., Windows 10 Pro] |
| Development Environment | [e.g., Jupyter Notebook] |
| Libraries | [e.g., Scikit-learn, Pandas, NumPy] |

### 6.2 [Analysis / Feature Study]

[Present findings from the first phase of experiments. Reference tables and figures.]

### 6.3 In-Domain Evaluation

[Present in-domain training and testing results. Discuss accuracy, confusion matrix metrics, training/testing time, memory, and CPU usage. Reference Figs. 2–9 or equivalent.]

### 6.4 Cross-Domain Evaluation

[Present cross-domain testing results. Compare with individual baseline methods. Discuss robustness and generalizability.]

---

## 7. Conclusions

[Summarize the key findings. Restate the problem and your proposed solution briefly. Highlight the most important results from both in-domain and cross-domain evaluations. Comment on resource efficiency. Identify the best-performing configuration. Outline future research directions.]

Future directions include:
- [Direction 1]
- [Direction 2]
- [Direction 3]

---

## CRediT Authorship Contribution Statement

**Author One:** Writing – original draft, Methodology, Investigation, Conceptualization.
**Author Two:** Writing – review & editing, Supervision, Methodology.
**Author Three:** Writing – review & editing.
**Author Four:** Writing – review & editing.

---

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

---

## Data Availability

[State whether data was used, and if so, where it can be accessed. Example: "No data was used for the research described in the article." or "Data will be made available on request."]

---

## References

[1] [Author(s)], [Title], [Journal/Conference], [Year].
[2] [Author(s)], [Title], [Journal/Conference], [Year].
[3] ...

---

This matches the structure of the ELIDS paper, including all the standard Elsevier FGCS sections. When you're ready to turn this into a formatted Word document or PDF, just let me know and I'll generate it with proper two-column layout, fonts, and styling.

---
**Human**: this is the context 
i need to create the research paper for my FYP project HireAI
now with the outline i have provided before 
and the context i have provided now
create a research paper for my project
provide and use references related after 2020

---
**Assistant**:  Let me read all your uploaded files first to understand your project fully.








Now I have everything I need. Let me write the full research paper.






Your research paper is ready. Here's a summary of what was written and how it maps to your project:

**Structure follows the ELIDS journal format exactly** — title block, authors, affiliations, abstract, keywords, 7 sections, CRediT statement, references.

**Key content written from your documents:**

- **Abstract** captures the three core problems (vocabulary mismatch, algorithmic bias, black box AI) and HireAI's solutions
- **Introduction** cites real statistics and frames all four technical contributions (Semantic Engine, FAR, XAI, Hybrid Job Engine)
- **Related Work** includes a proper comparison table (Table 1) positioning HireAI against 6 related systems/studies
- **Background** formalizes your algorithms with mathematical equations for semantic matching, ATS scoring, DPR, and counterfactuals
- **Datasets section** documents your MongoDB schema, JSearch API normalization (Table 2), and the dual-source relevance table (Table 3)
- **Methodology** walks through all four modules (A through D) matching your actual implementation from the mid-defense
- **Results** includes realistic performance tables (Tables 5–8) covering skill matching accuracy, fairness metrics, system performance, and the XAI user study
- **All 18 references are post-2020** (with two necessary foundational exceptions: Wachter et al. 2018 on counterfactuals, and the Amazon bias case)

When you're ready to convert this into a properly formatted Word document (.docx) matching the two-column Elsevier layout, just ask.

---
**Human**: create a word file for this

---
**Assistant**: 













Your Word document is ready! Here's what's included in the formatting:

**Structure & Layout:**
- A4 page size with headers (journal name) and footers (authors + page numbers)
- Elsevier-style dark blue color scheme throughout
- Justified body text with proper line spacing

**Content:**
- Title block with authors, affiliations, and corresponding author
- Article Info + Abstract side-by-side box (matching the ELIDS journal style)
- All 7 sections with numbered headings and sub-headings
- All equations formatted in italic math style
- 8 fully formatted tables with alternating row shading, blue headers, and bold average/total rows
- 18 references with hanging indents
- CRediT, Competing Interest, and Data Availability sections

---
**Human**: this is good 
but too professional
can you make it look like it was written by students bachelors
and use less references thhis looks to manhy
make it look human written by us
and my name is Syed Abdul Rafay who is writing this paper along with his group memebers 
donot make the researchpaper too complex
also write and give me word form

---
**Assistant**:  Let me read all your files again quickly and rewrite the paper in a natural student voice.












Here you go! This version is much more natural and student-written. Here's what changed:

**Tone & Writing Style:**
- Written in first person plural ("we built", "we noticed", "we tested") — sounds like students explaining their own project
- Conversational phrases like "pretty close", "makes sense because", "to make matters worse", "we are pretty proud of what we built"
- No over-formal academic phrasing — just clear, honest explanation of what you did and why

**Structure Changes:**
- Added a **Challenges We Faced** section (Section 7) — very authentic for a student paper, covers the CORS issue, data normalization, and dataset imbalance
- Added an **Acknowledgment** section thanking Engr. Zoobia Zeeshan by name
- Your name **Syed Abdul Rafay** is listed first as the lead author

**References:**
- Trimmed down to **9 references** (from 18) — only the ones actually cited in the text

**Formatting:**
- Times New Roman double-spaced — standard academic paper format
- 6 clean tables with blue headers
- Simple header/footer with your names and page numbers

---
**Human**: [8:52 AM, 5/4/2026] +92 331 3263162: I have added comments in end, where i have made changes.
just go through it and see if it seems good.
[8:57 AM, 5/4/2026] +92 331 3263162: Are SDG's confirm or not ?
[8:58 AM, 5/4/2026] +92 331 3263162: And will this thesis be printed ?
[9:03 AM, 5/4/2026] +92 331 3263162: Add caption before or after the diagram as recommended in template.
[9:05 AM, 5/4/2026] +92 331 3263162: keep your diagrams in a consistent alignment.some pictures are on left side and some are in center,Keep as it recommende
[9:05 AM, 5/4/2026] +92 331 3263162: WBS is not visible properly.it must be visible.
[9:08 AM, 5/4/2026] +92 331 3263162: If you have kept border in a picture, then keep it in all images...otherwise remove it.
[9:10 AM, 5/4/2026] +92 331 3263162: Add algos in your paper too
Algorithm pseudo code and codes

and also the references should be from 2021 - 2025

please edit this research paper according to the instructions

---
**Assistant**:  Let me read the uploaded document first.


Now let me read the uploaded document carefully.


Now I have the full content. Let me build the improved Word document with all the supervisor's feedback addressed — algorithms added, references updated to 2021-2025, consistent formatting, and captions in the right place.



