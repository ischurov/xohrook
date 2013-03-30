import markdown as md

class Markup:
    def __init__():
        pass

    def process(text, output):
        """
        - text is a Markdown text
        - output is one of 'HTML', 'LaTeX'
        """
        assert text.__class__ == u'a'.__class__
        assert output in [ 'HTML' ]
        return md.markdown(text)