import jinja2
import random

class PreprocessorException(Exception):
    def __init__(self):
        pass

class Preprocessor:
    """Dummy Preprocessor class."""
    def __init__(self):
        pass

    def process(self, code, text, seed=None):
        if seed != None:
            random.seed(seed)
        try:
            # Very insecure for now!
            module = compile(code, '', 'exec')
            localvars = {}
            eval(module, {'random': random}, localvars)
        except:
            raise PreprocessorException
        try:
            env = jinja2.Environment()
            template = env.from_string(text)
            parsed = template.render(**localvars)
            return parsed
        except:
            raise PreprocessorException


# some tests
if __name__ == '__main__':
    pp = Preprocessor()
    print pp.process("""
import math

r = range(1, 11)
random.shuffle(r)
seq = [(i, math.factorial(i), [str(i) for i in range(1, i+1)]) for i in r]
    """, """
# QUESTION
Answer the following questions:
{% for item in seq -%}
1. Factorial of which number is {{ item[1] }}?
{% endfor %}
# ANSWER
{% for item in seq -%}
1. {{ item[0] }}! = {{ item[1] }}.
{% endfor %}
# SOLUTION
{% for item in seq -%}
1. Try multiplying numbers one by one: {{ ', '.join(item[2]) }}. You will reach {{ item[1] }}.
{% endfor %}
    """, 3)
