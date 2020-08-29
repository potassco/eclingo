class AppConfig(object):
    """
    Class for application specific options.
    """

    def __init__(self):
        self.eclingo_verbose = 0
        self.eclingo_project_test = False
        self.eclingo_add_efacts = False
        self.eclingo_semantics = "g94" #"c19-1"
