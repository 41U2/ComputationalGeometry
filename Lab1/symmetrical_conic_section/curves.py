from typing import List, Tuple


class SecondOrderImplicitCurve:

    def __init__(self, coeffs: List[float]):
        assert len(coeffs) == 6
        self.a11 = coeffs[0]
        self.a12 = coeffs[1] / 2.
        self.a22 = coeffs[2]
        self.a13 = coeffs[3] / 2.
        self.a23 = coeffs[4] / 2.
        self.a33 = coeffs[5]

    def __call__(self, x: float, y: float):
        return \
            self.a11 * x * x + \
            self.a12 * 2 * x * y + \
            self.a22 * y * y + \
            self.a13 * 2 * x + \
            self.a23 * 2 * y + \
            self.a33

    def __add__(self, other: "SecondOrderImplicitCurve") -> "SecondOrderImplicitCurve":
        return SecondOrderImplicitCurve([
            (self.a11 + other.a11),
            (self.a12 + other.a12) * 2,
            (self.a22 + other.a22),
            (self.a13 + other.a13) * 2,
            (self.a23 + other.a23) * 2,
            (self.a33 + other.a33)
        ])

    def __mul__(self, scalar: float) -> "SecondOrderImplicitCurve":
        return SecondOrderImplicitCurve([
            scalar * self.a11,
            scalar * self.a12 * 2,
            scalar * self.a22,
            scalar * self.a13 * 2,
            scalar * self.a23 * 2,
            scalar * self.a33
        ])

    @staticmethod
    def point_belongs_to_curve(curve: "SecondOrderImplicitCurve", point: Tuple[float, float]) -> bool:
        x, y = point
        value = curve(x, y)
        if abs(value) <= 3e-2:
            return True
        return False


class FirstOrderImplicitCurve:

    def __init__(self, coeffs: List[float]):
        assert len(coeffs) == 3
        self.a1 = coeffs[0]
        self.a2 = coeffs[1]
        self.a3 = coeffs[2]

    def __call__(self, x: float, y: float):
        return self.a1 * x + self.a2 * y + self.a3

    def __mul__(self, scalar: float) -> "FirstOrderImplicitCurve":
        return FirstOrderImplicitCurve([scalar * self.a1, scalar * self.a2, scalar * self.a3])

    def __add__(self, other: "FirstOrderImplicitCurve") -> "FirstOrderImplicitCurve":
        return FirstOrderImplicitCurve([other.a1 + self.a1, other.a2 + self.a2, other.a3 + self.a3])

    def __mul__(self, other: "FirstOrderImplicitCurve") -> "SecondOrderImplicitCurve":
        return SecondOrderImplicitCurve([
            self.a1 * other.a1,
            self.a1 * other.a2 + self.a2 * other.a1,
            self.a2 * other.a2,
            self.a1 * other.a3 + self.a3 * other.a1,
            self.a2 * other.a3 + self.a3 * other.a2,
            self.a3 * other.a3
        ])

    @staticmethod
    def from_points(first_point: Tuple[float, float], second_point: Tuple[float, float]) -> "FirstOrderImplicitCurve":
        a1 = 0
        a2 = 0
        a3 = 0

        x1, y1 = first_point
        x2, y2 = second_point

        if x1 == x2:
            a1 = 1
            a2 = 0
            a3 = -x1
        elif y1 == y2:
            a1 = 0
            a2 = 1
            a3 = -y1
        else:
            a2 = 1
            a1 = a2 * (y2 - y1) / (x1 - x2)
            a3 = - a1 * x1 - a2 * y1
        return FirstOrderImplicitCurve([a1, a2, a3])

    @staticmethod
    def point_belongs_to_line(line: "FirstOrderImplicitCurve", point: Tuple[float, float]) -> bool:
        x, y = point
        value = line(x, y)
        if value == 0:
            return True
        return False
