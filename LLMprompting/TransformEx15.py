from llmapi import get_completion

text1 = ["Welcome","Hello"]
for text2 in text1:
    summary_template ="""
    Your are asked translate below text into French.

    The text is delimited by <> 
    <{text}>
    """
    translated = get_completion(summary_template, text2)
    print(translated)