from llmapi import get_completion
data_json = {"instructors":[{"name":"Mark Taylor","Age":50,"location":"Texas"},
                            {"name":"John Peter","Age":60,"location":"Delhi"},
                            {"name":"Jemes Border","Age":70,"location":"Tokyo"}]}
text1 = """
   Dude go and check the requirement document.
    """
#language or letter
summary_template ="""
Your are asked translate a json text in a python dictionary  into HTML table \
with column headers and titles

The json text is delimited by <> 
<{text}>
"""
print(get_completion(summary_template,data_json))