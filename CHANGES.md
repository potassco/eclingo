# Changes

## eclingo 0.2.1
  * Fixes the parsing avoiding that rules of the form "a :- not &k{b}." get wrongly removed when "b" does not occur in any rule head.
  * it allows to use "not" inside epistemic literals. Now "a :- &k{ not b}." is a valid program.
  * It works with (and requires) clingo 5.5 and python 3.8.
  * Semantics K14 is not supported in this version.
  * Grounding is done only once instead of twice.