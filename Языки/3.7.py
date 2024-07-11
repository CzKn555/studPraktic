a = int(input())
b = int(input())
c = int(input())
can_form_triangle = "YES" if (a < b + c) and (b < a + c) and (c < a + b) else "NO"
print(can_form_triangle)