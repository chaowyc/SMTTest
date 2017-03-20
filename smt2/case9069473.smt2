; 
(set-info :status unknown)
(declare-fun carg_var_chunkqueue_set_tempdirs_default_%tempdirs_0x4bb6340 () (_ BitVec 64))
(declare-fun var_chunkqueue_set_tempdirs_default_StMem_@chunkqueue_default_tempdirs_0x4bb6c10 () (_ BitVec 64))
(declare-fun var_chunkqueue_set_tempdirs_default_LdMem_0x15922870 () (_ BitVec 64))
(declare-fun R0x4bb6440 () (_ BitVec 1))
(declare-fun var_chunkqueue_set_tempdirs_default_%pseudo_ret_2_0x159226e0 () (_ BitVec 64))
(assert
 (= var_chunkqueue_set_tempdirs_default_StMem_@chunkqueue_default_tempdirs_0x4bb6c10 carg_var_chunkqueue_set_tempdirs_default_%tempdirs_0x4bb6340))
(assert
 (let (($x39 (= var_chunkqueue_set_tempdirs_default_LdMem_0x15922870 var_chunkqueue_set_tempdirs_default_StMem_@chunkqueue_default_tempdirs_0x4bb6c10)))
 (or (not (= R0x4bb6440 (_ bv1 1))) $x39)))
(assert
 (= var_chunkqueue_set_tempdirs_default_LdMem_0x15922870 var_chunkqueue_set_tempdirs_default_StMem_@chunkqueue_default_tempdirs_0x4bb6c10))
(assert
 (= var_chunkqueue_set_tempdirs_default_%pseudo_ret_2_0x159226e0 var_chunkqueue_set_tempdirs_default_LdMem_0x15922870))
(assert
 (= var_chunkqueue_set_tempdirs_default_%pseudo_ret_2_0x159226e0 var_chunkqueue_set_tempdirs_default_LdMem_0x15922870))
(assert
 (= R0x4bb6440 (_ bv1 1)))
(assert
 (and (distinct var_chunkqueue_set_tempdirs_default_%pseudo_ret_2_0x159226e0 (_ bv0 64)) true))
(check-sat)


