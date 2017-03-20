; 
(set-info :status unknown)
(declare-fun var_buffer_reset_StMem__0x77b7b70 () (_ BitVec 64))
(declare-fun var_buffer_reset_LdMem_0x48bba40 () (_ BitVec 64))
(declare-fun R0x46b8ca0 () (_ BitVec 1))
(declare-fun |parg_var_buffer_reset_%[S_1].128_0x77b7c70| () (_ BitVec 64))
(declare-fun var_buffer_reset_%temp_var0_0x48bb5f0 () (_ BitVec 64))
(declare-fun iugt_0x48bbde0 () (_ BitVec 1))
(declare-fun var_buffer_reset_%cmp1_0x46b9280 () (_ BitVec 1))
(declare-fun ieq_0x48bade0 () (_ BitVec 1))
(declare-fun var_buffer_reset_%cmp_0x46b9090 () (_ BitVec 1))
(declare-fun carg_var_buffer_reset_%b_0x46b8ba0 () (_ BitVec 64))
(declare-fun var_buffer_reset_StMem_%ptr3_0x48bd660 () (_ BitVec 64))
(declare-fun var_buffer_reset_StMem__0xbee8ae0 () (_ BitVec 64))
(declare-fun var_buffer_reset_LdMem_0xf7faac0 () (_ BitVec 64))
(declare-fun R0x48bb0b0 () (_ BitVec 1))
(declare-fun R0x46b9370 () (_ BitVec 1))
(declare-fun xor_0x46b9550 () (_ BitVec 1))
(declare-fun |parg_var_buffer_reset_%[S_1].0_0xbee8be0| () (_ BitVec 64))
(declare-fun var_buffer_reset_%pseudo_ret_4_0xc2e4da0 () (_ BitVec 64))
(assert
 (let (($x64 (= var_buffer_reset_LdMem_0x48bba40 var_buffer_reset_StMem__0x77b7b70)))
 (or (not (= R0x46b8ca0 (_ bv1 1))) $x64)))
(assert
 (= var_buffer_reset_LdMem_0x48bba40 var_buffer_reset_StMem__0x77b7b70))
(assert
 (= var_buffer_reset_StMem__0x77b7b70 |parg_var_buffer_reset_%[S_1].128_0x77b7c70|))
(assert
 (= var_buffer_reset_%temp_var0_0x48bb5f0 var_buffer_reset_LdMem_0x48bba40))
(assert
 (= iugt_0x48bbde0 (ite (bvugt var_buffer_reset_%temp_var0_0x48bb5f0 (_ bv4096 64)) (_ bv1 1) (_ bv0 1))))
(assert
 (= var_buffer_reset_%cmp1_0x46b9280 iugt_0x48bbde0))
(assert
 (= var_buffer_reset_%cmp_0x46b9090 ieq_0x48bade0))
(assert
 (let (($x36 (= (_ bv0 64) carg_var_buffer_reset_%b_0x46b8ba0)))
 (let ((?x37 (ite $x36 (_ bv1 1) (_ bv0 1))))
 (= ieq_0x48bade0 ?x37))))
(assert
 (= var_buffer_reset_StMem_%ptr3_0x48bd660 (_ bv0 64)))
(assert
 (let (($x71 (= var_buffer_reset_LdMem_0xf7faac0 var_buffer_reset_StMem__0xbee8ae0)))
 (or (not (= R0x48bb0b0 (_ bv1 1))) $x71)))
(assert
 (= R0x48bb0b0 var_buffer_reset_%cmp_0x46b9090))
(assert
 (let (($x80 (= var_buffer_reset_LdMem_0xf7faac0 var_buffer_reset_StMem_%ptr3_0x48bd660)))
 (or (not (= R0x46b9370 (_ bv1 1))) $x80)))
(assert
 (= R0x46b9370 xor_0x46b9550))
(assert
 (let ((?x78 (bvxor var_buffer_reset_%cmp_0x46b9090 (_ bv1 1))))
 (= xor_0x46b9550 ?x78)))
(assert
 (let (($x80 (= var_buffer_reset_LdMem_0xf7faac0 var_buffer_reset_StMem_%ptr3_0x48bd660)))
 (let (($x71 (= var_buffer_reset_LdMem_0xf7faac0 var_buffer_reset_StMem__0xbee8ae0)))
 (or $x71 $x80))))
(assert
 (= var_buffer_reset_StMem__0xbee8ae0 |parg_var_buffer_reset_%[S_1].0_0xbee8be0|))
(assert
 (= var_buffer_reset_%pseudo_ret_4_0xc2e4da0 var_buffer_reset_LdMem_0xf7faac0))
(assert
 (= var_buffer_reset_%pseudo_ret_4_0xc2e4da0 var_buffer_reset_LdMem_0xf7faac0))
(assert
 (and (= var_buffer_reset_%cmp1_0x46b9280 (_ bv1 1)) (not (= var_buffer_reset_%cmp_0x46b9090 (_ bv1 1)))))
(assert
 (= R0x46b9370 (_ bv1 1)))
(assert
 (= var_buffer_reset_%pseudo_ret_4_0xc2e4da0 (_ bv0 64)))
(check-sat)


