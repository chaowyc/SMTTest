; 
(set-info :status unknown)
(declare-fun var_vector_config_weak_init_StMem_%data_0x6e283d0 () (_ BitVec 64))
(declare-fun var_vector_config_weak_init_LdMem_0x80c0cd0 () (_ BitVec 64))
(declare-fun R0x6e27bb0 () (_ BitVec 1))
(declare-fun var_vector_config_weak_init_%pseudo_ret_3_0x7f82dc0 () (_ BitVec 64))
(assert
 (= var_vector_config_weak_init_StMem_%data_0x6e283d0 (_ bv0 64)))
(assert
 (let (($x33 (= var_vector_config_weak_init_LdMem_0x80c0cd0 var_vector_config_weak_init_StMem_%data_0x6e283d0)))
 (or (not (= R0x6e27bb0 (_ bv1 1))) $x33)))
(assert
 (= var_vector_config_weak_init_LdMem_0x80c0cd0 var_vector_config_weak_init_StMem_%data_0x6e283d0))
(assert
 (= var_vector_config_weak_init_%pseudo_ret_3_0x7f82dc0 var_vector_config_weak_init_LdMem_0x80c0cd0))
(assert
 (= var_vector_config_weak_init_%pseudo_ret_3_0x7f82dc0 var_vector_config_weak_init_LdMem_0x80c0cd0))
(assert
 (= R0x6e27bb0 (_ bv1 1)))
(assert
 (= var_vector_config_weak_init_%pseudo_ret_3_0x7f82dc0 (_ bv0 64)))
(check-sat)


