from typing import Tuple

from symmetrical_conic_section import conic_section_utils, curves, curves_classification


def symmetric_conic_section_in_box(
        box_center: Tuple[float, float], box_size: Tuple[float, float],
        relative_position_on_left_side: float,
        first_added_point: Tuple[float, float], second_added_point: Tuple[float, float]
):
    assert 0 <= relative_position_on_left_side <= 1
    right_upper_border = (box_center[0] + box_size[0] / 2, box_center[1] + box_size[1] / 2)
    left_upper_border = (box_center[0] - box_size[0] / 2, box_center[1] + box_size[1] / 2)
    left_lower_border = (box_center[0] - box_size[0] / 2, box_center[1] - box_size[1] / 2)
    right_lower_border = (box_center[0] + box_size[0] / 2, box_center[1] - box_size[1] / 2)

    upper_tangent_line = curves.FirstOrderImplicitCurve.from_points(right_upper_border, left_upper_border)
    lower_tangent_line = curves.FirstOrderImplicitCurve.from_points(left_lower_border, right_lower_border)
    left_tangent_line = curves.FirstOrderImplicitCurve.from_points(left_upper_border, left_lower_border)
    right_tangent_line = curves.FirstOrderImplicitCurve.from_points(right_upper_border, right_lower_border)

    y_border = (1 - relative_position_on_left_side) * left_lower_border[1] + \
        relative_position_on_left_side * left_upper_border[1]

    upper_point = (box_center[0], box_center[1] + box_size[1] / 2)
    lower_point = (box_center[0], box_center[1] - box_size[1] / 2)
    left_point = (
        box_center[0] - box_size[0] / 2,
        y_border
    )
    right_point = (
        box_center[0] + box_size[0] / 2,
        y_border
    )

    success, left_upper_func = conic_section_utils.compute_conic_section_using_3_points_and_2_tangent_lines(
        [
            (upper_point, upper_tangent_line),
            (left_point, left_tangent_line)
        ], first_added_point
    )
    if not success:
        return False, [], [], [[], []]
    success, left_lower_func = conic_section_utils.compute_conic_section_using_3_points_and_2_tangent_lines(
        [
            (left_point, left_tangent_line),
            (lower_point, lower_tangent_line)
        ], second_added_point
    )
    if not success:
        return False, [], [], [[], []]

    first_added_point_mirrored = (2 * box_center[0] - first_added_point[0], first_added_point[1])
    success, right_upper_func = conic_section_utils.compute_conic_section_using_3_points_and_2_tangent_lines(
        [
            (upper_point, upper_tangent_line),
            (right_point, right_tangent_line)
        ], first_added_point_mirrored
    )
    if not success:
        return False, [], [], [[], []]

    second_added_point_mirrored = (2 * box_center[0] - second_added_point[0], second_added_point[1])
    success, right_lower_func = conic_section_utils.compute_conic_section_using_3_points_and_2_tangent_lines(
        [
            (right_point, right_tangent_line),
            (lower_point, lower_tangent_line)
        ], second_added_point_mirrored
    )
    if not success:
        return False, [], [], [[], []]

    return True, conic_section_utils.combined_conic_section_function(
        [
            #
            (left_lower_func, (box_center[0] - box_size[0] / 2, box_center[0]),
             (box_center[1] - box_size[1] / 2, y_border)),
            #
            (left_upper_func, (box_center[0] - box_size[0] / 2, box_center[0]),
             (y_border, box_center[1] + box_size[1] / 2)),
            #
            (right_upper_func, (box_center[0], box_center[0] + box_size[0] / 2),
             (y_border, box_center[1] + box_size[1] / 2)),
            #
            (right_lower_func, (box_center[0], box_center[0] + box_size[0] / 2),
             (box_center[1] - box_size[1] / 2, y_border))
        ]
    ), \
    [
        curves_classification.curve_class(left_lower_func) +
            "\n a11 = " + str(left_lower_func.a11) +
            "\n a12 = " + str(left_lower_func.a12) +
            "\n a22 = " + str(left_lower_func.a22) +
            "\n a13 = " + str(left_lower_func.a13) +
            "\n a23 = " + str(left_lower_func.a23) +
            "\n a33 = " + str(left_lower_func.a33),
        curves_classification.curve_class(left_upper_func) +
            "\n a11 = " + str(left_upper_func.a11) +
            "\n a12 = " + str(left_upper_func.a12) +
            "\n a22 = " + str(left_upper_func.a22) +
            "\n a13 = " + str(left_upper_func.a13) +
            "\n a23 = " + str(left_upper_func.a23) +
            "\n a33 = " + str(left_upper_func.a33),
        curves_classification.curve_class(right_upper_func) +
            "\n a11 = " + str(right_upper_func.a11) +
            "\n a12 = " + str(right_upper_func.a12) +
            "\n a22 = " + str(right_upper_func.a22) +
            "\n a13 = " + str(right_upper_func.a13) +
            "\n a23 = " + str(right_upper_func.a23) +
            "\n a33 = " + str(right_upper_func.a33),
        curves_classification.curve_class(right_lower_func) +
            "\n a11 = " + str(right_lower_func.a11) +
            "\n a12 = " + str(right_lower_func.a12) +
            "\n a22 = " + str(right_lower_func.a22) +
            "\n a13 = " + str(right_lower_func.a13) +
            "\n a23 = " + str(right_lower_func.a23) +
            "\n a33 = " + str(right_lower_func.a33)
    ], \
    (
        [
            left_point[0],
            upper_point[0],
            right_point[0],
            lower_point[0],
            first_added_point[0],
            second_added_point[0],
            first_added_point_mirrored[0],
            second_added_point_mirrored[0],
        ],
        [
            left_point[1],
            upper_point[1],
            right_point[1],
            lower_point[1],
            first_added_point[1],
            second_added_point[1],
            first_added_point_mirrored[1],
            second_added_point_mirrored[1],
        ]
    )
