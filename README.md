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


## 📘 Day 2 — Understanding LLM Output Randomness

### 🔍 Objective
To demonstrate how Large Language Models (LLMs) like GPT-3.5 can produce **non-deterministic outputs** when generating text — even for the same prompt.

---

### ⚙️ What This Script Does

- Calls an OpenAI LLM twice with the **same prompt**
- Uses a moderate temperature (e.g., 0.9) to allow variation
- Prints both outputs
- Shows the differences using Python’s `unified_diff`

---

### 🧪 Prompt Used

```
Explain what API testing is in one short paragraph.
```

---

### 🧠 Key Concepts Learned

| Concept           | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| 🔁 Non-determinism | LLMs generate different outputs due to randomness at higher temperatures     |
| 🔥 Temperature      | Controls randomness — higher = more creative, lower = more consistent        |
| 🧮 Tokens           | Words are broken into smaller chunks (tokens) during processing              |
| 📉 Top-p            | Nucleus sampling — selects from top % of most likely tokens                 |
| 🤯 Hallucination    | When LLM gives factually incorrect answers confidently                      |

---

### 🧵 Sample Output (partial)

```diff
- API testing ensures that APIs return correct data and follow expected behavior.
+ API testing validates endpoints by sending requests and verifying responses.
```

---

🧠 Day 3 — Built-in + Custom LLM Metrics (DeepEval)

🗂️ File: day3_llm_eval.py
🎯 Goal: Evaluate LLM output using:

✅ AnswerRelevanceMetric (checks if the answer is relevant)

✅ ContextPrecisionMetric (checks if answer is grounded in context)

🛠️ FactualAccuracyMetric (custom rule-based metric)

🔍 Prompt Tested
Input:        "What is the capital of France?"
Expected:     "Paris is the capital of France."
Actual:       "The capital of France is Paris."
Context:      ["France is a country in Europe. Paris is its capital."]

📊 Output Sample (Console)
Metric: Answer Relevance | Score: ✅ 1.0 | Status: PASSED
Metric: Context Precision | Score: ✅ 1.0 | Status: PASSED
Metric: Factual Accuracy (custom) | Score: ✅ 1.0 | Status: PASSED

🧪 Custom Metric Logic

Simple rule: If "paris" is present in the actual answer → score = 1.0

This simulates a factual validation check (can be extended with NLP logic or regex)

💡 What I Learned

How to run multiple evaluation metrics together

How to create my own BaseMetric subclass in DeepEval

Hands-on practice of LLM output validation techniques used in real-world GenAI products

----------------------------------------------------