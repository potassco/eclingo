# Changes

## eclingo 0.2.1
  * allows to use "not" inside epistemic literals. Now "a :- &k{ not b}." is a valid program.
  * works with (and requires) clingo 5.5 and python 3.8.
  * Semantics K14 is not supported in this version.
  * Grounding is done only once instead of twice.
