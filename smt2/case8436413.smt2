; 
(set-info :status unknown)
(declare-fun ieq_0x2391870 () (_ BitVec 1))
(declare-fun var_buffer_free_%cmp_0x2391510 () (_ BitVec 1))
(declare-fun carg_var_buffer_free_%b_0x2391090 () (_ BitVec 64))
(declare-fun bitcast_0x46b8400 () (_ BitVec 64))
(declare-fun var_buffer_free_%temp_var1_0x46b8240 () (_ BitVec 64))
(assert
 (= var_buffer_free_%cmp_0x2391510 ieq_0x2391870))
(assert
 (let (($x34 (= (_ bv0 64) carg_var_buffer_free_%b_0x2391090)))
 (let ((?x35 (ite $x34 (_ bv1 1) (_ bv0 1))))
 (= ieq_0x2391870 ?x35))))
(assert
 (= bitcast_0x46b8400 carg_var_buffer_free_%b_0x2391090))
(assert
 (= var_buffer_free_%temp_var1_0x46b8240 bitcast_0x46b8400))
(assert
 (not (= var_buffer_free_%cmp_0x2391510 (_ bv1 1))))
(assert
 (and (distinct var_buffer_free_%temp_var1_0x46b8240 (_ bv0 64)) true))
(check-sat)


