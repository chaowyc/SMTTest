; 
(set-info :status unknown)
(declare-fun var_Decode_%j.0_0x713f170 () (_ BitVec 32))
(declare-fun add_0x7140ce0 () (_ BitVec 32))
(declare-fun var_Decode_%add_0x7140bb0 () (_ BitVec 32))
(declare-fun zext_0x7141040 () (_ BitVec 64))
(declare-fun var_Decode_%idxprom1_0x7140eb0 () (_ BitVec 64))
(declare-fun mul_0x7141200 () (_ BitVec 64))
(declare-fun var_Decode_node_0x7141390 () (_ BitVec 64))
(declare-fun carg_var_Decode_%input_0x713e420 () (_ BitVec 64))
(declare-fun add_0x7141540 () (_ BitVec 64))
(declare-fun var_Decode_node_0x7141720 () (_ BitVec 64))
(declare-fun gep_0x7141a40 () (_ BitVec 64))
(declare-fun iult_0x713f390 () (_ BitVec 1))
(declare-fun var_Decode_%cmp_0x713e730 () (_ BitVec 1))
(declare-fun carg_var_Decode_%len_0x713e5b0 () (_ BitVec 32))
(declare-fun var_Decode_%arrayidx2_0x71418b0 () (_ BitVec 64))
(assert
 (= var_Decode_%j.0_0x713f170 (_ bv0 32)))
(assert
 (= var_Decode_%j.0_0x713f170 (_ bv0 32)))
(assert
 (= add_0x7140ce0 (bvadd var_Decode_%j.0_0x713f170 (_ bv1 32))))
(assert
 (= var_Decode_%add_0x7140bb0 add_0x7140ce0))
(assert
 (= zext_0x7141040 ((_ zero_extend 32) var_Decode_%add_0x7140bb0)))
(assert
 (= var_Decode_%idxprom1_0x7140eb0 zext_0x7141040))
(assert
 (let (($x139 (or (or (= var_Decode_%idxprom1_0x7140eb0 (_ bv0 64)) (= (_ bv8 64) (_ bv0 64))) (and (distinct mul_0x7141200 (_ bv0 64)) true))))
 (and (= mul_0x7141200 (bvmul var_Decode_%idxprom1_0x7140eb0 (_ bv8 64))) $x139)))
(assert
 (= var_Decode_node_0x7141390 mul_0x7141200))
(assert
 (let ((?x127 (bvadd carg_var_Decode_%input_0x713e420 var_Decode_node_0x7141390)))
 (= add_0x7141540 ?x127)))
(assert
 (= var_Decode_node_0x7141720 add_0x7141540))
(assert
 (let (($x93 (= carg_var_Decode_%input_0x713e420 (_ bv0 64))))
 (and (= gep_0x7141a40 (ite $x93 (_ bv0 64) var_Decode_node_0x7141720)) (or $x93 (and (distinct var_Decode_node_0x7141720 (_ bv0 64)) true)))))
(assert
 (= var_Decode_%cmp_0x713e730 iult_0x713f390))
(assert
 (let ((?x71 (ite (bvult var_Decode_%j.0_0x713f170 carg_var_Decode_%len_0x713e5b0) (_ bv1 1) (_ bv0 1))))
 (= iult_0x713f390 ?x71)))
(assert
 (= var_Decode_%arrayidx2_0x71418b0 gep_0x7141a40))
(assert
 (= var_Decode_%cmp_0x713e730 (_ bv1 1)))
(assert
 (= var_Decode_%arrayidx2_0x71418b0 (_ bv0 64)))
(check-sat)


