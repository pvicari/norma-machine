from collections import namedtuple


class NormaMachine:
    Register = namedtuple('Register', ['signal', 'magnitude'])

    def __init__(self):
        self.registers = dict(
            A=NormaMachine.Register(0, 0),
            B=NormaMachine.Register(0, 0),
            C=NormaMachine.Register(0, 0),
            D=NormaMachine.Register(0, 0)
        )

    def __str__(self):
        msg = ""
        msg += "A: ({},{}) | ".format(self.registers["A"].signal, self.registers["A"].magnitude)
        msg += "B: ({},{}) | ".format(self.registers["B"].signal, self.registers["B"].magnitude)
        msg += "C: ({},{}) | ".format(self.registers["C"].signal, self.registers["C"].magnitude)
        msg += "D: ({},{})".format(self.registers["D"].signal, self.registers["D"].magnitude)
        return msg

    def set_0_to_reg(self, reg):
        while self.registers[reg].magnitude != 0:
            if self.registers[reg].signal != 0:
                self.registers[reg].magnitude += 1
            else:
                self.registers[reg].magnitude -= 1
            print(self)
