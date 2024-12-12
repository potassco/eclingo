from eclingo.config import AppConfig
from helper_test.helper_parsing import ParsingTestHelper

# python -m unittest tests.test_g94.Test.


class Test(ParsingTestHelper):
    def setUp(self) -> None:
        super().setUp()
        self.config: AppConfig = AppConfig(semantics="g94")

    def test_parsing_ground_programs(self):
        self.maxDiff = None

        self.assert_equal_parsing_program(
            "a :- &k{a}, a.", "u(a) :- not not k(u(a)), u(a). {k(u(a))} :- u(a)."
        )
        # self.assert_equal_parsing_program(
        #     "a :- not &k{a}, a.",
        #     "u(a). :- not k(u(a)), u(a). {k(u(a))} :- u(a)."
        # )
        # self.assert_equal_parsing_program(
        #     "a :- &k{-a}, b.",
        #     "u(a) :- not not k_sn_u_a, u(b). {k_sn_u_a} :- sn_u_a. sn_u_a :- -u_a.",
        # )

    # def test_ground_programs(self):
    #     self.assert_models(solve('a :- &k{a}.'), [[], ['&k{a}']])
    #     # self.assert_models(solve('a :- &k{a}. a:- not &k{a}.'), [])
