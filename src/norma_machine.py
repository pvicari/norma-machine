import math


class NormaMachine:

    def __init__(self):
        """
        Norma Machine constructor.

        Starts all registers at zero
        """
        self.registers = {
            "A": 0,
            "B": 0,
            "C": 0,
            "D": 0,
        }

    def __str__(self):
        """
        Print function
        :return: msg with register info
        :rtype: str
        """
        msg = ""
        msg += "A:({},{}) | ".format(0 if self.registers["A"] >= 0 else 1, abs(self.registers["A"]))
        msg += "B:({},{}) | ".format(0 if self.registers["B"] >= 0 else 1, abs(self.registers["B"]))
        msg += "C:({},{}) | ".format(0 if self.registers["C"] >= 0 else 1, abs(self.registers["C"]))
        msg += "D:({},{})".format(0 if self.registers["D"] >= 0 else 1, abs(self.registers["D"]))
        return msg

    def set_0_to_reg(self, register):
        """
        Set 0 to a passed register

        register := 0

        :param register: target register
        :type register: str
        :return: None
        """
        print("Set 0 to {}".format(register))
        print(self)
        while self.registers[register] != 0:
            if self.registers[register] > 0:
                self.registers[register] -= 1
            else:
                self.registers[register] += 1
            print(self)

    def set_n_to_reg(self, reg, n):
        """
        Set N to a passed register

        reg := n

        :param reg: target register
        :type reg: str
        :param n: new value for the register
        :type n: int
        :return: None
        """
        print("Set {} to {}".format(n, reg))
        while self.registers[reg] != n:
            if n == 0:
                self.set_0_to_reg(reg)
            elif n > self.registers[reg]:
                self.registers[reg] += 1
            else:
                self.registers[reg] -= 1
            print(self)

    def add_b_to_a(self, reg_b, reg_a):
        """
        Add value of reg B to A without conserving value

        A:= A+B

        :param reg_b: a given register (will be 0 after operation)
        :type reg_b: str
        :param reg_a: target register
        :type reg_a: str
        :return: None
        """
        print("Add B to A")
        while self.registers[reg_b] != 0:
            if self.registers[reg_b] > 0:
                self.registers[reg_a] += 1
                self.registers[reg_b] -= 1
            else:
                self.registers[reg_a] -= 1
                self.registers[reg_b] += 1
            print(self)

    def add_b_to_a_with_c(self, reg_b, reg_a, reg_c):
        print("Add B to A with C")
        while self.registers[reg_b] != 0:
            if self.registers[reg_b] > 0:
                self.registers[reg_a] += 1
                self.registers[reg_b] -= 1
                self.registers[reg_c] += 1
            else:
                self.registers[reg_a] -= 1
                self.registers[reg_b] += 1
                self.registers[reg_c] -= 1
            print(self)
        while self.registers[reg_c] != 0:
            if self.registers[reg_c] > 0:
                self.registers[reg_b] += 1
                self.registers[reg_c] -= 1
            else:
                self.registers[reg_b] -= 1
                self.registers[reg_c] += 1
            print(self)

    def set_b_to_a_with_c(self):
        self.set_0_to_reg("A")
        self.add_b_to_a_with_c("B", "A", "C")

    def mult_a_with_b(self):
        while self.registers["A"] != 0:
            self.registers["C"] += 1
            self.registers["A"] -= 1
            while self.registers["C"] != 0:
                self.add_b_to_a_with_c("B", "A", "D")
                self.registers["C"] -= 1

    def test_a_lower_than_b(self, reg_a, reg_b):
        return self.registers[reg_a] < self.registers[reg_b]

    def test_a_lower_e_than_b(self, reg_a, reg_b):
        return self.registers[reg_a] <= self.registers[reg_b]

    def is_primal(self, reg):
        n = self.registers[reg]
        start = 2

        while start <= math.sqrt(n):
            if n % start < 1:
                return False
            start += 1

        return n > 1

    def remainder_division_of_a_by_b(self, reg_a, reg_b):
        return self.registers[reg_a] % self.registers[reg_b]

    def factorial(self, reg):
        return math.factorial(self.registers[reg])

    def potential(self, reg_a, reg_b):
        return self.registers[reg_a] ** self.registers[reg_b]
