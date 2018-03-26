class NormaMachine:

    def __init__(self):
        self.registers = dict(
            A={
                "signal": 0,
                "magnitude": 0,
            },
            B={
                "signal": 0,
                "magnitude": 0,
            },
            C={
                "signal": 0,
                "magnitude": 0,
            },
            D={
                "signal": 0,
                "magnitude": 0,
            },
        )

    def __str__(self):
        msg = ""
        msg += "A: ({},{}) | ".format(self.registers["A"]["signal"], self.registers["A"]["magnitude"])
        msg += "B: ({},{}) | ".format(self.registers["B"]["signal"], self.registers["B"]["magnitude"])
        msg += "C: ({},{}) | ".format(self.registers["C"]["signal"], self.registers["C"]["magnitude"])
        msg += "D: ({},{})".format(self.registers["D"]["signal"], self.registers["D"]["magnitude"])
        return msg

    def set_0_to_reg(self, reg):
        print("Set 0 to {}".format(reg))
        print(self)
        while self.registers[reg]["magnitude"] != 0:
            self.registers[reg]["magnitude"] -= 1
            print(self)
        self.registers[reg]["signal"] = 0
        print(self)

    def set_n_to_reg(self, reg, n):
        print("Set {} to {}".format(n, reg))
        print(self)
        register = self.registers[reg]
        number = abs(n)
        while register["magnitude"] != number:
            if (n == 0):
                self.set_0_to_reg(reg)
            elif (n > 0):
                if register["signal"] != 0:  # signal negativo
                    self.set_0_to_reg(reg)
                else:
                    if number > register["magnitude"]:
                        register["magnitude"] += 1
                    else:
                        register["magnitude"] -= 1
            else:
                if register["signal"] == 0:  # signal positivo
                    self.set_0_to_reg(reg)
                    register["signal"] = 1
                else:
                    if number > register["magnitude"]:
                        register["magnitude"] += 1
                    else:
                        register["magnitude"] -= 1
            if (register["signal"] == 1 and register["magnitude"] == 0):
                continue
            else:
                print(self)
