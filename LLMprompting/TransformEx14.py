from llmapi import get_completion

text1 = """
    Hola Mundo!
    """
summary_template ="""
Which language is below text.

The text is delimited by <> 
<{text}>
"""
print(get_completion(summary_template,text1))