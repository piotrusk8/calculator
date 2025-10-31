class Calculator:
    def __init__(self, op1: float, op2: float):
        self.__op1 = op1
        self.__op2 = op2

    def sum(self) -> float:
        return self.__op1 + self.__op2

    def sub(self) -> float:
        return self.__op1 - self.__op2

    def mul(self) -> float:
        return self.__op1 * self.__op2

    def div(self) -> float:
        if self.__op2 == 0:
            raise ZeroDivisionError("Dzielenie przez zero!")
        return self.__op1 / self.__op2


if __name__ == "__main__": # pragma: no cover
    calc = Calculator(10, 2) # pragma: no cover
    print("Suma:", calc.sum()) # pragma: no cover
    print("Różnica:", calc.sub()) # pragma: no cover
    print("Iloczyn:", calc.mul()) # pragma: no cover
    print("Iloraz:", calc.div()) # pragma: no cover