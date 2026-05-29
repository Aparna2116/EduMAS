# EduMAS — Adaptive Multi-Agent Learning System

EduMAS is an AI-powered adaptive education platform developed using a Multi-Agent System (MAS) architecture. The platform generates personalized lessons, creates quizzes dynamically, evaluates student performance, stores learning history, and adapts future learning difficulty based on student progress.

The system integrates Large Language Models (LLMs), semantic memory, adaptive learning logic, and orchestration frameworks to simulate an intelligent educational assistant capable of personalized tutoring.

---

# Project Objectives

- Generate personalized educational content dynamically
- Adapt lesson difficulty according to student performance
- Maintain persistent student learning memory
- Automate quiz generation and evaluation
- Demonstrate the practical implementation of multi-agent AI systems
- Provide an interactive full-stack educational platform

---

# Core Features

- AI-generated lessons using LLMs
- Dynamic quiz generation
- Automated quiz evaluation and scoring
- Adaptive learning difficulty adjustment
- Persistent semantic memory using vector databases
- Multi-agent orchestration workflow
- Interactive web-based frontend
- REST API backend services
- Automated unit testing

---

# Multi-Agent Architecture

EduMAS is composed of multiple specialized AI agents, each responsible for a dedicated task within the system.

| Agent | Responsibility |
|---|---|
| Adaptive Agent | Determines the next learning difficulty level |
| Curriculum Agent | Generates personalized educational lessons |
| Quiz Agent | Generates quiz questions dynamically |
| Scoring Agent | Evaluates student answers and calculates scores |
| Memory Agent | Stores and retrieves semantic learning history |
| Student Agent | Logs student sessions and performance data |

---

# System Workflow

```text
Student
↓
Streamlit Frontend
↓
FastAPI Backend
↓
LangGraph Orchestrator
↓
Adaptive Agent
↓
Curriculum Agent
↓
Quiz Agent
↓
Scoring Agent
↓
Memory Agent
↓
SQLite + ChromaDB