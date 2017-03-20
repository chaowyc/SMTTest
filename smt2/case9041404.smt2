; 
(set-info :status unknown)
(declare-fun var_keyvalue_get_key_StMem__0x11324840 () (_ BitVec 64))
(declare-fun var_keyvalue_get_key_LdMem_0x4aff3a0 () (_ BitVec 64))
(declare-fun R0x4afc930 () (_ BitVec 1))
(declare-fun |parg_var_keyvalue_get_key_%[S_1].32_0x11324940| () (_ BitVec 64))
(declare-fun var_keyvalue_get_key_%temp_var0_0x4aff1a0 () (_ BitVec 64))
(declare-fun ine_0x4aff770 () (_ BitVec 1))
(declare-fun var_keyvalue_get_key_%tobool_0x4afcfd0 () (_ BitVec 1))
(declare-fun carg_var_keyvalue_get_key_%s_0x4afcc50 () (_ BitVec 64))
(assert
 (let (($x278 (= var_keyvalue_get_key_LdMem_0x4aff3a0 var_keyvalue_get_key_StMem__0x11324840)))
 (or (not (= R0x4afc930 (_ bv1 1))) $x278)))
(assert
 (= var_keyvalue_get_key_LdMem_0x4aff3a0 var_keyvalue_get_key_StMem__0x11324840))
(assert
 (= var_keyvalue_get_key_StMem__0x11324840 |parg_var_keyvalue_get_key_%[S_1].32_0x11324940|))
(assert
 (= var_keyvalue_get_key_%temp_var0_0x4aff1a0 var_keyvalue_get_key_LdMem_0x4aff3a0))
(assert
 (= ine_0x4aff770 (ite (and (distinct var_keyvalue_get_key_%temp_var0_0x4aff1a0 (_ bv0 64)) true) (_ bv1 1) (_ bv0 1))))
(assert
 (= var_keyvalue_get_key_%tobool_0x4afcfd0 ine_0x4aff770))
(assert
 (= var_keyvalue_get_key_%tobool_0x4afcfd0 (_ bv1 1)))
(assert
 (= carg_var_keyvalue_get_key_%s_0x4afcc50 (_ bv0 64)))
(check-sat)


