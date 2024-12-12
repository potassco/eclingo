#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(
    description="Create a PDDL domain that admits a reverse plan of length n."
)

parser.add_argument("n", type=int, help="number of fluents to reverse")
parser.add_argument("--i", type=int, default=0, help="number of irrelevant fluents")
args = parser.parse_args()

print(f"(define (domain rev-{str(args.n)}-{str(args.i)} )")
print("  (:requirements :strips)")
print("  (:predicates", end=" ")
for j in range(args.n):
    print(f"(f{j})", end=" ")
for j in range(args.i):
    print(f"(i{j})", end=" ")
print(")")
print()

print("  (:action del-all")
print("   :precondition (and ", end=" ")
for j in range(args.n):
    print(f"(f{j})", end=" ")
print(")")
print("   :effect (and ", end=" ")
for j in range(args.n):
    print(f"(not (f{j}))", end=" ")
print(")")
print("  )")
print()

for j in range(args.n):
    print(f"  (:action add-f{j}")
    if j > 0:
        print(f"   :precondition (f{j-1})")
    print(f"   :effect (f{j})")
    print("  )")
    print()

for j in range(args.i):
    print(f"  (:action rem-i{j}")
    print(f"   :precondition (i{j})")
    print(f"   :effect (not (i{j}))")
    print("  )")
    print()
print(")")
