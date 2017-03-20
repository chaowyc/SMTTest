; 
(set-info :status unknown)
(declare-fun var_chunkqueue_append_chunkqueue_StMem__0x830fed0 () (_ BitVec 64))
(declare-fun var_chunkqueue_append_chunkqueue_LdMem_0x4b87080 () (_ BitVec 64))
(declare-fun R0x4b84500 () (_ BitVec 1))
(declare-fun |parg_var_chunkqueue_append_chunkqueue_%[S_1].0_0xa6ce540| () (_ BitVec 64))
(declare-fun var_chunkqueue_append_chunkqueue_%temp_var0_0x4b86e50 () (_ BitVec 64))
(declare-fun ieq_0x4b87470 () (_ BitVec 1))
(declare-fun var_chunkqueue_append_chunkqueue_%cmp1_0x4b84fd0 () (_ BitVec 1))
(declare-fun ieq_0x4b864e0 () (_ BitVec 1))
(declare-fun var_chunkqueue_append_chunkqueue_%cmp_0x4b84de0 () (_ BitVec 1))
(declare-fun carg_var_chunkqueue_append_chunkqueue_%src_0x4b84c30 () (_ BitVec 64))
(declare-fun var_chunkqueue_append_chunkqueue_StMem_%last13_0x4b8ed10 () (_ BitVec 64))
(declare-fun xor_0x4b85320 () (_ BitVec 1))
(declare-fun R0x4b850c0 () (_ BitVec 1))
(declare-fun R0x4b85800 () (_ BitVec 1))
(declare-fun and_0x4b85f40 () (_ BitVec 1))
(declare-fun xor_0x4b85a30 () (_ BitVec 1))
(declare-fun R0x4b85c50 () (_ BitVec 1))
(declare-fun xor_0xc32a300 () (_ BitVec 1))
(declare-fun R0xc32a150 () (_ BitVec 1))
(declare-fun var_chunkqueue_append_chunkqueue_StMem__0xa71b900 () (_ BitVec 64))
(declare-fun var_chunkqueue_append_chunkqueue_LdMem_0x112e4960 () (_ BitVec 64))
(declare-fun |parg_var_chunkqueue_append_chunkqueue_%[S_1].64_0xa6ec030| () (_ BitVec 64))
(declare-fun var_chunkqueue_append_chunkqueue_%pseudo_ret_5_0x112e47d0 () (_ BitVec 64))
(assert
 (let (($x53 (= var_chunkqueue_append_chunkqueue_LdMem_0x4b87080 var_chunkqueue_append_chunkqueue_StMem__0x830fed0)))
 (or (not (= R0x4b84500 (_ bv1 1))) $x53)))
(assert
 (= var_chunkqueue_append_chunkqueue_LdMem_0x4b87080 var_chunkqueue_append_chunkqueue_StMem__0x830fed0))
(assert
 (= var_chunkqueue_append_chunkqueue_StMem__0x830fed0 |parg_var_chunkqueue_append_chunkqueue_%[S_1].0_0xa6ce540|))
(assert
 (= var_chunkqueue_append_chunkqueue_%temp_var0_0x4b86e50 var_chunkqueue_append_chunkqueue_LdMem_0x4b87080))
(assert
 (let (($x46 (= (_ bv0 64) var_chunkqueue_append_chunkqueue_%temp_var0_0x4b86e50)))
 (let ((?x47 (ite $x46 (_ bv1 1) (_ bv0 1))))
 (= ieq_0x4b87470 ?x47))))
(assert
 (= var_chunkqueue_append_chunkqueue_%cmp1_0x4b84fd0 ieq_0x4b87470))
(assert
 (= var_chunkqueue_append_chunkqueue_%cmp_0x4b84de0 ieq_0x4b864e0))
(assert
 (let ((?x39 (ite (= carg_var_chunkqueue_append_chunkqueue_%src_0x4b84c30 (_ bv0 64)) (_ bv1 1) (_ bv0 1))))
 (= ieq_0x4b864e0 ?x39)))
(assert
 (= var_chunkqueue_append_chunkqueue_StMem_%last13_0x4b8ed10 (_ bv0 64)))
(assert
 (= R0x4b850c0 xor_0x4b85320))
(assert
 (let ((?x81 (bvxor var_chunkqueue_append_chunkqueue_%cmp_0x4b84de0 (_ bv1 1))))
 (= xor_0x4b85320 ?x81)))
(assert
 (let ((?x77 (bvand R0x4b850c0 R0x4b85800)))
 (= and_0x4b85f40 ?x77)))
(assert
 (= R0x4b85800 xor_0x4b85a30))
(assert
 (let ((?x85 (bvxor var_chunkqueue_append_chunkqueue_%cmp1_0x4b84fd0 (_ bv1 1))))
 (= xor_0x4b85a30 ?x85)))
(assert
 (= R0x4b85c50 and_0x4b85f40))
(assert
 (let ((?x71 (bvxor R0x4b85c50 (_ bv1 1))))
 (= xor_0xc32a300 ?x71)))
(assert
 (= R0xc32a150 xor_0xc32a300))
(assert
 (let (($x110 (= var_chunkqueue_append_chunkqueue_LdMem_0x112e4960 var_chunkqueue_append_chunkqueue_StMem__0xa71b900)))
 (or (not (= R0xc32a150 (_ bv1 1))) $x110)))
(assert
 (let (($x112 (= var_chunkqueue_append_chunkqueue_LdMem_0x112e4960 var_chunkqueue_append_chunkqueue_StMem_%last13_0x4b8ed10)))
 (or (not (= R0x4b85c50 (_ bv1 1))) $x112)))
(assert
 (let (($x112 (= var_chunkqueue_append_chunkqueue_LdMem_0x112e4960 var_chunkqueue_append_chunkqueue_StMem_%last13_0x4b8ed10)))
 (let (($x110 (= var_chunkqueue_append_chunkqueue_LdMem_0x112e4960 var_chunkqueue_append_chunkqueue_StMem__0xa71b900)))
 (or $x110 $x112))))
(assert
 (= var_chunkqueue_append_chunkqueue_StMem__0xa71b900 |parg_var_chunkqueue_append_chunkqueue_%[S_1].64_0xa6ec030|))
(assert
 (= var_chunkqueue_append_chunkqueue_%pseudo_ret_5_0x112e47d0 var_chunkqueue_append_chunkqueue_LdMem_0x112e4960))
(assert
 (= var_chunkqueue_append_chunkqueue_%pseudo_ret_5_0x112e47d0 var_chunkqueue_append_chunkqueue_LdMem_0x112e4960))
(assert
 (and (not (= var_chunkqueue_append_chunkqueue_%cmp1_0x4b84fd0 (_ bv1 1))) (not (= var_chunkqueue_append_chunkqueue_%cmp_0x4b84de0 (_ bv1 1)))))
(assert
 (= R0x4b85c50 (_ bv1 1)))
(assert
 (= var_chunkqueue_append_chunkqueue_%pseudo_ret_5_0x112e47d0 (_ bv0 64)))
(check-sat)


