; 
(set-info :status unknown)
(declare-fun var_stream_close_StMem_%start7_0x4cbe3a0 () (_ BitVec 64))
(declare-fun var_stream_close_LdMem_0x1346a760 () (_ BitVec 64))
(declare-fun R0x4cb8270 () (_ BitVec 1))
(declare-fun var_stream_close_%pseudo_ret_2_0xcf1f1a0 () (_ BitVec 64))
(assert
 (= var_stream_close_StMem_%start7_0x4cbe3a0 (_ bv0 64)))
(assert
 (let (($x63 (= var_stream_close_LdMem_0x1346a760 var_stream_close_StMem_%start7_0x4cbe3a0)))
 (or (not (= R0x4cb8270 (_ bv1 1))) $x63)))
(assert
 (= var_stream_close_LdMem_0x1346a760 var_stream_close_StMem_%start7_0x4cbe3a0))
(assert
 (= var_stream_close_%pseudo_ret_2_0xcf1f1a0 var_stream_close_LdMem_0x1346a760))
(assert
 (= var_stream_close_%pseudo_ret_2_0xcf1f1a0 var_stream_close_LdMem_0x1346a760))
(assert
 (= R0x4cb8270 (_ bv1 1)))
(assert
 (= var_stream_close_%pseudo_ret_2_0xcf1f1a0 (_ bv0 64)))
(check-sat)


