
__author__ = 'Milan'

import argparse
from ravnina import *


def kreiraj_vektor(arg):
    clean = arg.strip()
    clean = clean.strip("(")
    clean = clean.strip(")")
    parts = clean.split(",")
    return Vector(int(parts[0]), int(parts[1]))


parser = argparse.ArgumentParser(description="Program zbraja i oduzima vektore.")

parser.add_argument("--add", nargs=2,
                    help="Zbraja dva vektora formata (x,y) i ispisuje njihov zbroj")
parser.add_argument("--sub", nargs=2,
                    help="Oduzima dva vektora formata (x,y) i ispisuje njihovu razliku")
parser.add_argument("--verbose", action="store_true",
                    help="Ispisuje prikladne poruke uz rezultate")
parser.add_argument("--debug", action="store_true",
                    help="Ispisuje detaljne poruke iznimki")

args = parser.parse_args()

if args.debug:
    print("Debug je ukljucen.")

if args.add:
    try:
        vectors = args.add
        a = kreiraj_vektor(vectors[0])
        b = kreiraj_vektor(vectors[1])
        c = a + b
        if args.verbose:
            print("Zbroj vektora {} i {} je vektor ".format(a, b), end="")
        print(c)

    except Exception as ex:
        if args.debug:
            print(ex)
        else:
            print("Doslo je do pogreske. Za vise informacija pokrenite program s opcijom --debug.")

elif args.sub:
    try:
        vectors = args.sub
        a = kreiraj_vektor(vectors[0])
        b = kreiraj_vektor(vectors[1])
        c = a - b
        if args.verbose:
            print("Razlika vektora {} i {} je vektor ".format(a, b), end="")
        print(c)

    except Exception as ex:
        if args.debug:
            print(ex)
        else:
            print("Doslo je do pogreske. Za vise informacija pokrenite program s opcijom --debug.")