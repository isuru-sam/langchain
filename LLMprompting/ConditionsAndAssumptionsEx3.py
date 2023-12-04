import openai


from llmapi import get_completion


text1 = """
First Crack eggs in a bowl, add the milk, and whisk until yolks break.
Then Add milk, peppers, and onions and whisk again.
After that Put bowl in microwave and cook for 1 minute, checking occasionally.
Next Take out bowl, put omelet on a plate, sprinkle cheese and cook for 30 seconds to melt cheese.
Cooking done.Take out and enjoy! 
    """
summary_template ="""
You will be provided the text delimited by triple single quotes.
If it contains a sequence of instructions\ rewrite those instrucitons in following fromat.

Step1- ....
Step2- ....
.....- ....
StepN- ....

If the text does not contain a sequence of instructions, \ 
then simply write \"No steps provided\"

'''{text}'''



"""
print(get_completion(summary_template,text1))





