from src.norma_machine import NormaMachine

nm = NormaMachine()

nm.set_n_to_reg("A",1)
nm.is_primal("A")
nm.set_n_to_reg("A",5)
nm.is_primal("A")
nm.set_n_to_reg("A",-1)
nm.set_n_to_reg("A",-4)
nm.set_n_to_reg("A",-2)
nm.set_n_to_reg("A",4)
nm.set_n_to_reg("A",9)
nm.is_primal("A")
nm.set_n_to_reg("A",11)
nm.is_primal("A")


