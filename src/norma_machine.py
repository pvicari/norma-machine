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

    def add_b_to_a(self):
        print("Add B to A")
        while self.registers["B"] != 0:
            if self.registers["B"] > 0:
                self.registers["A"] += 1
                self.registers["B"] -= 1
            else:
                self.registers["A"] -= 1
                self.registers["B"] += 1
            print(self)

    def add_b_to_a_with_c(self):
        print("Add B to A with C")
        while self.registers["B"] != 0:
            if self.registers["B"] > 0:
                self.registers["A"] += 1
                self.registers["B"] -= 1
                self.registers["C"] += 1
            else:
                self.registers["A"] -= 1
                self.registers["B"] += 1
                self.registers["C"] -= 1
            print(self)
        while self.registers["C"] != 0:
            if self.registers["C"] > 0:
                self.registers["B"] += 1
                self.registers["C"] -= 1
            else:
                self.registers["B"] -= 1
                self.registers["C"] += 1
            print(self)
