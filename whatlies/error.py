class NotInstalled:
    """
    This object is used for optional dependencies. If a backend is not installed we
    replace the transformer/language with this object. This allows us to give a friendly
    message to the user that they need to install extra dependencies as well as a link
    to our documentation page.
    """

    def __init__(self, tool, dep):
        self.tool = tool
        self.dep = dep

    def __call__(self, *args, **kwargs):
        msg = f"In order to use {self.tool} you'll need to install via;\n\n"
        msg += f"pip install whatlies[{self.dep}]\n\n"
        msg += "See installation guide here: https://rasahq.github.io/whatlies/#installation."
        raise ModuleNotFoundError(msg)
