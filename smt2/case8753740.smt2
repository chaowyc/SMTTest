; 
(set-info :status unknown)
(declare-fun carg_var_buffer_to_lower_%b_0x4817d20 () (_ BitVec 64))
(declare-fun gep_0x4819400 () (_ BitVec 64))
(declare-fun var_buffer_to_lower_%used_0x4819270 () (_ BitVec 64))
(assert
 (let (($x35 (or (= carg_var_buffer_to_lower_%b_0x4817d20 (_ bv0 64)) (and (distinct carg_var_buffer_to_lower_%b_0x4817d20 (_ bv0 64)) true))))
 (let ((?x36 (ite (= carg_var_buffer_to_lower_%b_0x4817d20 (_ bv0 64)) (_ bv0 64) carg_var_buffer_to_lower_%b_0x4817d20)))
 (and (= gep_0x4819400 ?x36) $x35))))
(assert
 (= var_buffer_to_lower_%used_0x4819270 gep_0x4819400))
(assert
 (= var_buffer_to_lower_%used_0x4819270 (_ bv0 64)))
(check-sat)


