; 
(set-info :status unknown)
(declare-fun var_buffer_caseless_compare_%i.0_0x4705570 () (_ BitVec 64))
(declare-fun mul_0x47069c0 () (_ BitVec 64))
(declare-fun var_buffer_caseless_compare_node_0x4706b50 () (_ BitVec 64))
(declare-fun carg_var_buffer_caseless_compare_%b_0x4700600 () (_ BitVec 64))
(declare-fun add_0x4706d10 () (_ BitVec 64))
(declare-fun var_buffer_caseless_compare_node_0x4706f60 () (_ BitVec 64))
(declare-fun gep_0x47072a0 () (_ BitVec 64))
(declare-fun iult_0x4705280 () (_ BitVec 1))
(declare-fun var_buffer_caseless_compare_%cmp_0x4704d70 () (_ BitVec 1))
(declare-fun carg_var_buffer_caseless_compare_%b_len_0x47007a0 () (_ BitVec 64))
(declare-fun carg_var_buffer_caseless_compare_%a_len_0x4700450 () (_ BitVec 64))
(declare-fun select_0x47050b0 () (_ BitVec 64))
(declare-fun var_buffer_caseless_compare_%a_len.b_len_0x4704f40 () (_ BitVec 64))
(declare-fun iult_0x47058e0 () (_ BitVec 1))
(declare-fun var_buffer_caseless_compare_%cmp1_0x4700bd0 () (_ BitVec 1))
(declare-fun var_buffer_caseless_compare_%arrayidx2_0x4707100 () (_ BitVec 64))
(assert
 (= var_buffer_caseless_compare_%i.0_0x4705570 (_ bv0 64)))
(assert
 (= var_buffer_caseless_compare_%i.0_0x4705570 (_ bv0 64)))
(assert
 (let (($x350 (or (or (= var_buffer_caseless_compare_%i.0_0x4705570 (_ bv0 64)) (= (_ bv8 64) (_ bv0 64))) (and (distinct mul_0x47069c0 (_ bv0 64)) true))))
 (let (($x356 (= mul_0x47069c0 (bvmul var_buffer_caseless_compare_%i.0_0x4705570 (_ bv8 64)))))
 (and $x356 $x350))))
(assert
 (= var_buffer_caseless_compare_node_0x4706b50 mul_0x47069c0))
(assert
 (let ((?x326 (bvadd carg_var_buffer_caseless_compare_%b_0x4700600 var_buffer_caseless_compare_node_0x4706b50)))
 (= add_0x4706d10 ?x326)))
(assert
 (= var_buffer_caseless_compare_node_0x4706f60 add_0x4706d10))
(assert
 (let (($x311 (or (= carg_var_buffer_caseless_compare_%b_0x4700600 (_ bv0 64)) (and (distinct var_buffer_caseless_compare_node_0x4706f60 (_ bv0 64)) true))))
 (let ((?x312 (ite (= carg_var_buffer_caseless_compare_%b_0x4700600 (_ bv0 64)) (_ bv0 64) var_buffer_caseless_compare_node_0x4706f60)))
 (and (= gep_0x47072a0 ?x312) $x311))))
(assert
 (= var_buffer_caseless_compare_%cmp_0x4704d70 iult_0x4705280))
(assert
 (let (($x75 (bvult carg_var_buffer_caseless_compare_%a_len_0x4700450 carg_var_buffer_caseless_compare_%b_len_0x47007a0)))
 (= iult_0x4705280 (ite $x75 (_ bv1 1) (_ bv0 1)))))
(assert
 (let ((?x71 (ite (= var_buffer_caseless_compare_%cmp_0x4704d70 (_ bv1 1)) carg_var_buffer_caseless_compare_%a_len_0x4700450 carg_var_buffer_caseless_compare_%b_len_0x47007a0)))
 (= select_0x47050b0 ?x71)))
(assert
 (= var_buffer_caseless_compare_%a_len.b_len_0x4704f40 select_0x47050b0))
(assert
 (let (($x62 (bvult var_buffer_caseless_compare_%i.0_0x4705570 var_buffer_caseless_compare_%a_len.b_len_0x4704f40)))
 (= iult_0x47058e0 (ite $x62 (_ bv1 1) (_ bv0 1)))))
(assert
 (= var_buffer_caseless_compare_%cmp1_0x4700bd0 iult_0x47058e0))
(assert
 (= var_buffer_caseless_compare_%arrayidx2_0x4707100 gep_0x47072a0))
(assert
 (= var_buffer_caseless_compare_%cmp1_0x4700bd0 (_ bv1 1)))
(assert
 (= var_buffer_caseless_compare_%arrayidx2_0x4707100 (_ bv0 64)))
(check-sat)


