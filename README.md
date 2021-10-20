# eclingo

> A solver for Epistemic Logic Programs.

![Travis](https://travis-ci.com/potassco/eclingo.svg?token=UsJRkwzSfzyEzdaYoHPd&branch=master&status=passed)
![GitHub](https://img.shields.io/github/license/potassco/eclingo?color=blue)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/potassco/eclingo)

---

## Description
`eclingo` is a solver for epistemic logic programs [[1]] built upon the ASP system [`clingo`](https://github.com/potassco/clingo).  
Currently, `eclingo` can compute world views under the following semantics:
- Gelfond 1991; Gelfond and Przymusinska 1993; Gelfond 1994 (G94) [[2, 3, 4]](#references)

## Dependencies

- `python 3.8
- `clingo 5.5.0` Python module.

## Installation

### Clone

Install the correct version of python and clingo:
```
conda create --name eclingo-0.2.1-dev python=3.8
conda activate eclingo-0.2.1-dev
conda install -c potassco/label/dev clingo=5.5.0 mypy
```

Clone this repo:
```
git clone https://github.com/potassco/eclingo.git
```

### Setup

Change your directory and install `eclingo`:
```
cd eclingo/
pip install .
```

## Usage


### Input language

`eclingo`'s syntax considers three types of statements:
- [Rules](#rules)
- [Show statements](#show-statements)
- [Constant definitions](#constant-definitions)

#### Rules

`eclingo` accepts rules with the same structure as `clingo` does. Additionally, `eclingo` allows these rules to include subjective literals in their body. These subjective literals are represented using the modal operator **K**, which is represented as `&k{}`. The expression inside the curly braces can be an explicit literal (that is, an atom `A` or its explicit negation `-A`) possibly preceded by default negation, that is represented inside the braces as `~`.

> Modal operator **M** is not directly supported but `M A` can be replaced by the construction `not &k{ ~ A}`.

For example, the epistemic logic program:
```
p <- M q.
```
is written under `eclingo`'s syntax as:
```
p :- not &k{ not q }.
```

#### Show statements
Show statements follow `clingo`'s syntax but, in eclingo, they refer to *subjective atoms*.

For example, the show statement:
```
#show p/1.
```
refers to the subjective atom `&k{p/1}`.

```

## License

- **[MIT license](https://github.com/potassco/eclingo/blob/master/LICENSE)**

---

## References

[1] Cabalar P., Fandinno J., Garea J., Romero J. and Schaub T. 2020. eclingo: A solver for Epistemic Logic Programs. In Theory and Practice of Logic Programming.

[2] Gelfond, M. 1991. Strong introspection. In Proceedings of the Ninth National Conference on Artificial Intelligence (AAAI’91), T. Dean and K. McKeown, Eds. AAAI Press / The MIT Press, 386–391.

[3] Gelfond, M. and Przymusinska, H. 1993. Reasoning on open domains. In Logic Programming and Non-monotonic Reasoning, Proceedings of the Second International Workshop, Lisbon, Portugal, June 1993, L. Moniz Pereira and A. Nerode, Eds. MIT Press, 397–413.

[4] Gelfond, M. 1994. Logic programming and reasoning with incomplete information. Annals of Mathematics and Artificial Intelligence 12, 1-2, 89–116.
