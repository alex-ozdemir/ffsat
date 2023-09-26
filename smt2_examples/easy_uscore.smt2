(set-logic QF_FF)
(set-info :smt-lib-version 2.6)
(set-info :category "crafted")
(define-sort F () (_ FiniteField 5))
(declare-const _x F)
(declare-const _1 F)
(assert (= _x _1))
(assert (not (= _x _1)))
(check-sat)


