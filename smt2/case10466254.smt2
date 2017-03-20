; 
(set-info :status unknown)
(declare-fun trunc_0xc917e60 () (_ BitVec 32))
(declare-fun |var_fdevent_event_clr_%[S_3].224_0xb789db0| () (_ BitVec 32))
(declare-fun var_fdevent_event_clr_node_0xc906ff0 () (_ BitVec 64))
(declare-fun var_fdevent_event_clr_StMem__0xb3288d0 () (_ BitVec 32))
(declare-fun var_fdevent_event_clr_LdMem_0x4d383d0 () (_ BitVec 32))
(declare-fun R0x4d34120 () (_ BitVec 1))
(declare-fun var_fdevent_event_clr_%temp_var2_0x4d38230 () (_ BitVec 32))
(declare-fun carg_var_fdevent_event_clr_%event_0x4d34780 () (_ BitVec 32))
(declare-fun and_0x4d38840 () (_ BitVec 32))
(declare-fun var_fdevent_event_clr_%and_0x4d38680 () (_ BitVec 32))
(declare-fun ine_0x4d38b60 () (_ BitVec 1))
(declare-fun var_fdevent_event_clr_%tobool_0x4d34bd0 () (_ BitVec 1))
(declare-fun var_fdevent_event_clr_StMem__0xb139f00 () (_ BitVec 64))
(declare-fun var_fdevent_event_clr_LdMem_0x4d39db0 () (_ BitVec 64))
(declare-fun |parg_var_fdevent_event_clr_%[S_1].7040_0x157f8a50| () (_ BitVec 64))
(declare-fun var_fdevent_event_clr_%temp_var3_0x4d39c10 () (_ BitVec 64))
(declare-fun ine_0x4d3a1d0 () (_ BitVec 1))
(declare-fun var_fdevent_event_clr_%tobool5_0x4d35250 () (_ BitVec 1))
(declare-fun ieq_0x4d35ec0 () (_ BitVec 1))
(declare-fun var_fdevent_event_clr_%cmp_0x4d349e0 () (_ BitVec 1))
(declare-fun carg_var_fdevent_event_clr_%fd_0x4d34600 () (_ BitVec 32))
(declare-fun carg_var_fdevent_event_clr_%fde_ndx_0x4d34460 () (_ BitVec 64))
(assert
 (= |var_fdevent_event_clr_%[S_3].224_0xb789db0| trunc_0xc917e60))
(assert
 (let ((?x79 ((_ extract 31 0) var_fdevent_event_clr_node_0xc906ff0)))
 (= trunc_0xc917e60 ?x79)))
(assert
 (= var_fdevent_event_clr_StMem__0xb3288d0 |var_fdevent_event_clr_%[S_3].224_0xb789db0|))
(assert
 (let (($x97 (= var_fdevent_event_clr_LdMem_0x4d383d0 var_fdevent_event_clr_StMem__0xb3288d0)))
 (or (not (= R0x4d34120 (_ bv1 1))) $x97)))
(assert
 (= var_fdevent_event_clr_LdMem_0x4d383d0 var_fdevent_event_clr_StMem__0xb3288d0))
(assert
 (= var_fdevent_event_clr_%temp_var2_0x4d38230 var_fdevent_event_clr_LdMem_0x4d383d0))
(assert
 (let ((?x64 (bvand var_fdevent_event_clr_%temp_var2_0x4d38230 carg_var_fdevent_event_clr_%event_0x4d34780)))
 (= and_0x4d38840 ?x64)))
(assert
 (= var_fdevent_event_clr_%and_0x4d38680 and_0x4d38840))
(assert
 (= ine_0x4d38b60 (ite (and (distinct var_fdevent_event_clr_%and_0x4d38680 (_ bv0 32)) true) (_ bv1 1) (_ bv0 1))))
(assert
 (= var_fdevent_event_clr_%tobool_0x4d34bd0 ine_0x4d38b60))
(assert
 (let (($x122 (= var_fdevent_event_clr_LdMem_0x4d39db0 var_fdevent_event_clr_StMem__0xb139f00)))
 (or (not (= R0x4d34120 (_ bv1 1))) $x122)))
(assert
 (= var_fdevent_event_clr_LdMem_0x4d39db0 var_fdevent_event_clr_StMem__0xb139f00))
(assert
 (= var_fdevent_event_clr_StMem__0xb139f00 |parg_var_fdevent_event_clr_%[S_1].7040_0x157f8a50|))
(assert
 (= var_fdevent_event_clr_%temp_var3_0x4d39c10 var_fdevent_event_clr_LdMem_0x4d39db0))
(assert
 (let ((?x73 (ite (and (distinct var_fdevent_event_clr_%temp_var3_0x4d39c10 (_ bv0 64)) true) (_ bv1 1) (_ bv0 1))))
 (= ine_0x4d3a1d0 ?x73)))
(assert
 (= var_fdevent_event_clr_%tobool5_0x4d35250 ine_0x4d3a1d0))
(assert
 (= var_fdevent_event_clr_%cmp_0x4d349e0 ieq_0x4d35ec0))
(assert
 (let (($x43 (= (_ bv4294967295 32) carg_var_fdevent_event_clr_%fd_0x4d34600)))
 (let ((?x44 (ite $x43 (_ bv1 1) (_ bv0 1))))
 (= ieq_0x4d35ec0 ?x44))))
(assert
 (let (($x52 (and (= var_fdevent_event_clr_%tobool_0x4d34bd0 (_ bv1 1)) (not (= var_fdevent_event_clr_%cmp_0x4d349e0 (_ bv1 1))))))
 (and (= var_fdevent_event_clr_%tobool5_0x4d35250 (_ bv1 1)) $x52)))
(assert
 (= carg_var_fdevent_event_clr_%fde_ndx_0x4d34460 (_ bv0 64)))
(check-sat)


