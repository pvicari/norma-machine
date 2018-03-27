class NormaMachine:

    def __init__(self):
        self.registers = dict(
            A={"signal": 0, "magnitude": 0},
            B={"signal": 0, "magnitude": 0},
            C={"signal": 0, "magnitude": 0},
            D={"signal": 0, "magnitude": 0},
        )

    def __str__(self):
        msg = ""
        msg += "A: ({},{}) | ".format(self.registers["A"]["signal"], self.registers["A"]["magnitude"])
        msg += "B: ({},{}) | ".format(self.registers["B"]["signal"], self.registers["B"]["magnitude"])
        msg += "C: ({},{}) | ".format(self.registers["C"]["signal"], self.registers["C"]["magnitude"])
        msg += "D: ({},{})".format(self.registers["D"]["signal"], self.registers["D"]["magnitude"])
        return msg

    def change_signal(self, reg):
        pass

    def set_0_to_reg(self, reg):
        while True:
            if self.registers[reg]["magnitude"] == 0:
                self.registers[reg]["signal"] = 0
                break
            else:
                self.registers[reg]["magnitude"] = self.registers[reg]["magnitude"] - 1
                if self.registers[reg]["magnitude"] == 0:
                    self.registers[reg]["signal"] = 0
                print(self)

    def set_n_to_reg(self, reg, n):
        self.set_0_to_reg(reg)
        cont = abs(n)
        if n < 0: self.registers[reg]["signal"] = 1
        while True:
            if cont == 0:
                break
            else:
                self.registers[reg]["magnitude"] = self.registers[reg]["magnitude"] + 1
                cont -= 1
                print(self)

    def add_b_to_a(self, reg_b, reg_a):
        while True:
            if self.registers[reg_b]["magnitude"] == 0:
                break

            else:  # se b diferente de 0
                self.registers[reg_b]["magnitude"] = self.registers[reg_b]["magnitude"] - 1  # decrementa b
                if self.registers[reg_b]["signal"] == 0:  # b positivo

                    if self.registers[reg_a]["signal"] == 0:  # a positivo
                        self.registers[reg_a]["magnitude"] = self.registers[reg_a]["magnitude"] + 1


                    else:  # a negativo
                        self.registers[reg_a]["magnitude"] = self.registers[reg_a]["magnitude"] - 1
                        if self.registers[reg_a]["magnitude"] == 0:  # o a passa de negativo para positivo
                            self.registers[reg_a]["signal"] = 0



                else:  # b negativo

                    if self.registers[reg_a]["signal"] == 0:  # a positivo
                        if self.registers[reg_a][
                            "magnitude"] == 0:  # o a vai passar de positivo para negativo e vai passar a somar
                            self.registers[reg_a]["signal"] = 1
                            self.registers[reg_a]["magnitude"] = self.registers[reg_a]["magnitude"] + 1
                        else:
                            self.registers[reg_a]["magnitude"] = self.registers[reg_a]["magnitude"] - 1

                    else:  # a negativo
                        self.registers[reg_a]["magnitude"] = self.registers[reg_a]["magnitude"] + 1

                if self.registers[reg_b]["magnitude"] == 0:  # muda sinal de b se ele chegar a 0
                    self.registers[reg_b]["signal"] = 0
                print(self)

    def add_b_to_a_with_c(self, reg_b, reg_a, reg_c):
        self.set_0_to_reg(reg_c)
        self.registers[reg_c]["signal"] = self.registers[reg_b]["signal"]
        while True:
            if self.registers[reg_b]["magnitude"] == 0:
                break

            else:  # se b diferente de 0

                self.registers[reg_b]["magnitude"] = self.registers[reg_b]["magnitude"] - 1  # decrementa b
                self.registers[reg_c]["magnitude"] = self.registers[reg_c]["magnitude"] + 1  # incrementa c
                if self.registers[reg_b]["signal"] == 0:  # b positivo

                    if self.registers[reg_a]["signal"] == 0:  # a positivo
                        self.registers[reg_a]["magnitude"] = self.registers[reg_a]["magnitude"] + 1


                    else:  # a negativo
                        self.registers[reg_a]["magnitude"] = self.registers[reg_a]["magnitude"] - 1
                        if self.registers[reg_a]["magnitude"] == 0:  # o a passa de negativo para positivo
                            self.registers[reg_a]["signal"] = 0



                else:  # b negativo

                    if self.registers[reg_a]["signal"] == 0:  # a positivo
                        if self.registers[reg_a][
                            "magnitude"] == 0:  # o a vai passar de positivo para negativo e vai passar a somar
                            self.registers[reg_a]["signal"] = 1
                            self.registers[reg_a]["magnitude"] = self.registers[reg_a]["magnitude"] + 1
                        else:
                            self.registers[reg_a]["magnitude"] = self.registers[reg_a]["magnitude"] - 1

                    else:  # a negativo
                        self.registers[reg_a]["magnitude"] = self.registers[reg_a]["magnitude"] + 1

                if self.registers[reg_b]["magnitude"] == 0:  # muda sinal de b se ele chegar a 0
                    self.registers[reg_b]["signal"] = 0
                print(self)
        self.add_b_to_a(reg_c, reg_b)

    def set_b_to_a_with_c(self, reg_b, reg_a, reg_c):
        self.set_0_to_reg(reg_a)
        self.add_b_to_a_with_c(reg_b, reg_a, reg_c)

    def mult_a_with_b_with_c_and_d(self,reg_a,reg_b,reg_c,reg_d):
        self.set_0_to_reg(reg_c)
        self.add_b_to_a(reg_a,reg_c)
        while True:
            if self.registers[reg_c]["magnitude"] == 0:
                break
            else:
                self.add_b_to_a_with_c(reg_b,reg_a,reg_d)
                self.registers[reg_c]["magnitude"] = self.registers[reg_c]["magnitude"] -1
                if self.registers[reg_c]["magnitude"] == 0:
                    self.registers[reg_c]["signal"] = 0
                print(self)

    def test_a_lower_eq_than_b_auxc_auxd(self,reg_a="A",reg_b="B",reg_c="C",reg_d="D"):
        if self.registers[reg_a]["signal"] == 0:
            if self.registers[reg_b]["signal"] == 0:
                pass
            else:
                print(False)
                return
        else:
            if self.registers[reg_b]["signal"] == 0:
                print(True)
                return

        while True:
            if self.registers[reg_a]["magnitude"] == 0:
                if self.registers[reg_b]["magnitude"] == 0:
                    print(True)
                else:
                    if self.registers[reg_b]["signal"] == 0:
                        print(True)
                    else:
                        print(False)
                break
            if self.registers[reg_b]["magnitude"] == 0:
                print(False)
                break

            self.registers[reg_a]["magnitude"] = self.registers[reg_a]["magnitude"] - 1
            self.registers[reg_c]["magnitude"] = self.registers[reg_c]["magnitude"] + 1
            self.registers[reg_b]["magnitude"] = self.registers[reg_b]["magnitude"] - 1
            self.registers[reg_d]["magnitude"] = self.registers[reg_d]["magnitude"] + 1

        while True:
            if self.registers[reg_c]["magnitude"] == 0:
                break
            if self.registers[reg_d]["magnitude"] == 0:
                break
            self.registers[reg_a]["magnitude"] = self.registers[reg_a]["magnitude"] + 1
            self.registers[reg_c]["magnitude"] = self.registers[reg_c]["magnitude"] - 1
            self.registers[reg_b]["magnitude"] = self.registers[reg_b]["magnitude"] + 1
            self.registers[reg_d]["magnitude"] = self.registers[reg_d]["magnitude"] - 1

    def test_a_lower_than_b_auxc_auxd(self,reg_a="A",reg_b="B",reg_c="C",reg_d="D"):
        if self.registers[reg_a]["signal"] == 0:
            if self.registers[reg_b]["signal"] == 0:
                pass
            else:
                print(False)
                return
        else:
            if self.registers[reg_b]["signal"] == 0:
                print(True)
                return

        while True:
            if self.registers[reg_a]["magnitude"] == 0:
                if self.registers[reg_b]["magnitude"] == 0:
                    print(False)
                else:
                    if self.registers[reg_b]["signal"] == 0:
                        print(True)
                    else:
                        print(False)
                break
            if self.registers[reg_b]["magnitude"] == 0:
                print(False)
                break

            self.registers[reg_a]["magnitude"] = self.registers[reg_a]["magnitude"] - 1
            self.registers[reg_c]["magnitude"] = self.registers[reg_c]["magnitude"] + 1
            self.registers[reg_b]["magnitude"] = self.registers[reg_b]["magnitude"] - 1
            self.registers[reg_d]["magnitude"] = self.registers[reg_d]["magnitude"] + 1

        while True:
            if self.registers[reg_c]["magnitude"] == 0:
                break
            if self.registers[reg_d]["magnitude"] == 0:
                break
            self.registers[reg_a]["magnitude"] = self.registers[reg_a]["magnitude"] + 1
            self.registers[reg_c]["magnitude"] = self.registers[reg_c]["magnitude"] - 1
            self.registers[reg_b]["magnitude"] = self.registers[reg_b]["magnitude"] + 1
            self.registers[reg_d]["magnitude"] = self.registers[reg_d]["magnitude"] - 1