#!/usr/bin/env python

from eval.sp import sp_el
import functools
import re
import operator
from sage.all import GF, PolynomialRing
import string
import sys
from enum import StrEnum

sys.setrecursionlimit(10000)


class Result(StrEnum):
    SAT = "sat"
    UNSAT = "unsat"
    UNKNOWN = "unknown"


def strip_comments(s: str) -> str:
    return "\n".join((l[: l.index(";")] if ";" in l else l) for l in s.splitlines())


def parse_s_exprs(s: str):
    s = s.replace("(", " ( ").replace(")", " ) ")
    toks = s.split()
    stack = [[]]
    for tok in toks:
        if tok == "(":
            stack.append([])
        elif tok == ")":
            back = stack.pop()
            if not stack:
                return None
            stack[-1].append(back)
        else:
            if not stack:
                return None
            stack[-1].append(tok)
    if len(stack) != 1:
        return None
    return stack[0]


def parse_file(path: str):
    return parse_s_exprs(strip_comments(open(path).read()))


def expand_lets(s, bindings={}):
    if isinstance(s, str):
        if s in bindings:
            return bindings[s]
        else:
            return s
    else:
        if s and s[0] == "let":
            old = []
            for k, v in s[1]:
                vv = expand_lets(v)
                old.append((k, bindings[k] if k in bindings else None))
                bindings[k] = vv
            out = expand_lets(s[2], bindings)
            for k, v in reversed(old):
                bindings[k] = v
                if v is None:
                    del bindings[k]
            return out
        else:
            return [expand_lets(c, bindings) for c in s]


ast = parse_file(sys.argv[1])
ast = expand_lets(ast)


class Unknown(Exception):
    pass


def or_unknown(b, reason=""):
    if not b:
        raise Unknown(reason)


def san_name(s: str) -> str:
    s = re.sub("[^a-zA-Z0-9_]", "", s)
    if s[0] not in string.ascii_letters:
        s = "letstart" + s
    return s


class SimpleFfSolver:
    def __init__(self):
        self.fields = {}
        self.field_vars = set()
        self.var_polys = {}
        self.assertions = []
        self.field = None
        self.poly_ring = None
        self.zero_polys = []
        self.nz_polys = []

    def cmd(self, cmd):
        match cmd:
            case ["define-sort", name, [], ["_", "FiniteField", size]]:
                or_unknown(len(self.fields) == 0, "multiple fields")
                self.fields[name] = GF(int(size))
                self.field = GF(int(size))
            case ["set-info", *_]:
                pass
            case ["set-logic", logic]:
                or_unknown(logic == "QF_FF", "logic")
            case ["declare-fun", name, [], sort_name]:
                or_unknown(sort_name in self.fields, f"bad sort {sort_name}")
                self.field_vars.add(name)
            case ["declare-const", name, sort_name]:
                or_unknown(sort_name in self.fields, f"bad sort {sort_name}")
                self.field_vars.add(name)
            case ["assert", term]:
                self.assertions.append(term)
            case ["check-sat"]:
                return self.check()
            case _:
                or_unknown(False, f"{cmd}")

    def poly(self, term):
        match term:
            case ["=", a, b]:
                return self.poly(a) - self.poly(b)
            case ["as", ff_lit, field]:
                return self.field(ff_lit[2:])
            case ["ff.mul", *args]:
                return functools.reduce(operator.mul, (self.poly(p) for p in args))
            case ["ff.add", *args]:
                return sum(self.poly(p) for p in args)
            case ["ff.neg", a]:
                return -self.poly(a)
            case var:
                if (m := re.match(r"#f(-?\d+)m(\d+)", var)) is not None:
                    return self.field(int(m.group(1)))
                if isinstance(var, str):
                    return self.var_polys[san_name(var)]
        or_unknown(False, f"term {term}")

    def flatten(self, assertion):
        match assertion:
            case ["not", ["=>", a, b]]:
                self.flatten(a)
                self.flatten(["not", b])
            case ["not", ["=", a, b]]:
                self.nz_polys.append(self.poly(assertion[1]))
            case ["=", a, b]:
                self.zero_polys.append(self.poly(assertion))
            case ["and", *args]:
                for a in args:
                    self.flatten(a)
            case ["or", *args]:
                self.zero_polys.append(
                    functools.reduce(operator.mul, (self.poly(a) for a in args))
                )
            case _:
                or_unknown(False, f"assertion {assertion}")

    def check(self):
        assert len(self.fields) == 1
        self.field = list(self.fields.values())[0]
        self.field_vars.add(INV_VAR)
        self.poly_ring = PolynomialRing(
            self.field, list(map(san_name, self.field_vars))
        )
        self.var_polys = self.poly_ring.gens_dict()
        for a in self.assertions:
            self.flatten(a)
        if self.nz_polys:
            self.zero_polys.append(
                self.var_polys[INV_VAR] * functools.reduce(operator.mul, self.nz_polys)
                + 1
            )
        result = sp_el(self.poly_ring, self.zero_polys)
        if result is False:
            return Result.UNSAT
        return Result.SAT


INV_VAR = "inversevar"

r = Result.UNKNOWN
try:
    s = SimpleFfSolver()
    for cmd in ast:
        rr = s.cmd(cmd)
        if rr is not None:
            r = rr
except Unknown as e:
    print(e, file=sys.stderr)

print(r)
