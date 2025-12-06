from deepeval.test_case import LLMTestCase
from deepeval.metrics.answer_relevancy import AnswerRelevancyTemplate
from deepeval.metrics.contextual_precision import ContextualPrecisionTemplate
from deepeval.test_run import TestRun
from deepeval.metrics.base_metric import BaseMetric

from dotenv import load_dotenv

from test_day1_deepeval_test import test_case

load_dotenv()
import os

class FactualAccuracyMetric(BaseMetric):
    def __init__(self):
        super().__init__(name="Factual Accuracy")

    def measure(self, test_case: LLMTestCase, *args, **kwargs) -> float:
        expected_fact = "paris"
        return 1.0 if expected_fact in test_case.actual_output.lower() else 0.0

    def is_successful(self,score:float) -> bool:
        return score >= 1.0
#-----------------
# LLM Test Case
#-----------------
test_case = LLMTestCase(
    input="what is the capital of France?",
    actual_output="The capital of France is Paris.",
    expected_output="The capital of France is Paris.",
    retrieval_context=["France is a country in Europe. Its capital is Paris."]
)

#-----------------
# Metrics to run
#----------------
metrics = [
    AnswerRelevancyTemplate(threshold=0.7),
    ContextualPrecisionTemplate(threshold=0.7),

]

test_run = TestRun()
test_run.run(test_case, metrics)