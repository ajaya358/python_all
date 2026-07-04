from transformers import pipeline

# This is a simple example; install transformers to run it.
# pip install transformers torch

classifier = pipeline("sentiment-analysis")
result = classifier("I love learning Python and AI")
print(result)
