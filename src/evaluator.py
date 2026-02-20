def simple_grounding_check(answer, contexts):
    context_text = " ".join(contexts)
    return any(word in context_text for word in answer.split())