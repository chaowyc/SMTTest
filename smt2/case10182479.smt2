; 
(set-info :status unknown)
(declare-fun var_Decode_%j.0_0x713f170 () (_ BitVec 32))
(declare-fun add_0x7145960 () (_ BitVec 32))
(declare-fun var_Decode_%add10_0x71457d0 () (_ BitVec 32))
(declare-fun zext_0x7145ce0 () (_ BitVec 64))
(declare-fun var_Decode_%idxprom11_0x7145b50 () (_ BitVec 64))
(declare-fun mul_0x7145ea0 () (_ BitVec 64))
(declare-fun var_Decode_node_0x7146030 () (_ BitVec 64))
(declare-fun carg_var_Decode_%input_0x713e420 () (_ BitVec 64))
(declare-fun add_0x71461e0 () (_ BitVec 64))
(declare-fun var_Decode_node_0x71463c0 () (_ BitVec 64))
(declare-fun gep_0x71466e0 () (_ BitVec 64))
(declare-fun iult_0x713f390 () (_ BitVec 1))
(declare-fun var_Decode_%cmp_0x713e730 () (_ BitVec 1))
(declare-fun carg_var_Decode_%len_0x713e5b0 () (_ BitVec 32))
(declare-fun var_Decode_%arrayidx12_0x7146550 () (_ BitVec 64))
(assert
 (= var_Decode_%j.0_0x713f170 (_ bv0 32)))
(assert
 (= var_Decode_%j.0_0x713f170 (_ bv0 32)))
(assert
 (= add_0x7145960 (bvadd var_Decode_%j.0_0x713f170 (_ bv3 32))))
(assert
 (= var_Decode_%add10_0x71457d0 add_0x7145960))
(assert
 (= zext_0x7145ce0 ((_ zero_extend 32) var_Decode_%add10_0x71457d0)))
(assert
 (= var_Decode_%idxprom11_0x7145b50 zext_0x7145ce0))
(assert
 (let (($x232 (or (or (= var_Decode_%idxprom11_0x7145b50 (_ bv0 64)) (= (_ bv8 64) (_ bv0 64))) (and (distinct mul_0x7145ea0 (_ bv0 64)) true))))
 (and (= mul_0x7145ea0 (bvmul var_Decode_%idxprom11_0x7145b50 (_ bv8 64))) $x232)))
(assert
 (= var_Decode_node_0x7146030 mul_0x7145ea0))
(assert
 (let ((?x205 (bvadd carg_var_Decode_%input_0x713e420 var_Decode_node_0x7146030)))
 (= add_0x71461e0 ?x205)))
(assert
 (= var_Decode_node_0x71463c0 add_0x71461e0))
(assert
 (let (($x93 (= carg_var_Decode_%input_0x713e420 (_ bv0 64))))
 (and (= gep_0x71466e0 (ite $x93 (_ bv0 64) var_Decode_node_0x71463c0)) (or $x93 (and (distinct var_Decode_node_0x71463c0 (_ bv0 64)) true)))))
(assert
 (= var_Decode_%cmp_0x713e730 iult_0x713f390))
(assert
 (let ((?x71 (ite (bvult var_Decode_%j.0_0x713f170 carg_var_Decode_%len_0x713e5b0) (_ bv1 1) (_ bv0 1))))
 (= iult_0x713f390 ?x71)))
(assert
 (= var_Decode_%arrayidx12_0x7146550 gep_0x71466e0))
(assert
 (= var_Decode_%cmp_0x713e730 (_ bv1 1)))
(assert
 (= var_Decode_%arrayidx12_0x7146550 (_ bv0 64)))
(check-sat)


