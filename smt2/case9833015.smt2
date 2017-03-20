; 
(set-info :status unknown)
(declare-fun var_Decode_%j.0_0x713f170 () (_ BitVec 32))
(declare-fun zext_0x713fed0 () (_ BitVec 64))
(declare-fun var_Decode_%idxprom_0x713fd20 () (_ BitVec 64))
(declare-fun mul_0x7140090 () (_ BitVec 64))
(declare-fun var_Decode_node_0x7140220 () (_ BitVec 64))
(declare-fun carg_var_Decode_%input_0x713e420 () (_ BitVec 64))
(declare-fun add_0x71403d0 () (_ BitVec 64))
(declare-fun var_Decode_node_0x71405b0 () (_ BitVec 64))
(declare-fun gep_0x71408d0 () (_ BitVec 64))
(declare-fun iult_0x713f390 () (_ BitVec 1))
(declare-fun var_Decode_%cmp_0x713e730 () (_ BitVec 1))
(declare-fun carg_var_Decode_%len_0x713e5b0 () (_ BitVec 32))
(declare-fun var_Decode_%arrayidx_0x7140740 () (_ BitVec 64))
(assert
 (= var_Decode_%j.0_0x713f170 (_ bv0 32)))
(assert
 (= var_Decode_%j.0_0x713f170 (_ bv0 32)))
(assert
 (= zext_0x713fed0 ((_ zero_extend 32) var_Decode_%j.0_0x713f170)))
(assert
 (= var_Decode_%idxprom_0x713fd20 zext_0x713fed0))
(assert
 (let (($x82 (or (or (= var_Decode_%idxprom_0x713fd20 (_ bv0 64)) (= (_ bv8 64) (_ bv0 64))) (and (distinct mul_0x7140090 (_ bv0 64)) true))))
 (and (= mul_0x7140090 (bvmul var_Decode_%idxprom_0x713fd20 (_ bv8 64))) $x82)))
(assert
 (= var_Decode_node_0x7140220 mul_0x7140090))
(assert
 (let ((?x90 (bvadd carg_var_Decode_%input_0x713e420 var_Decode_node_0x7140220)))
 (= add_0x71403d0 ?x90)))
(assert
 (= var_Decode_node_0x71405b0 add_0x71403d0))
(assert
 (let (($x94 (or (= carg_var_Decode_%input_0x713e420 (_ bv0 64)) (and (distinct var_Decode_node_0x71405b0 (_ bv0 64)) true))))
 (let ((?x95 (ite (= carg_var_Decode_%input_0x713e420 (_ bv0 64)) (_ bv0 64) var_Decode_node_0x71405b0)))
 (and (= gep_0x71408d0 ?x95) $x94))))
(assert
 (= var_Decode_%cmp_0x713e730 iult_0x713f390))
(assert
 (let ((?x71 (ite (bvult var_Decode_%j.0_0x713f170 carg_var_Decode_%len_0x713e5b0) (_ bv1 1) (_ bv0 1))))
 (= iult_0x713f390 ?x71)))
(assert
 (= var_Decode_%arrayidx_0x7140740 gep_0x71408d0))
(assert
 (= var_Decode_%cmp_0x713e730 (_ bv1 1)))
(assert
 (= var_Decode_%arrayidx_0x7140740 (_ bv0 64)))
(check-sat)


