# eclingo

> A solver for epistemic logic programs.

![Travis](https://travis-ci.com/javiergarea/eclingo.svg?token=UsJRkwzSfzyEzdaYoHPd&branch=master&status=passed)
![GitHub](https://img.shields.io/github/license/javiergarea/eclingo?color=blue)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/javiergarea/eclingo)

---

## Description
`eclingo` is a solver for epistemic logic programs built upon the ASP system [`clingo`](https://github.com/potassco/clingo).  
Currently, `eclingo` can compute world views under the following semantics:
- Gelfond 1991 (G91) [[1]](#references)
- Kahl 2015 (K15) [[2]](#references)

## Dependencies

- `python 3.6`
- `clingo 5.4.0` Python module.

## Installation

### Clone

Clone this repo:
```
git clone https://github.com/javiergarea/eclingo.git
```

### Setup

Change your directory and install `eclingo`:
```
cd eclingo/
pip install .
```

## Usage

```
$ eclingo --help
eclingo version 1.0.0
usage: eclingo [-h] [-n MODELS] [-k] [-op OPTIMIZATION] [-c CONST]
               input_files [input_files ...]

positional arguments:
  input_files           path to input files

optional arguments:
  -h, --help            show this help message and exit
  -n MODELS, --models MODELS
                        maximum number of models to compute (0 computes all
                        models)
  -k, --k15             computes world views under K15 semantics
  -op OPTIMIZATION, --optimization OPTIMIZATION
                        number of optimization to use (0 for no optimizations)
  -c CONST, --const CONST
                        adds a constant to the program (using '<name>=<term>'
                        format)
```

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
p :- not &k{ ~ q }.
```

#### Show statements
Show statements follow `clingo`'s syntax but, in eclingo, they refer to *subjective atoms*.

For example, the show statement:
```
#show p/1.
```
refers to the subjective atom `&k{p/1}`.


#### Constant definitions

`eclingo` accepts constant definitions in the same way as `clingo` does.
For example, to declare the constant `length` with value `2`, the following statement is written:
```
#const length=2.
```

### Examples

This repo contains a set of example scenarios inside the `test` folder.

- The `prog` folder, includes some basic programs.
- The `eligible` folder, includes the knowledge base and a set of 25 instances of the *Scholarship Eligibility Problem*.
- The `yale` folder, includes the knowledge base and a set of 13 instances of the *Yale Shooting Problem*.
- The `paths` folder, includes the knowledge base and a set of 5 instances of a custom search problem that involves directed graphs.


#### Simple example

Run `eclingo` passing the input files paths as arguments.

```
$ eclingo test/eligible/eligible.lp test/eligible/input/eligible10.lp
eclingo version 1.0.0
Solving...
Answer: 1
&k{ -eligible(van) }    &k{ eligible(mary) }    &k{ eligible(nancy) }   &k{ eligible(paul) }    &k{ eligible(sam) }     &k{ eligible(tim) }
SATISFIABLE

Elapsed time: 0.011072 s
```
> Note that you can provide several paths to split the problem encoding from its instances.

#### Computing `n` models

The `-n` flag allows the user to select the maximum number of models to compute (0 for all models).

```
$ eclingo test/prog/input/prog02.lp -n 0
eclingo version 1.0.0
Solving...
Answer: 1
&k{ a }
Answer: 2
&k{ b }
SATISFIABLE

Elapsed time: 0.004526 s
```
> By default, `eclingo` computes just one model.

#### Solving a conformant planning problem
We can use the `-c` flag to declare a constant.
In the case of a planning problem, this is useful to indicate the length of the path:
```
$ eclingo test/yale/yale.lp test/yale/input/yale04.lp -c length=4
eclingo version 1.0.0
Solving...
Answer: 1
&k{ occurs(load, 0) }   &k{ occurs(load, 2) }   &k{ occurs(pull_trigger, 1) }   &k{ occurs(pull_trigger, 3) }
SATISFIABLE

Elapsed time: 0.058982 s
```

## License

- **[MIT license](https://github.com/javiergarea/eclingo/blob/master/LICENSE)**

---

## References

[1] M. Gelfond. Strong introspection. pages 386–391. AAAI Press / The MIT Press, 1991.

[2] P. Kahl, R. Watson, E. Balai, M. Gelfond, and Y. Zhang. The language of epistemic specifications (refined) including a prototype solver. Journal of Logic and Computation, 2015.
