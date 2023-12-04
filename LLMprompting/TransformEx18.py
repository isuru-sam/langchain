from llmapi import get_completion

text1 = ["Srilanka has had been beatifulest country",\
         " It has a nashional isport kallled voliball",\
         "Sri lanka is being place at indian oshion"]
for text2 in text1:
    summary_template ="""
    Your are asked proofread and correct below text.

    The text is delimited by <>
    <{text}>
    """
    translated = get_completion(summary_template, text2)
    print(translated)