from llmapi import get_completion


summary_template = f"""
Your task is to answer in consistent style.
<child>: Tell me how to play cricket
<teacher>: to play cricket you need 11 players.\
First find 11 players.
Also you need 2 umpires to curate the match
You need a bat and ball to play cricket.
You need a large  vacant flat ground to play.
<child>:Tell me how to play volleyball
"""
print(get_completion(summary_template))
