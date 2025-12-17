# AI Kata – Learning Intelligence CLI Tool

## Overview
This project is an AI-powered Learning Intelligence tool designed for internship or training platforms.
It analyzes learner behavior data and provides intelligent predictions and insights for mentors and administrators.

The tool is built as a **Command Line Interface (CLI)** application and integrates a trained Machine Learning model
to move beyond experimentation toward real-world AI deployment.

---

## Features
- Course completion prediction (Binary Classification)
- Early dropout risk detection
- Chapter difficulty analysis
- Human-readable insights for mentors and admins
- Production-style AI pipeline with saved ML models

---

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
