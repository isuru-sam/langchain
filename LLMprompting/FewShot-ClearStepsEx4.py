from llmapi import get_completion


text = """
    srilanka is in asia.capital is colombo.
    It is situated from indian ocean.
    It is famous for its ancient ruins and beautiful landscapes.
    Srilanka has beautiful rivers and canals flowing covering many parts of the island.
    There are hills and mountains which add to the beauty of this country.
    """
summary_template = """
    1.Summarize the below text delimited by <> in 1 sentence.
    2.Translate the summary into french
    
    
    <{text}>
"""
print(get_completion(summary_template,text))
