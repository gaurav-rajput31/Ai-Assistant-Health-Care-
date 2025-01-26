from transformers import pipeline

# Load a question-answering pipeline
qa_pipeline = pipeline("question-answering")

def get_response(question, context):
    response = qa_pipeline(question=question, context=context)
        return response['answer']
        