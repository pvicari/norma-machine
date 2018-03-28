from src.norma_machine import NormaMachine


# TODO separated test functions
def main():
    nm = NormaMachine()  # instantiate the machine

    nm.set_n_to_reg("A", -4)
    nm.set_n_to_reg("B", -3)
    nm.test_a_lower_than_b_auxc_auxd()
    nm.test_a_lower_eq_than_b_auxc_auxd()
    #nm.mult_a_with_b_with_c_and_d()
    #nm.add_b_to_a_with_c()
    print(nm)

    # verificar o pq da falso


# Central point for all the program startup
if __name__ == '__main__':
    main()
