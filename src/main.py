from src.norma_machine import NormaMachine


def main():
    nm = NormaMachine() # instantiate the machine

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
    print(nm.is_primal("A"))


# Central point for all the program startup
if __name__ == '__main__':
    main()
