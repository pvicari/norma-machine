import copy


class NormaMachine:

    def __init__(self):
        self.registers = dict(
            A={"signal": 0, "magnitude": 0},
            B={"signal": 0, "magnitude": 0},
            C={"signal": 0, "magnitude": 0},
            D={"signal": 0, "magnitude": 0},
            E={"signal": 0, "magnitude": 0},
            F={"signal": 0, "magnitude": 0},
        )
        self.stack = []
        self.stack_pointer = -1  # pilha vazia

        self.response = []  # resposta (history) das ações

    def __str__(self):
        msg = ""
        for reg in self.registers:
            msg += "{}: ({},{}) | ".format(reg, self.registers[reg]["signal"], self.registers[reg]["magnitude"])
        msg += "Stack: {} | Stack Pointer: {}".format(self.stack, self.stack_pointer)
        return msg

    def clear_response(self):
        self.response = []

    def append_to_response(self):
        log_entry = {
            'registers': copy.deepcopy(self.registers),
            'stack': copy.deepcopy(self.stack),
            'stack_pointer': copy.deepcopy(self.stack_pointer)
        }

        self.response.append(log_entry)

    # TODO implement change of signal as a function
    def change_signal(self, reg):
        pass

    def get_reg_magnitude(self, reg):
        return self.registers[reg]["magnitude"]

    def get_reg_signal(self, reg):
        return self.registers[reg]["signal"]

    def reset_machine(self):
        for reg in self.registers:
            self.set_0_to_reg(reg)
        self.stack = []
        self.stack_pointer = -1
        return self.response

    def push_to_stack(self, value):
        print("Pushing {} to the stack".format(value))
        self.stack.append(value)
        self.stack_pointer += 1
        self.append_to_response()
        return self.response

    def pop_from_stack(self, reg="A"):
        """
        Pops the stack.
        A chosen register ca be passed as the target for the popped value
        :param reg: (optional, default "A") the register where the popped
                    value will be stored
        :return: None
        """
        print("Popping the stack".format(reg))
        msg = ''
        if len(self.stack) == 0:
            msg += "Stack is empty"
            self.stack_pointer = -1
        else:
            val = self.stack.pop()
            self.stack_pointer -= 1
            self.set_n_to_reg(reg, val)
            if len(self.stack) == 0:
                msg += "Stack is now empty"
                self.stack_pointer = -1
        self.append_to_response()
        return self.response, msg

    def set_0_to_reg(self, reg):
        print("{}:= 0".format(reg))
        self.append_to_response()
        while True:
            if self.get_reg_magnitude(reg) == 0:
                break
            else:
                self.registers[reg]["magnitude"] = self.registers[reg]["magnitude"] - 1
                if self.get_reg_magnitude(reg) == 0:
                    self.registers[reg]["signal"] = 0
                self.append_to_response()
                # print(self)
        return self.response

    def set_n_to_reg(self, reg, n):
        print("{}:= {}".format(reg, n))
        self.append_to_response()
        self.set_0_to_reg(reg)
        cont = abs(n)
        if n < 0:
            self.registers[reg]["signal"] = 1
        while True:
            if cont == 0:
                break
            else:
                self.registers[reg]["magnitude"] = self.registers[reg]["magnitude"] + 1
                cont -= 1
                self.append_to_response()
                # print(self)
        return self.response

    def add_b_to_a(self, reg_b="B", reg_a="A"):
        print("{0}:={0} + {1}".format(reg_a, reg_b))
        self.append_to_response()
        while True:
            if self.get_reg_magnitude(reg_b) == 0:
                break

            else:  # se b diferente de 0
                self.registers[reg_b]["magnitude"] = self.registers[reg_b]["magnitude"] - 1  # decrementa b
                if self.get_reg_signal(reg_b) == 0:  # b positivo

                    if self.get_reg_signal(reg_a) == 0:  # a positivo
                        self.registers[reg_a]["magnitude"] = self.registers[reg_a]["magnitude"] + 1


                    else:  # a negativo
                        self.registers[reg_a]["magnitude"] = self.registers[reg_a]["magnitude"] - 1
                        if self.get_reg_magnitude(reg_a) == 0:  # o a passa de negativo para positivo
                            self.registers[reg_a]["signal"] = 0



                else:  # b negativo

                    if self.get_reg_signal(reg_a) == 0:  # a positivo
                        # o a vai passar de positivo para negativo e vai passar a somar
                        if self.get_reg_magnitude(reg_a) == 0:
                            self.registers[reg_a]["signal"] = 1
                            self.registers[reg_a]["magnitude"] = self.registers[reg_a]["magnitude"] + 1
                        else:
                            self.registers[reg_a]["magnitude"] = self.registers[reg_a]["magnitude"] - 1

                    else:  # a negativo
                        self.registers[reg_a]["magnitude"] = self.registers[reg_a]["magnitude"] + 1

                if self.get_reg_magnitude(reg_b) == 0:  # muda sinal de b se ele chegar a 0
                    self.registers[reg_b]["signal"] = 0
                # print(self)
                self.append_to_response()
        return self.response

    def add_b_to_a_with_c(self, reg_b="B", reg_a="A", reg_c="C"):
        print("{0}:={0} + {1} usando {2}".format(reg_a, reg_b, reg_c))
        self.append_to_response()
        self.set_0_to_reg(reg_c)

        while True:
            if self.get_reg_magnitude(reg_b) == 0:
                break
            else:  # se b diferente de 0
                self.registers[reg_b]["magnitude"] = self.registers[reg_b]["magnitude"] - 1  # decrementa b
                self.registers[reg_c]["magnitude"] = self.registers[reg_c]["magnitude"] + 1  # incrementa c
                if self.get_reg_signal(reg_b) == 0:  # b positivo
                    if self.get_reg_signal(reg_a) == 0:  # a positivo
                        self.registers[reg_a]["magnitude"] = self.registers[reg_a]["magnitude"] + 1
                    else:  # a negativo
                        self.registers[reg_a]["magnitude"] = self.registers[reg_a]["magnitude"] - 1
                        if self.get_reg_magnitude(reg_a) == 0:  # o a passa de negativo para positivo
                            self.registers[reg_a]["signal"] = 0
                else:  # b negativo
                    if self.get_reg_signal(reg_a) == 0:  # a positivo
                        if self.get_reg_magnitude(
                                reg_a) == 0:  # o a vai passar de positivo para negativo e vai passar a somar
                            self.registers[reg_a]["signal"] = 1
                            self.registers[reg_a]["magnitude"] = self.registers[reg_a]["magnitude"] + 1
                        else:
                            self.registers[reg_a]["magnitude"] = self.registers[reg_a]["magnitude"] - 1
                    else:  # a negativo
                        self.registers[reg_a]["magnitude"] = self.registers[reg_a]["magnitude"] + 1
                if self.get_reg_magnitude(reg_b) == 0:  # muda sinal de b se ele chegar a 0
                    self.registers[reg_c]["signal"] = self.registers[reg_b]["signal"]
                    self.registers[reg_b]["signal"] = 0
                # print(self)
                self.append_to_response()
        self.add_b_to_a(reg_c, reg_b)
        return self.response

    def set_b_to_a_with_c(self, reg_b="B", reg_a="A", reg_c="C"):
        print("{}:= {} usando {}".format(reg_a, reg_b, reg_c))
        self.append_to_response()
        self.set_0_to_reg(reg_a)
        self.add_b_to_a_with_c(reg_b, reg_a, reg_c)
        return self.response

    def mult_a_with_b_with_c_and_d(self, reg_a="A", reg_b="B", reg_c="C", reg_d="D"):
        print("{0}:={0} x {1} usando {2}, {3}".format(reg_a, reg_b, reg_c, reg_d))
        self.append_to_response()
        signal = 0
        if (self.get_reg_signal(reg_a) == 0 and self.get_reg_signal(reg_b) == 0) or \
                (self.get_reg_signal(reg_a) == 1 and self.get_reg_signal(reg_b) == 1):
            pass
        else:
            signal = 1
        self.set_0_to_reg(reg_c)
        self.add_b_to_a(reg_a, reg_c)

        while True:
            if self.get_reg_magnitude(reg_c) == 0:
                break
            else:
                self.add_b_to_a_with_c(reg_b, reg_a, reg_d)
                self.registers[reg_c]["magnitude"] = self.registers[reg_c]["magnitude"] - 1
                if self.get_reg_magnitude(reg_c) == 0:
                    self.registers[reg_c]["signal"] = 0
                # print(self)
                self.append_to_response()
        self.registers[reg_a]["signal"] = signal
        self.append_to_response()
        return self.response

    def test_a_lower_eq_than_b_auxc_auxd(self, reg_a="A", reg_b="B", reg_c="C", reg_d="D"):
        flag = False
        self.append_to_response()
        if self.get_reg_signal(reg_a) == 0:
            if self.get_reg_signal(reg_b) == 0:  # se os dois sao positivos subtrai e ve quem chega primeiro em 0
                while True:
                    if self.get_reg_magnitude(reg_a) == 0:
                        if self.get_reg_magnitude(reg_b) == 0:  # se os dois sao 0, retorna true
                            flag = True
                        break
                    if self.get_reg_magnitude(reg_b) == 0:
                        flag = False
                        break
                    self.registers[reg_a]["magnitude"] = self.registers[reg_a]["magnitude"] - 1
                    self.registers[reg_c]["magnitude"] = self.registers[reg_c]["magnitude"] + 1
                    self.registers[reg_b]["magnitude"] = self.registers[reg_b]["magnitude"] - 1
                    self.registers[reg_d]["magnitude"] = self.registers[reg_d]["magnitude"] + 1
                    self.append_to_response()

            else:  # se o a é positivo e o b é negativo então retorna falso (a > b)
                flag = False
                return self.response, flag
        else:  # se a é negativo
            if self.get_reg_signal(reg_b) == 0:  # e b é positivo retorna true
                flag = True
                return self.response, flag
            else:  # se os dois sao negativos
                while True:
                    if self.get_reg_magnitude(reg_a) == 0:
                        if self.get_reg_magnitude(reg_b) == 0:  # se os dois sao 0, retorna falso
                            flag = False
                        else:
                            flag = True
                        break
                    if self.get_reg_magnitude(reg_b) == 0:
                        flag = False
                        break

                    self.registers[reg_a]["magnitude"] = self.registers[reg_a]["magnitude"] - 1
                    self.registers[reg_c]["magnitude"] = self.registers[reg_c]["magnitude"] + 1
                    self.registers[reg_b]["magnitude"] = self.registers[reg_b]["magnitude"] - 1
                    self.registers[reg_d]["magnitude"] = self.registers[reg_d]["magnitude"] + 1
                    self.append_to_response()

        while True:
            if self.get_reg_magnitude(reg_c) == 0:
                break
            if self.get_reg_magnitude(reg_d) == 0:
                break
            self.registers[reg_a]["magnitude"] = self.registers[reg_a]["magnitude"] + 1
            self.registers[reg_c]["magnitude"] = self.registers[reg_c]["magnitude"] - 1
            self.registers[reg_b]["magnitude"] = self.registers[reg_b]["magnitude"] + 1
            self.registers[reg_d]["magnitude"] = self.registers[reg_d]["magnitude"] - 1
        return self.response, flag

    def test_a_lower_than_b_auxc_auxd(self, reg_a="A", reg_b="B", reg_c="E", reg_d="F"):
        self.set_0_to_reg(reg_c)
        self.set_0_to_reg(reg_d)
        flag = False
        self.append_to_response()

        if self.get_reg_signal(reg_a) == 0:
            if self.get_reg_signal(reg_b) == 0:  # se os dois sao positivos subtrai e ve quem chega primeiro em 0
                while True:
                    if self.get_reg_magnitude(reg_a) == 0:
                        if self.get_reg_magnitude(reg_b) == 0:  # se os dois sao 0, retorna falso
                            flag = False
                        else:
                            flag = True
                        break
                    if self.get_reg_magnitude(reg_b) == 0:
                        flag = False
                        break
                    self.registers[reg_a]["magnitude"] = self.registers[reg_a]["magnitude"] - 1
                    self.registers[reg_c]["magnitude"] = self.registers[reg_c]["magnitude"] + 1
                    self.registers[reg_b]["magnitude"] = self.registers[reg_b]["magnitude"] - 1
                    self.registers[reg_d]["magnitude"] = self.registers[reg_d]["magnitude"] + 1
                    self.append_to_response()

            else:  # se o a é positivo e o b é negativo então retorna falso (a > b)
                flag = False
                return self.response, flag
        else:  # se a é negativo
            if self.get_reg_signal(reg_b) == 0:  # e b é positivo retorna true
                flag = True
                return self.response, flag
            else:  # se os dois sao negativos
                while True:
                    if self.get_reg_magnitude(reg_a) == 0:
                        if self.get_reg_magnitude(reg_b) == 0:  # se os dois sao 0, retorna falso
                            flag = False
                        else:
                            flag = True
                        break
                    if self.get_reg_magnitude(reg_b) == 0:
                        flag = False
                        break

                    self.registers[reg_a]["magnitude"] = self.registers[reg_a]["magnitude"] - 1
                    self.registers[reg_c]["magnitude"] = self.registers[reg_c]["magnitude"] + 1
                    self.registers[reg_b]["magnitude"] = self.registers[reg_b]["magnitude"] - 1
                    self.registers[reg_d]["magnitude"] = self.registers[reg_d]["magnitude"] + 1
                    self.append_to_response()

        while True:
            if self.registers[reg_c]["magnitude"] == 0:
                break
            if self.registers[reg_d]["magnitude"] == 0:
                break
            self.registers[reg_a]["magnitude"] = self.registers[reg_a]["magnitude"] + 1
            self.registers[reg_c]["magnitude"] = self.registers[reg_c]["magnitude"] - 1
            self.registers[reg_b]["magnitude"] = self.registers[reg_b]["magnitude"] + 1
            self.registers[reg_d]["magnitude"] = self.registers[reg_d]["magnitude"] - 1
        return self.response, flag

    def factorial(self, n):
        error_msg = ''
        # Para evitar problemas na máquina, essa condição foi acrescentada
        if n < 0:  # não existe fatorial negativo
            error_msg += "ERROR: Illegal Instruction."
            self.append_to_response()
            return self.response, error_msg
        print("Calculando o fatorial de {}".format(n))
        self.append_to_response()
        if n == 0:  # 0! = 1
            self.set_n_to_reg("A", 1)
            return self.response, error_msg

        self.set_n_to_reg("B", n)  # B := n, the value we want factorial from
        self.set_n_to_reg("A", 1)
        while True:
            if self.registers["B"]["magnitude"] == 0:
                break
            else:
                self.mult_a_with_b_with_c_and_d()
                self.registers["B"]["magnitude"] -= 1
            self.append_to_response()
        return self.response, error_msg

    def power(self, a, b):
        error_msg = ''
        if b < 0:
            error_msg += "ERROR: Not yet supported"
            return self.response, error_msg
        print("Power of {} to {}".format(a, b))
        self.append_to_response()
        if b == 0:  # if exponent is 0, result is 1
            self.set_n_to_reg("A", 1)
        elif a == 0:  # if base is zero, result is 0
            self.set_0_to_reg("A")
        else:  # a != 0 and b > 0
            self.set_n_to_reg("A", a)
            self.set_n_to_reg("E", b)
            while True:
                if self.get_reg_magnitude("E") == 0:
                    break
                else:
                    self.registers["E"]["magnitude"] -= 1
                    if self.get_reg_magnitude("E") == 0:
                        break
                    self.set_n_to_reg("B", self.get_reg_magnitude("A"))
                    self.mult_a_with_b_with_c_and_d()
                # print(self)
                self.append_to_response()
        return self.response, error_msg
