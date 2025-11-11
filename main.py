from circle import area as circle_area, perimeter as circle_perimeter
from square import area as square_area, perimeter as square_perimeter
from rectangle import area as rect_area, perimeter as rect_perimeter
from triangle import area as tri_area, perimeter as tri_perimeter

print(round(circle_area(3), 2))
print(round(circle_perimeter(3), 2))
print(round(square_area(4), 2))
print(round(square_perimeter(4), 2))
print(round(rect_area(3, 5), 2))
print(round(rect_perimeter(3, 5), 2))
print(round(tri_area(6, 4), 2))
print(round(tri_perimeter(3, 4, 5), 2))
