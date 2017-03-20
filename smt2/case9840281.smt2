; 
(set-info :status unknown)
(declare-fun carg_var_sock_addr_get_port_%addr_0x7274b90 () (_ BitVec 64))
(declare-fun bitcast_0x7275490 () (_ BitVec 64))
(declare-fun var_sock_addr_get_port_%plain_0x72753a0 () (_ BitVec 64))
(declare-fun gep_0x7275840 () (_ BitVec 64))
(declare-fun var_sock_addr_get_port_%sa_family_0x72756a0 () (_ BitVec 64))
(assert
 (= bitcast_0x7275490 carg_var_sock_addr_get_port_%addr_0x7274b90))
(assert
 (= var_sock_addr_get_port_%plain_0x72753a0 bitcast_0x7275490))
(assert
 (let (($x35 (or (= var_sock_addr_get_port_%plain_0x72753a0 (_ bv0 64)) (and (distinct var_sock_addr_get_port_%plain_0x72753a0 (_ bv0 64)) true))))
 (let ((?x36 (ite (= var_sock_addr_get_port_%plain_0x72753a0 (_ bv0 64)) (_ bv0 64) var_sock_addr_get_port_%plain_0x72753a0)))
 (and (= gep_0x7275840 ?x36) $x35))))
(assert
 (= var_sock_addr_get_port_%sa_family_0x72756a0 gep_0x7275840))
(assert
 (= var_sock_addr_get_port_%sa_family_0x72756a0 (_ bv0 64)))
(check-sat)


