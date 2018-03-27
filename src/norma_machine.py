import math


class NormaMachine:

    def __init__(self):
        self.registers = {
            "A": 0,
            "B": 0,
            "C": 0,
            "D": 0,
        }

    def __str__(self):
        msg = ""
        msg += "A:({},{}) | ".format(0 if self.registers["A"] >= 0 else 1, abs(self.registers["A"]))
        msg += "B:({},{}) | ".format(0 if self.registers["B"] >= 0 else 1, abs(self.registers["B"]))
        msg += "C:({},{}) | ".format(0 if self.registers["C"] >= 0 else 1, abs(self.registers["C"]))
        msg += "D:({},{})".format(0 if self.registers["D"] >= 0 else 1, abs(self.registers["D"]))
        return msg

    def set_0_to_reg(self, register):
        print("Set 0 to {}".format(register))
        print(self)
        while self.registers[register] != 0:
            if self.registers[register] > 0:
                self.registers[register] -= 1
            else:
                self.registers[register] += 1
            print(self)

    def set_n_to_reg(self, reg, n):
        print("Set {} to {}".format(n, reg))
        while self.registers[reg] != n:
            if n == 0:
                self.set_0_to_reg(reg)
            elif n > self.registers[reg]:
                self.registers[reg] += 1
            else:
                self.registers[reg] -= 1
            print(self)

    def add_b_to_a(self, regB, regA):
        print("Add B to A")
        while self.registers[regB] != 0:
            if self.registers[regB] > 0:
                self.registers[regA] += 1
                self.registers[regB] -= 1
            else:
                self.registers[regA] -= 1
                self.registers[regB] += 1
            print(self)

    def add_b_to_a_with_c(self, regB, regA, regC):
        print("Add B to A with C")
        while self.registers[regB] != 0:
            if self.registers[regB] > 0:
                self.registers[regA] += 1
                self.registers[regB] -= 1
                self.registers[regC] += 1
            else:
                self.registers[regA] -= 1
                self.registers[regB] += 1
                self.registers[regC] -= 1
            print(self)
        while self.registers[regC] != 0:
            if self.registers[regC] > 0:
                self.registers[regB] += 1
                self.registers[regC] -= 1
            else:
                self.registers[regB] -= 1
                self.registers[regC] += 1
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

    def test_a_lower_than_b(self, regA, regB):
        return self.registers[regA] < self.registers[regB]

    def test_a_lower_e_than_b(self, regA, regB):
        return self.registers[regA] <= self.registers[regB]

    def is_primal(self, reg):
        n = self.registers[reg]
        start = 2;

        while start <= math.sqrt(n):
            if n % start < 1:
                return print("False")
            start += 1

        return print(n > 1)

    def remainder_division_of_a_by_b(self,regA,regB):
        return self.registers[regA] % self.registers[regB]

    def factorial(self,reg):
        return math.factorial(self.registers[reg])

    def potential(self,regA,regB):
        return self.registers[regA] ** self.registers[regB]