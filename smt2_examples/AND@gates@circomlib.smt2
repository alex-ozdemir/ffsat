(set-logic QF_FF)
(set-info :smt-lib-version 2.6)
(set-info :category "crafted")
(define-sort F () (_ FiniteField 21888242871839275222246405745257275088548364400416034343698204186575808495617))
; ================================
; ======== original block ========
; ================================
; ======== declaration constraints ========
(declare-const x0 F)
(declare-const x1 F)
(declare-const x2 F)
(declare-const x3 F)
; ======== p definitions ========
(declare-const p F)
(assert (= p #f21888242871839275222246405745257275088548364400416034343698204186575808495617m21888242871839275222246405745257275088548364400416034343698204186575808495617))
(declare-const ps1 F)
(assert (= ps1 #f21888242871839275222246405745257275088548364400416034343698204186575808495616m21888242871839275222246405745257275088548364400416034343698204186575808495617))
(declare-const ps2 F)
(assert (= ps2 #f21888242871839275222246405745257275088548364400416034343698204186575808495615m21888242871839275222246405745257275088548364400416034343698204186575808495617))
(declare-const ps3 F)
(assert (= ps3 #f21888242871839275222246405745257275088548364400416034343698204186575808495614m21888242871839275222246405745257275088548364400416034343698204186575808495617))
(declare-const ps4 F)
(assert (= ps4 #f21888242871839275222246405745257275088548364400416034343698204186575808495613m21888242871839275222246405745257275088548364400416034343698204186575808495617))
(declare-const ps5 F)
(assert (= ps5 #f21888242871839275222246405745257275088548364400416034343698204186575808495612m21888242871839275222246405745257275088548364400416034343698204186575808495617))
(declare-const zero F)
(assert (= zero #f0m21888242871839275222246405745257275088548364400416034343698204186575808495617))
(declare-const one F)
(assert (= one #f1m21888242871839275222246405745257275088548364400416034343698204186575808495617))
; ======== main constraints ========
(assert (= (ff.mul ps1 (ff.mul x2 x3)) (ff.mul ps1 x1)))
(assert (= one one))
; ===================================
; ======== alternative block ========
; ===================================
; ======== declaration constraints ========
; x0: already defined
(declare-const y1 F)
; x2: already defined
; x3: already defined
; ======== p definitions: alt skip ========
; p definition placeholder
; p definition placeholder
; p definition placeholder
; p definition placeholder
; p definition placeholder
; p definition placeholder
; p definition placeholder
; p definition placeholder
; p definition placeholder
; p definition placeholder
; p definition placeholder
; p definition placeholder
; p definition placeholder
; p definition placeholder
; p definition placeholder
; p definition placeholder
; ======== main constraints ========
(assert (= (ff.mul ps1 (ff.mul x2 x3)) (ff.mul ps1 y1)))
(assert (= one one))
; ====================================
; ======== precondition block ========
; ====================================
; (no precondition or skipped by user)
; ========================================
; ======== extra constraint block ========
; ========================================
; =============================
; ======== known block ========
; =============================
(assert (= x0 x0))
(assert (= x2 x2))
(assert (= x3 x3))
; =============================
; ======== query block ========
; =============================
(assert (not (= x1 y1)))
(check-sat)
