

# 1. Построить график неявной функции
# 2. Решение системы для пполучения уравнения конического сечения
# 3. Определить его тип.
# P.S Скорее всего все пойдет не по плану, просто набросил
#
#
#

from symmetrical_conic_section import graph_utils, curves, conic_section_utils, conic_section

box_center = (0, 0)
box_size = (2, 2)
relative_position_on_left_side = 0.6

first_added_point = (-0.8, 0.95)
second_added_point = (-0.5, -0.8)

func = conic_section.symmetric_conic_section_in_box(
    box_center, box_size, relative_position_on_left_side,
    first_added_point, second_added_point)


graph_utils.draw_implicit_function_2d(
    func,
    (box_center[0] - box_size[0] / 2 - 0.1, box_center[0] + box_size[0] / 2 + 0.1),
    (box_center[1] - box_size[1] / 2 - 0.1, box_center[1] + box_size[1] / 2 + 0.1)
)


