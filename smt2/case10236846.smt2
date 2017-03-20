; 
(set-info :status unknown)
(declare-fun carg_var_handler_ctx_free_%hctx_0x75aea00 () (_ BitVec 64))
(declare-fun bitcast_0x75af130 () (_ BitVec 64))
(declare-fun var_handler_ctx_free_%temp_var0_0x75af040 () (_ BitVec 64))
(assert
 (= bitcast_0x75af130 carg_var_handler_ctx_free_%hctx_0x75aea00))
(assert
 (= var_handler_ctx_free_%temp_var0_0x75af040 bitcast_0x75af130))
(assert
 (and (distinct var_handler_ctx_free_%temp_var0_0x75af040 (_ bv0 64)) true))
(check-sat)


