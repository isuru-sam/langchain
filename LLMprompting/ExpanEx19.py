from llmapi import get_completion

text1 = """
   The course content is satisfactory.\
   Ellaboration and articulation is  beyond expected standards.\
   Course content covers a lot of depth and breath for the subject.\
   I recomend this course for everyone.
    """

text1_negative = """
   The course content is not covering expected topics.\
   Ellaboration and articulation is  below expected standards.\
   I do not recomend this course for everyone.
    """
summary_template ="""
You are a Course providers support service AI assistant.
Your are asked to send an email reply to a regular student of your courses.
Given the student email seperated by ''',\
Generate a reply to thanks for the course review.
If the sentiment is negative ask the student to keep in touch with support team.
Write the reply in concise ans professional manner.
Sign the email as 'AI support agent'

The text is delimited by <> 
<{text}>
"""
#print(get_completion(summary_template,text1_negative))
#temperature setting more temp more creative
print(get_completion(summary_template,text1_negative,temperature=0.7))