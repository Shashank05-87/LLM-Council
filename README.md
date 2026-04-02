#LLM Council

A Consensus-Based Question Answering System Using Multiple LLM Agents

Overview

Large Language Models (LLMs) are powerful but often suffer from hallucinations, incompleteness, and overconfidence when answering complex or open-ended questions.

This project implements an LLM Council architecture, where multiple independent LLM agents answer the same user query, and a judge LLM evaluates their responses to select the most reliable final answer.

The system demonstrates how model consensus can improve answer quality compared to using a single LLM.

Objectives:-

Reduce hallucinations in LLM-generated answers

Improve response reliability using consensus

Explore LLM-based evaluation and ranking

Build a domain-agnostic, research-inspired system

System Architecture:-

User Query
    
     ↓
     
LLM Agent 1 (Analytical)
LLM Agent 2 (Concise)
LLM Agent 3 (Detailed)
    
     ↓
     
Judge LLM (Evaluation & Selection)
    
     ↓
     
Final Consensus Answer

Key Components:-
1. Council Agents

    Multiple LLM agents with different reasoning styles

    Each agent uses a unique system prompt

    Agents do not communicate with each other

2. Judge Agent

    Evaluates all agent responses

    Ranks answers based on:

    Correctness

    Completeness

    Clarity

    Produces a final consensus answer

3. Orchestrator

    Coordinates the entire workflow

    Sends queries to agents

    Collects responses

    Passes results to the judge

🛠️ Technology Stack

   Programming Language: Python

  LLM API: OpenAI / Gemini / compatible LLM API

  Framework (Optional): LangChain

  Interface: Command Line Interface (CLI)

How It Works:-

User enters a question

The same question is sent to all council agents

Each agent generates an independent response

All responses are passed to the judge agent

The judge selects or synthesizes the best answer

The final response is displayed to the user


