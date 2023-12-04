from llmapi import get_completion

text = """
    srilanka has beautiful rivers and canals flowing covering many parts of the island.
    There are hills and mountains which add to the beauty of this country.
    Srilanka is famous for cricket and once they became world champions.
  
    """
summary_template =f"""
What is the sentiment of the given review about Srilanka
Use the text delimited by <> 
<{text}>
"""
print(get_completion(summary_template,text))