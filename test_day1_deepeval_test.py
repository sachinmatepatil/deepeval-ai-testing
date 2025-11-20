import os
from deepeval.test_case import LLMTestCase
from deepeval.metrics import FaithfulnessMetric
from deepeval.evaluate import evaluate
from dotenv import load_dotenv
load_dotenv()

# # Set your API key
# os.environ["OPENAI_API_KEY"] = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

# Simple test case with very short prompt & response
test_case = LLMTestCase(
    input="What is an API?",
    actual_output="An API lets software talk to each other.",
    expected_output="An API allows two software systems to communicate using defined rules.",
    retrieval_context=[
        "An API (Application Programming Interface) allows communication between software components via requests and responses."
    ]
)

# Single metric to save cost
metrics = [
    FaithfulnessMetric(threshold=0.6)
]

# Run the test (will use very few tokens)
evaluate([test_case], metrics)
