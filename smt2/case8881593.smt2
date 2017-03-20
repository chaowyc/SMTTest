; 
(set-info :status unknown)
(declare-fun var_keyvalue_get_value_StMem__0x11328ec0 () (_ BitVec 64))
(declare-fun var_keyvalue_get_value_LdMem_0x4af1ea0 () (_ BitVec 64))
(declare-fun R0x4aef400 () (_ BitVec 1))
(declare-fun |parg_var_keyvalue_get_value_%[S_1].32_0x11328fc0| () (_ BitVec 64))
(declare-fun var_keyvalue_get_value_%temp_var0_0x4af1ca0 () (_ BitVec 64))
(declare-fun ine_0x4af2280 () (_ BitVec 1))
(declare-fun var_keyvalue_get_value_%tobool_0x4aefac0 () (_ BitVec 1))
(declare-fun var_keyvalue_get_value_StMem__0x113290e0 () (_ BitVec 32))
(declare-fun var_keyvalue_get_value_LdMem_0x4af3930 () (_ BitVec 32))
(declare-fun |parg_var_keyvalue_get_value_%[S_1].0_0x113291e0| () (_ BitVec 32))
(declare-fun var_keyvalue_get_value_%temp_var1_0x4af37c0 () (_ BitVec 32))
(declare-fun carg_var_keyvalue_get_value_%k_0x4aef730 () (_ BitVec 32))
(declare-fun ieq_0x4af3c10 () (_ BitVec 1))
(declare-fun var_keyvalue_get_value_%cmp_0x4aeff40 () (_ BitVec 1))
(declare-fun var_keyvalue_get_value_%temp_var4_0x4af5fa0 () (_ BitVec 64))
(declare-fun ine_0x4af6420 () (_ BitVec 1))
(declare-fun var_keyvalue_get_value_%tobool.ec_0x4af04a0 () (_ BitVec 1))
(declare-fun var_keyvalue_get_value_%temp_var5_0x4af7ad0 () (_ BitVec 32))
(declare-fun ieq_0x4af7f20 () (_ BitVec 1))
(declare-fun var_keyvalue_get_value_%cmp.ec_0x4aefd10 () (_ BitVec 1))
(declare-fun var_keyvalue_get_value_%temp_var3_0x4afa9c0 () (_ BitVec 64))
(declare-fun var_keyvalue_get_value_%retval.0_0x4afb1a0 () (_ BitVec 64))
(declare-fun return_var_keyvalue_get_value_node_0x4aef8c0 () (_ BitVec 64))
(assert
 (let (($x47 (= var_keyvalue_get_value_LdMem_0x4af1ea0 var_keyvalue_get_value_StMem__0x11328ec0)))
 (or (not (= R0x4aef400 (_ bv1 1))) $x47)))
(assert
 (= var_keyvalue_get_value_LdMem_0x4af1ea0 var_keyvalue_get_value_StMem__0x11328ec0))
(assert
 (= var_keyvalue_get_value_StMem__0x11328ec0 |parg_var_keyvalue_get_value_%[S_1].32_0x11328fc0|))
(assert
 (= var_keyvalue_get_value_%temp_var0_0x4af1ca0 var_keyvalue_get_value_LdMem_0x4af1ea0))
(assert
 (let ((?x41 (ite (and (distinct var_keyvalue_get_value_%temp_var0_0x4af1ca0 (_ bv0 64)) true) (_ bv1 1) (_ bv0 1))))
 (= ine_0x4af2280 ?x41)))
(assert
 (= var_keyvalue_get_value_%tobool_0x4aefac0 ine_0x4af2280))
(assert
 (let (($x65 (= var_keyvalue_get_value_LdMem_0x4af3930 var_keyvalue_get_value_StMem__0x113290e0)))
 (or (not (= R0x4aef400 (_ bv1 1))) $x65)))
(assert
 (= var_keyvalue_get_value_LdMem_0x4af3930 var_keyvalue_get_value_StMem__0x113290e0))
(assert
 (= var_keyvalue_get_value_StMem__0x113290e0 |parg_var_keyvalue_get_value_%[S_1].0_0x113291e0|))
(assert
 (= var_keyvalue_get_value_%temp_var1_0x4af37c0 var_keyvalue_get_value_LdMem_0x4af3930))
(assert
 (let (($x59 (= var_keyvalue_get_value_%temp_var1_0x4af37c0 carg_var_keyvalue_get_value_%k_0x4aef730)))
 (let ((?x60 (ite $x59 (_ bv1 1) (_ bv0 1))))
 (= ieq_0x4af3c10 ?x60))))
(assert
 (= var_keyvalue_get_value_%cmp_0x4aeff40 ieq_0x4af3c10))
(assert
 (let ((?x74 (ite (and (distinct var_keyvalue_get_value_%temp_var4_0x4af5fa0 (_ bv0 64)) true) (_ bv1 1) (_ bv0 1))))
 (= ine_0x4af6420 ?x74)))
(assert
 (= var_keyvalue_get_value_%temp_var4_0x4af5fa0 var_keyvalue_get_value_LdMem_0x4af1ea0))
(assert
 (= var_keyvalue_get_value_%tobool.ec_0x4af04a0 ine_0x4af6420))
(assert
 (let (($x83 (= var_keyvalue_get_value_%temp_var5_0x4af7ad0 carg_var_keyvalue_get_value_%k_0x4aef730)))
 (let ((?x84 (ite $x83 (_ bv1 1) (_ bv0 1))))
 (= ieq_0x4af7f20 ?x84))))
(assert
 (= var_keyvalue_get_value_%temp_var5_0x4af7ad0 var_keyvalue_get_value_LdMem_0x4af3930))
(assert
 (= var_keyvalue_get_value_%cmp.ec_0x4aefd10 ieq_0x4af7f20))
(assert
 (let (($x88 (= var_keyvalue_get_value_%retval.0_0x4afb1a0 var_keyvalue_get_value_%temp_var3_0x4afa9c0)))
 (let (($x36 (= var_keyvalue_get_value_%tobool_0x4aefac0 (_ bv1 1))))
 (let (($x54 (and (not (= var_keyvalue_get_value_%cmp_0x4aeff40 (_ bv1 1))) $x36)))
 (let (($x77 (and (= var_keyvalue_get_value_%cmp.ec_0x4aefd10 (_ bv1 1)) (and (= var_keyvalue_get_value_%tobool.ec_0x4af04a0 (_ bv1 1)) $x54))))
 (let (($x89 (not (or $x77 (and (= var_keyvalue_get_value_%cmp_0x4aeff40 (_ bv1 1)) $x36)))))
 (or $x89 $x88)))))))
(assert
 (let (($x36 (= var_keyvalue_get_value_%tobool_0x4aefac0 (_ bv1 1))))
 (let (($x54 (and (not (= var_keyvalue_get_value_%cmp_0x4aeff40 (_ bv1 1))) $x36)))
 (let (($x94 (or (not $x36) (and (not (= var_keyvalue_get_value_%tobool.ec_0x4af04a0 (_ bv1 1))) $x54))))
 (or (not $x94) (= var_keyvalue_get_value_%retval.0_0x4afb1a0 (_ bv0 64)))))))
(assert
 (let (($x88 (= var_keyvalue_get_value_%retval.0_0x4afb1a0 var_keyvalue_get_value_%temp_var3_0x4afa9c0)))
 (or $x88 (= var_keyvalue_get_value_%retval.0_0x4afb1a0 (_ bv0 64)))))
(assert
 (= var_keyvalue_get_value_%temp_var3_0x4afa9c0 var_keyvalue_get_value_LdMem_0x4af1ea0))
(assert
 (let (($x138 (= return_var_keyvalue_get_value_node_0x4aef8c0 var_keyvalue_get_value_%retval.0_0x4afb1a0)))
 (let (($x36 (= var_keyvalue_get_value_%tobool_0x4aefac0 (_ bv1 1))))
 (let (($x54 (and (not (= var_keyvalue_get_value_%cmp_0x4aeff40 (_ bv1 1))) $x36)))
 (let (($x77 (and (= var_keyvalue_get_value_%cmp.ec_0x4aefd10 (_ bv1 1)) (and (= var_keyvalue_get_value_%tobool.ec_0x4af04a0 (_ bv1 1)) $x54))))
 (let (($x137 (or (not $x36) $x77 (and (= var_keyvalue_get_value_%cmp_0x4aeff40 (_ bv1 1)) $x36) (and (not (= var_keyvalue_get_value_%tobool.ec_0x4af04a0 (_ bv1 1))) $x54))))
 (or (not $x137) $x138)))))))
(assert
 (= return_var_keyvalue_get_value_node_0x4aef8c0 var_keyvalue_get_value_%retval.0_0x4afb1a0))
(assert
 (let (($x36 (= var_keyvalue_get_value_%tobool_0x4aefac0 (_ bv1 1))))
 (let (($x54 (and (not (= var_keyvalue_get_value_%cmp_0x4aeff40 (_ bv1 1))) $x36)))
 (or (not $x36) (and (not (= var_keyvalue_get_value_%tobool.ec_0x4af04a0 (_ bv1 1))) $x54)))))
(assert
 (let (($x36 (= var_keyvalue_get_value_%tobool_0x4aefac0 (_ bv1 1))))
 (let (($x54 (and (not (= var_keyvalue_get_value_%cmp_0x4aeff40 (_ bv1 1))) $x36)))
 (let (($x77 (and (= var_keyvalue_get_value_%cmp.ec_0x4aefd10 (_ bv1 1)) (and (= var_keyvalue_get_value_%tobool.ec_0x4af04a0 (_ bv1 1)) $x54))))
 (or (not $x36) $x77 (and (= var_keyvalue_get_value_%cmp_0x4aeff40 (_ bv1 1)) $x36) (and (not (= var_keyvalue_get_value_%tobool.ec_0x4af04a0 (_ bv1 1))) $x54))))))
(assert
 (= return_var_keyvalue_get_value_node_0x4aef8c0 (_ bv0 64)))
(check-sat)


