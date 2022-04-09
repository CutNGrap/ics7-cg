#ЦДА
def cda(start, end):
    if start == end:
        return [start]
    cur_x = start[0]
    cur_y = start[1]
    dx = dx = end[0] - start[0]
    dy = end[1] - start[1]
    if abs(dx) >= abs(dy):
        l = abs(dx)
    else:
        l = abs(dy)
    dx /= l
    dy /= l
    dots = []
    for i in range(l + 1):
        dots.append([round(cur_x), round(cur_y)])
        cur_x += dx
        cur_y += dy
    return dots

def br_fl(start, end):
    if start == end:
        return [start]
    cur_x = start[0]
    cur_y = start[1]
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    sx = sign(dx)
    sy = sign(dy)
    dx = abs(dx)
    dy = abs(dy)
    if dx > dy:
        change = False
    else:
        change = True
        dx, dy = dy, dx
    m = dy / dx
    e = m - 0.5
    l = dx + 1
    points = [0] * l
    for i in range(l):
        points[i] = [cur_x, cur_y]
        if e >= 0:
            if change:
                cur_x += sx
            else:
                cur_y += sy
            e -= 1
        if e < 0:
            if change:
                cur_y += sy
            else:
                cur_x += sx
            e += m
    return points

def br_int(start, end):
    if start == end:
        return [start]
    cur_x = start[0]
    cur_y = start[1]
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    sx = sign(dx)
    sy = sign(dy)
    dx = abs(dx)
    dy = abs(dy)
    if dx > dy:
        change = False
    else:
        change = True
        dx, dy = dy, dx
    double_dy = 2 * dy
    double_dx = 2 * dx
    e = double_dy - dx
    l = dx + 1
    points = [0] * l
    for i in range(l):
        points[i] = [cur_x, cur_y]
        if e >= 0:
            if change:
                cur_x += sx
            else:
                cur_y += sy
            e -= double_dx
        if e < 0:
            if change:
                cur_y += sy
            else:
                cur_x += sx
            e += double_dy
    return points

def br_smooth(start, end, imax):
    if start == end:
        return [Qstart], [Imax]
    cur_x = start[0]
    cur_y = start[1]
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    sx = sign(dx)
    sy = sign(dy)
    dx = abs(dx)
    dy = abs(dy)
    if dx > dy:
        change = False
    else:
        change = True
        dx, dy = dy, dx
    m = dy / dx * imax
    e = imax / 2
    w = imax - m
    l = dx + 1
    points = [0] * l
    alpha = [0] * l
    for i in range(l):
        points[i] = [cur_x, cur_y]
        alpha[i] = imax - e
        if e <= w:
            if change:
                cur_y += sy
            else:
                cur_x += sx
            e += m
        else:
            cur_x += sx
            cur_y += sy
            e -= w
    return points, alpha


def vu(start, end, imax):
    if start == end:
        return [start], [imax]
    x0, y0 = start
    x1, y1 = end
    dx = x1 - x0
    dy = y1 - y0
    change = abs(dx) < abs(dy)
    if change:
        x0, y0 = y0, x0
        x1, y1 = y1, x1
    if x1 < x0:
        x0, x1 = x1, x0
        y0, y1 = y1, y0
    dx = x1 - x0
    dy = y1 - y0
    grad = dy / dx if dx else 1
    cur_y = y0
    cur_x = x0
    l = 2 * (x1 - x0 + 1)
    points = [0] * l
    alpha = [0] * l
    for i in range(0, l, 2):
        s = sign(cur_y)
        r1 = cur_y - int(cur_y)
        r2 = 1 - r1
        if change:
            alpha[i] = imax * r2
            points[i] = [int(cur_y), cur_x]
            alpha[i + 1] = imax * r1
            points[i + 1] = [int(cur_y) + s, cur_x]
        else:
            alpha[i] = imax * r2
            points[i] = [cur_x, int(cur_y)]
            alpha[i + 1] = imax * r1
            points[i + 1] = [cur_x, int(cur_y) + s]
        cur_y += grad
        cur_x += 1
    return points, alpha

def sign(n):
    return 1 if n >= 0 else -1