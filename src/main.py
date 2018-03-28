from src.norma_machine import NormaMachine


# TODO separated test functions
def main():
    nm = NormaMachine()  # instantiate the machine

    nm.set_n_to_reg("A", -3)
    nm.set_n_to_reg("B", -2)
    # nm.test_a_lower_than_b_auxc_auxd()
    nm.mult_a_with_b_with_c_and_d()
    print(nm)

    # verificar o pq da falso


# Central point for all the program startup
if __name__ == '__main__':
    main()
