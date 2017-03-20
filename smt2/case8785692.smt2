; 
(set-info :status unknown)
(declare-fun carg_var_buffer_to_upper_%b_0x4821910 () (_ BitVec 64))
(declare-fun gep_0x4822c60 () (_ BitVec 64))
(declare-fun var_buffer_to_upper_%used_0x4822ad0 () (_ BitVec 64))
(assert
 (let (($x35 (or (= carg_var_buffer_to_upper_%b_0x4821910 (_ bv0 64)) (and (distinct carg_var_buffer_to_upper_%b_0x4821910 (_ bv0 64)) true))))
 (let ((?x36 (ite (= carg_var_buffer_to_upper_%b_0x4821910 (_ bv0 64)) (_ bv0 64) carg_var_buffer_to_upper_%b_0x4821910)))
 (and (= gep_0x4822c60 ?x36) $x35))))
(assert
 (= var_buffer_to_upper_%used_0x4822ad0 gep_0x4822c60))
(assert
 (= var_buffer_to_upper_%used_0x4822ad0 (_ bv0 64)))
(check-sat)


