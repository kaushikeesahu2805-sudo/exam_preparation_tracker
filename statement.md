# Problem Statement

## Problem
In the first semester, a student has to prepare for several subjects at the same time. It is easy to forget which topics are already studied, which ones are weak, and how many days are left for each exam. Most students keep this in their head or on loose paper, so revision is often left to the last few days.

## Scope of the Project
- A console (text based) program written only in Python.
- Covers three subjects with three subtopics each:
  - **Calculus** - Limit, Continuity, Partial Derivative
  - **Python** - List, Dictionary, Array
  - **Environmental Sustainability** - Photochemical Smog, Air Pollution, Water Pollution
- Progress is stored in a simple JSON file. No database is used.
- Not included: login system, graphical screen, internet features.

## Target Users
First-semester engineering students (especially CSE) who want a simple way to plan and track their exam preparation.

## High-Level Features
1. **Syllabus and progress tracking** - mark topics as studied and rate confidence from 1 to 5.
2. **Practice score log** - store practice test scores (out of 10) for every topic and see the average.
3. **Study planner and report** - set exam dates, see days left, get a list of weakest topics to revise first, and view a progress report with progress bars.
4. Input validation and automatic saving of progress.
