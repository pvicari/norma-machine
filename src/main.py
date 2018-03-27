from src.norma_machine import NormaMachine


# TODO separated test functions
def main():
    nm = NormaMachine()  # instantiate the machine

    nm.set_n_to_reg("A", 1)
    print(nm.is_primal("A"))
    nm.set_n_to_reg("A", 5)
    print(nm.is_primal("A"))
    nm.set_n_to_reg("A", -1)
    nm.set_n_to_reg("A", -4)
    nm.set_n_to_reg("A", -2)
    nm.set_n_to_reg("A", 4)
    nm.set_n_to_reg("A", 9)
    print(nm.is_primal("A"))
    nm.set_n_to_reg("A", 11)
    nm.set_n_to_reg("B", 4)
    print(nm.is_primal("A"))
    print(nm.potential("B", "A"))
    print(nm.factorial("B"))
    nm.set_b_to_a_with_c()


# Central point for all the program startup
if __name__ == '__main__':
    main()
