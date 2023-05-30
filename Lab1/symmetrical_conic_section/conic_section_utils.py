from typing import List, Tuple

import numpy as np

from symmetrical_conic_section import curves


def closest_conic_section_value_of_point(
    x: float, y: float,
    conic_section_and_borders: List[Tuple[curves.SecondOrderImplicitCurve, Tuple[float, float], Tuple[float, float]]]
) -> float:
    for conic_section_and_border in conic_section_and_borders:
        if x >= conic_section_and_border[1][0] - 1e-2 \
                and x <= conic_section_and_border[1][1] + 1e-2 \
                and y >= conic_section_and_border[2][0] - 1e-2 \
                and y <= conic_section_and_border[2][1] + 1e-2:
             if curves.SecondOrderImplicitCurve.point_belongs_to_curve(conic_section_and_border[0], (x, y)):
                 return conic_section_and_border[0](x, y)

    return None


def combined_conic_section_function(
        conic_section_and_borders: List[Tuple[curves.SecondOrderImplicitCurve, Tuple[float, float], Tuple[float, float]]]
):
    func = lambda x, y: \
        closest_conic_section_value_of_point(x, y, conic_section_and_borders)
    return func


def compute_conic_section_using_3_points_and_2_tangent_lines(
        points_with_tangent_lines: List[Tuple[Tuple[float, float], curves.FirstOrderImplicitCurve]],
        point: Tuple[float, float]
) -> (bool, curves.SecondOrderImplicitCurve):
    assert len(points_with_tangent_lines) == 2
    secant_line = curves.FirstOrderImplicitCurve.from_points(
        points_with_tangent_lines[0][0], points_with_tangent_lines[1][0])
    return compute_conic_section_using_lines_and_point(
        [
            points_with_tangent_lines[0][1],
            points_with_tangent_lines[1][1],
            secant_line,
            secant_line
        ],
        point
    )


def compute_conic_section_using_5_points(
        points: List[Tuple[float, float]]
) -> (bool, curves.SecondOrderImplicitCurve):
    assert len(points) == 5
    lines = [
        curves.FirstOrderImplicitCurve.from_points(points[0], points[1]),
        curves.FirstOrderImplicitCurve.from_points(points[2], points[3]),
        curves.FirstOrderImplicitCurve.from_points(points[0], points[3]),
        curves.FirstOrderImplicitCurve.from_points(points[1], points[2])
    ]
    return compute_conic_section_using_lines_and_point(lines, points[4])


def compute_conic_section_using_lines_and_point(
        lines: List[curves.FirstOrderImplicitCurve],
        point: Tuple[float, float]
) -> (bool, curves.SecondOrderImplicitCurve):
    assert len(lines) == 4
    for line in lines:
        if curves.FirstOrderImplicitCurve.point_belongs_to_line(line, point):
            return False, curves.SecondOrderImplicitCurve([0, 0, 0, 0, 0, 0])
    first_lines = lines[0] * lines[1]
    second_lines = lines[2] * lines[3]
    x, y = point
    scalar = first_lines(x, y) / (first_lines(x, y) - second_lines(x, y))
    return True, first_lines * (1 - scalar) + second_lines * scalar