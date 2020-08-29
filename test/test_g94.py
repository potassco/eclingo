from helper_test.helper_parsing import ParsingTestHelper

class Test(ParsingTestHelper):

    def setUp(self) -> None:
        super().setUp()
        self.eclingo_semantics = "g94"

    def test_parsing_ground_programs(self):
        self.assert_equal_parsing_program('a :- &k{a}, a.', "u_a :- not not k_u_a, u_a. {k_u_a} :- u_a.")
        self.assert_equal_parsing_program('a :- not &k{a}, a.', "u_a :- not k_u_a, u_a. {k_u_a} :- u_a.")
        self.assert_equal_parsing_program('a :- &k{-a}, b.', "u_a :- not not k_sn_u_a, u_b. {k_sn_u_a} :- sn_u_a. sn_u_a :- -u_a.")

    # def test_ground_programs(self):
    #     self.assert_models(solve('a :- &k{a}.'), [[], ['&k{a}']])
    #     # self.assert_models(solve('a :- &k{a}. a:- not &k{a}.'), [])