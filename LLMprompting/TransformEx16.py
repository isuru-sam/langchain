from llmapi import get_completion

text1 = """
   Dude go and check the requirement document.
    """
#language or letter
summary_template ="""
Your are asked translate below slang text into formal business language.

The text is delimited by <> 
<{text}>
"""
print(get_completion(summary_template,text1))