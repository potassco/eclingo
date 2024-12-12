"""
If using conda, then be sure to be in the nox environment different from "base" before running this file.

To run all tests: nox -Rs all_tests
The above also runs coverage.
The follwing only run a subset of tests and they do not run coverage.
To run only fast test: nox -Rs tests
To run only slow test: nox -Rs slow_tests
"""
import os
import nox

IS_GITHUB = "GITHUB_ACTIONS" in os.environ

@nox.session
def format(session: nox.Session):
    session.install("black", "isort", external=IS_GITHUB)
    session.run("isort", "--profile", "black", "src/eclingo", external=IS_GITHUB)
    args = session.posargs if session.posargs else ["src/eclingo", "tests"]
    session.run("black", *args, external=IS_GITHUB)


@nox.session(python=None)
def typecheck(session: nox.Session):
    session.install("mypy", external=IS_GITHUB)
    session.install("-e", ".", external=IS_GITHUB)
    session.run("mypy", "--implicit-optional", "src/eclingo", external=IS_GITHUB)


@nox.session(python=None)
def all_tests(session: nox.Session):
    session.notify("tests")
    session.notify("slow_tests")
    session.notify("coverage")


@nox.session(python=None)
def tests(session: nox.Session):
    session.install("coverage", external=IS_GITHUB)
    session.install("-e", ".", external=IS_GITHUB)
    session.run(
        "coverage",
        "run",
        "--data-file",
        ".coverage_fast",
        "-m",
        "unittest",
        "tests/test_reification.py",
        "tests/test_reification2.py",
        "tests/test_reification3.py",
        "tests/test_reification4.py",
        "tests/test_reification5.py",
        "tests/test_eclingo.py",
        # "tests/test_grounder.py",
        "tests/test_generator_reification.py",
        "tests/test_literals.py",
        "tests/test_parsing.py",
        "tests/test_solver_reification.py",
        "tests/test_worldview_builder_reification.py",
        "tests/test_tester_reification.py",
        "tests/test_theory_atom_parser.py",
        "tests/test_transformers.py",
        "tests/test_util.py",
        "tests/test_preprocessor.py",
        "tests/test_propagator.py",
        "-v",
        external=IS_GITHUB,
    )


@nox.session(python=None)
def slow_tests(session: nox.Session):
    session.install("coverage", external=IS_GITHUB)
    # session.install("-r", "requirements.txt", external=IS_GITHUB)
    session.install("-e", ".", external=IS_GITHUB)
    session.run(
        "coverage",
        "run",
        "--data-file",
        ".coverage_slow",
        "-m",
        "unittest",
        "tests/test_app.py",
        "tests/test_eclingo_examples.py",
        "-v",
        external=IS_GITHUB,
    )


@nox.session(python=None)
def coverage(session: nox.Session):
    session.install("coverage", external=IS_GITHUB)
    omit = ["src/eclingo/__main__.py", "src/eclingo/__init__.py", "tests/*", "helper_test/*"]
    session.run(
        "coverage",
        "combine",
        ".coverage_fast",
        ".coverage_slow",
        external=IS_GITHUB,
    )
    session.run(
        "coverage",
        "report",
        "--sort=cover",
        "--fail-under=99",
        "--omit",
        ",".join(omit),
        external=IS_GITHUB,
    )


@nox.session
def pylint(session: nox.Session):
    session.install("-e", ".", external=IS_GITHUB)
    session.install("pylint", external=IS_GITHUB)
    # session.install("-r", "requirements.txt", "pylint", external=IS_GITHUB)
    session.run("pylint", "src/eclingo", external=IS_GITHUB)


@nox.session
def lint_flake8(session: nox.Session):
    session.install("flake8", "flake8-black", "flake8-isort", external=IS_GITHUB)
    session.run("flake8", "src/eclingo", external=IS_GITHUB)
