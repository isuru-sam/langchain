from llmapi import get_completion

text = """
    srilanka is in asia.capital is colombo.
    It is situated from indian ocean.
    It is famous for its ancient ruins and beautiful landscapes.
    Srilanka has beautiful rivers and canals flowing covering many parts of the island.
    There are hills and mountains which add to the beauty of this country.
    Srilanka is famous for cricket and once they becaem world champions.
    National sport in Sri lanka is vlleyball.
    """
summary_template =f"""
Your task is to summarize a text wrtten on Sri Lanka.
Summarize the text delimited by <> 
<{text}>
"""
print(get_completion(summary_template,text))