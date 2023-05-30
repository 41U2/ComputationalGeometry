import string

from symmetrical_conic_section import curves


def invariant_1(curve: curves.SecondOrderImplicitCurve) -> float:
    return curve.a11 + curve.a22


def invariant_2(curve: curves.SecondOrderImplicitCurve) -> float:
    return curve.a11 * curve.a22 - curve.a12 * curve.a12


def invariant_3(curve: curves.SecondOrderImplicitCurve) -> float:
    return curve.a11 * (curve.a22 * curve.a33 - curve.a23 ** 2) - \
           curve.a12 * (curve.a12 * curve.a33 - curve.a13 * curve.a23) + \
           curve.a13 * (curve.a12 * curve.a23 - curve.a13 * curve.a22)


def rotation_invariant(curve: curves.SecondOrderImplicitCurve) -> float:
    return curve.a22 * curve.a33 - curve.a23 ** 2 + curve.a11 * curve.a33 - curve.a13 ** 2


def curve_class(curve: curves.SecondOrderImplicitCurve) -> string:
    treshold = 1e-4
    i1 = invariant_1(curve)
    i2 = invariant_2(curve)
    i3 = invariant_3(curve)
    a = rotation_invariant(curve)
    if abs(i3) < treshold:
        if i2 > treshold:
            return "Действительная точка"
        if i2 < -treshold:
            return "Пара действительных пересекающихся прямых"
        if a > treshold:
            return "Нет действительных точек"
        if a < -treshold:
            return "Пара действительных параллельных прямых"
        return "Пара совпадающих прямых"

    if abs(i2) < treshold:
        return "Парабола"

    if i2 < -treshold:
        return "Гипербола"

    scalar = i3 / i1
    if scalar < -treshold:
        return "Эллипс"
    return "Мнимый эллипс"


def test_crossing_lines():
    line_1 = curves.FirstOrderImplicitCurve([1, 1, 0])
    line_2 = curves.FirstOrderImplicitCurve([1, -1, 0])

    curve = line_1 * line_2
    print(curve_class(curve))


def test_parallel_lines():
    line_1 = curves.FirstOrderImplicitCurve([1, 1, 0])
    line_2 = curves.FirstOrderImplicitCurve([1, 1, 1])

    curve = line_1 * line_2
    print(curve_class(curve))


def test_same_lines():
    line_1 = curves.FirstOrderImplicitCurve([1, 1, 0])

    curve = line_1 * line_1
    print(curve_class(curve))


def test_parabola():
    curve = curves.SecondOrderImplicitCurve([1, 0, 0, 0, 1, 0])
    print(curve_class(curve))


def test_ellipse():
    curve = curves.SecondOrderImplicitCurve([1, 0, 2, 0, 0, -1])
    print(curve_class(curve))


def test_i_ellipse():
    curve = curves.SecondOrderImplicitCurve([1, 0, 2, 0, 0, 1])
    print(curve_class(curve))


test_crossing_lines()
test_parallel_lines()
test_same_lines()
test_parabola()
test_ellipse()
test_i_ellipse()
