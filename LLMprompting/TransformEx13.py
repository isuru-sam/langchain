from llmapi import get_completion

text1 = """
    srilanka is in asia.capital is colombo.
    It is situated from indian ocean.
    It is famous for its ancient ruins and beautiful landscapes.
    Srilanka has beautiful rivers and canals flowing covering many parts of the island.
    There are hills and mountains which add to the beauty of this country.
    Srilanka is famous for cricket and once they became world champions.
    National sport in Sri lanka is Volleyball.
    """
summary_template ="""
Your are asked translate below text into French.

The text is delimited by <> 
<{text}>
"""
print(get_completion(summary_template,text1))