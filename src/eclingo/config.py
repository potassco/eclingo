class AppConfig(object):
    """
    Class for application specific options.
    """

    def __init__(
        self,
        semantics="g94",
        verbose=0,
        eclingo_rewritten="no",
        rewritten_program=[],
        preprocessing_level=0,
        propagate=True,
        ignore_shows=False,
    ):
        self.eclingo_verbose = verbose
        self.eclingo_semantics = semantics
        self.eclingo_rewritten = eclingo_rewritten
        self.rewritten_program = rewritten_program
        self.preprocessing_level = preprocessing_level
        self.propagate = propagate
        self.ignore_shows = ignore_shows
