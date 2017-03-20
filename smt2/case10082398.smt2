; 
(set-info :status unknown)
(declare-fun var_Decode_%j.0_0x713f170 () (_ BitVec 32))
(declare-fun add_0x71437a0 () (_ BitVec 32))
(declare-fun var_Decode_%add4_0x7143610 () (_ BitVec 32))
(declare-fun zext_0x7143b20 () (_ BitVec 64))
(declare-fun var_Decode_%idxprom5_0x7143990 () (_ BitVec 64))
(declare-fun mul_0x7143ce0 () (_ BitVec 64))
(declare-fun var_Decode_node_0x7143e70 () (_ BitVec 64))
(declare-fun carg_var_Decode_%input_0x713e420 () (_ BitVec 64))
(declare-fun add_0x7144020 () (_ BitVec 64))
(declare-fun var_Decode_node_0x7144200 () (_ BitVec 64))
(declare-fun gep_0x7144520 () (_ BitVec 64))
(declare-fun iult_0x713f390 () (_ BitVec 1))
(declare-fun var_Decode_%cmp_0x713e730 () (_ BitVec 1))
(declare-fun carg_var_Decode_%len_0x713e5b0 () (_ BitVec 32))
(declare-fun var_Decode_%arrayidx6_0x7144390 () (_ BitVec 64))
(assert
 (= var_Decode_%j.0_0x713f170 (_ bv0 32)))
(assert
 (= var_Decode_%j.0_0x713f170 (_ bv0 32)))
(assert
 (= add_0x71437a0 (bvadd var_Decode_%j.0_0x713f170 (_ bv2 32))))
(assert
 (= var_Decode_%add4_0x7143610 add_0x71437a0))
(assert
 (= zext_0x7143b20 ((_ zero_extend 32) var_Decode_%add4_0x7143610)))
(assert
 (= var_Decode_%idxprom5_0x7143990 zext_0x7143b20))
(assert
 (let (($x185 (or (or (= var_Decode_%idxprom5_0x7143990 (_ bv0 64)) (= (_ bv8 64) (_ bv0 64))) (and (distinct mul_0x7143ce0 (_ bv0 64)) true))))
 (and (= mul_0x7143ce0 (bvmul var_Decode_%idxprom5_0x7143990 (_ bv8 64))) $x185)))
(assert
 (= var_Decode_node_0x7143e70 mul_0x7143ce0))
(assert
 (let ((?x167 (bvadd carg_var_Decode_%input_0x713e420 var_Decode_node_0x7143e70)))
 (= add_0x7144020 ?x167)))
(assert
 (= var_Decode_node_0x7144200 add_0x7144020))
(assert
 (let (($x93 (= carg_var_Decode_%input_0x713e420 (_ bv0 64))))
 (and (= gep_0x7144520 (ite $x93 (_ bv0 64) var_Decode_node_0x7144200)) (or $x93 (and (distinct var_Decode_node_0x7144200 (_ bv0 64)) true)))))
(assert
 (= var_Decode_%cmp_0x713e730 iult_0x713f390))
(assert
 (let ((?x71 (ite (bvult var_Decode_%j.0_0x713f170 carg_var_Decode_%len_0x713e5b0) (_ bv1 1) (_ bv0 1))))
 (= iult_0x713f390 ?x71)))
(assert
 (= var_Decode_%arrayidx6_0x7144390 gep_0x7144520))
(assert
 (= var_Decode_%cmp_0x713e730 (_ bv1 1)))
(assert
 (= var_Decode_%arrayidx6_0x7144390 (_ bv0 64)))
(check-sat)


