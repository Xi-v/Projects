from transformers import pipeline

# Load the question-answering pipeline with a valid model
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

# Example context
context = """
x = k/14
"""

# Ask a question about the context
question = "Rearrange the question so that k is the subject"

# Use the pipeline to answer the question based on the context
result = qa_pipeline(question=question, context=context)

# Print the result
print(f"Question: {question}")
print(f"Answer: {result['answer']}")
