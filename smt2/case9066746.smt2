; 
(set-info :status unknown)
(declare-fun carg_var_chunkqueue_is_empty_%cq_0x4c62290 () (_ BitVec 64))
(declare-fun gep_0x4c62a60 () (_ BitVec 64))
(declare-fun var_chunkqueue_is_empty_%first_0x4c62970 () (_ BitVec 64))
(assert
 (let (($x31 (or (= carg_var_chunkqueue_is_empty_%cq_0x4c62290 (_ bv0 64)) (and (distinct carg_var_chunkqueue_is_empty_%cq_0x4c62290 (_ bv0 64)) true))))
 (let ((?x32 (ite (= carg_var_chunkqueue_is_empty_%cq_0x4c62290 (_ bv0 64)) (_ bv0 64) carg_var_chunkqueue_is_empty_%cq_0x4c62290)))
 (and (= gep_0x4c62a60 ?x32) $x31))))
(assert
 (= var_chunkqueue_is_empty_%first_0x4c62970 gep_0x4c62a60))
(assert
 (= var_chunkqueue_is_empty_%first_0x4c62970 (_ bv0 64)))
(check-sat)


