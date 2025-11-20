# 🧪 DeepEval AI Testing Project – Day 1

This project uses [DeepEval](https://github.com/confident-ai/deepeval) to test the output of LLMs using the `FaithfulnessMetric`.

## ✅ What This Does

- Sends a question to the LLM
- Compares actual vs expected response
- Scores how faithful the response is to a known context
- Prints score (e.g., ✅ PASSED if score > 0.7)

## 🧠 Prompt

**Input:** What is an API?  
**Actual Output:** An API lets software talk.  
**Expected Output:** An API allows two apps to communicate.  
**Context:** API stands for Application Programming Interface.

## 🚀 How to Run

1. Install dependencies:
pip install -r requirements.txt
2. Add your OpenAI API key to your environment variables:
3. Run the script:
