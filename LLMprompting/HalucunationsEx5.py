from llmapi import get_completion

summary_template = """
    Tell me about elephant tooth brush.
"""
print(get_completion(summary_template))
