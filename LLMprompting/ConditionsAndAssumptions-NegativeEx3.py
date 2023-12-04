import openai


text = """
 srilanka is in asia.capital is colombo.
    It is situated from indian ocean.
    It is famous for its ancient ruins and beautiful landscapes.
    Srilanka has beautiful rivers and canals flowing covering many parts of the island.
    There are hills and mountains which add to the beauty of this country.
    """
summary_template = f"""
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
print(get_completion(summary_template))





