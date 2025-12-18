# AI Kata – Learning Intelligence CLI Tool

## Overview
This project is an AI-powered Learning Intelligence tool designed for internship or training platforms.
It analyzes learner behavior data and provides intelligent predictions and insights for mentors and administrators.

The tool is built as a **Command Line Interface (CLI)** application and integrates a trained Machine Learning model
to move beyond experimentation toward real-world AI deployment.

---
## AI System Architecture

The tool follows a production-style AI pipeline:

1. Data Ingestion  
   - Loads learner activity data from CSV files

2. Preprocessing & Validation  
   - Ensures schema correctness and cleans missing values

3. Feature Engineering  
   - Aggregates chapter-level logs into student-level learning signals

4. Model Inference  
   - Loads a pre-trained Logistic Regression model
   - Predicts course completion probability

5. Intelligence Layer  
   - Early dropout risk detection using model confidence and performance rules
   - Chapter difficulty analysis using dropout rate, time spent, and scores

6. Insight Generation  
   - Converts predictions and analytics into human-readable insights for mentors and admins

## Features
- Course completion prediction (Binary Classification)
- Early dropout risk detection
- Chapter difficulty analysis
- Human-readable insights for mentors and admins
- Production-style AI pipeline with saved ML models

---
## Why These Features?

The model uses explainable, behavior-driven features:

- Average score → learning performance
- Total time spent → effort and engagement
- Chapters completed → progress
- Score trend → improvement or decline over time
- Time per chapter → learning difficulty

These features allow transparent reasoning behind predictions and risk flags.

## Input Format
The tool accepts a CSV file containing learner activity data with the following columns:

| Column | Description |
|------|------------|
| student_id | Unique student identifier |
| course_id | Course identifier |
| chapter_order | Chapter sequence number |
| time_spent | Time spent on chapter (minutes) |
| score | Assessment score |
| completion_status | 1 = completed, 0 = dropped |

Example:
```csv
S101,C01,1,30,75,1

## AI Usage Disclosure

AI assistance (ChatGPT) was used for:
- High-level architectural guidance
- Code organization suggestions
- Documentation clarity

All core logic — including feature engineering, model selection, training, risk rules,
chapter difficulty logic, testing, and validation — was independently implemented,
understood, and verified by the author.
