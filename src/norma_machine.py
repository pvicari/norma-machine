import math


class NormaMachine:

    def __init__(self):
        """
        Norma Machine

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
        while self.registers[register] != 0:  # if the register is not yet zero
            if self.registers[register] > 0:  # and it's value is > 0
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
        while self.registers[reg] != n:  # while the value is not set
            if n == 0:
                self.set_0_to_reg(reg)
            elif n > self.registers[reg]:  # if the magnitude is greater
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
        """
        Add value of reg B to A conserving value

        A:= A+B using C

        :param reg_b: a given register (will be 0 after operation)
        :type reg_b: str
        :param reg_a: target register
        :type reg_a: str
        :param reg_c: the register used to conserve B's value
        :type reg_c: str
        :return: None
        """
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
        """
        Set A to B using C to conserve value

        A:=B using C

        :return: None
        """
        self.set_0_to_reg("A")  # set A to 0
        self.add_b_to_a_with_c("B", "A", "C")  # does attribution with C

    def mult_a_with_b(self):
        while self.registers["A"] != 0:
            # passes value of A to C
            self.registers["C"] += 1
            self.registers["A"] -= 1
            while self.registers["C"] != 0:
                # does multiple sums using D as auxiliary register
                self.add_b_to_a_with_c("B", "A", "D")
                self.registers["C"] -= 1  # decrements C

    def test_a_lower_than_b(self, reg_a, reg_b):
        """
        Tests if A < B

        A < B

        :param reg_a: first register
        :type reg_a: str
        :param reg_b: target register
        :type reg_b: str
        :return: True if reg_a < than reg_b
        :rtype: bool
        """
        return self.registers[reg_a] < self.registers[reg_b]

    def test_a_lower_equals_than_b(self, reg_a, reg_b):
        """
        Tests if A <= B

        A <= B

        :param reg_a: first register
        :type reg_a: str
        :param reg_b: target register
        :type reg_b: str
        :return: True if reg_a < than reg_b
        :rtype: bool
        """
        return self.registers[reg_a] <= self.registers[reg_b]

    def is_primal(self, reg):
        """
        Test if a given register contains a prime value

        :param reg: target register
        :type reg: str
        :return: False if the register does not contain a prime
        :rtype: bool
        """
        n = self.registers[reg]
        start = 2  # first prime number

        while start <= math.sqrt(n):  # using theorem to limit execution
            if n % start < 1:  # if it is divisible by start it's not prime
                return False
            start += 1
        return n > 1  # Is the number greater than 1 (1 is not prime)

    def remainder_division_of_a_by_b(self, reg_a, reg_b):
        """
        Returns the remainder of a de division between two given registers
        :param reg_a: dividend
        :type reg_a: str
        :param reg_b: divisor
        :type reg_b: str
        :return: A mod B
        :rtype: int
        """
        return self.registers[reg_a] % self.registers[reg_b]

    def factorial(self, reg):
        """
        Returns Factorial of a given register
        :param reg: target register
        :type reg: str
        :return: reg!
        :rtype: int
        """
        return math.factorial(self.registers[reg])

    def potential(self, reg_a, reg_b):
        """
        Returns reg_a to the power of reg_b
        :param reg_a: base
        :type reg_a: str
        :param reg_b: exponent
        :type reg_b: str
        :return: a^b
        """
        return pow(self.registers[reg_a], self.registers[reg_b])  # same as x ** y
