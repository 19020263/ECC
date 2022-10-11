from math import sqrt

def count_point(a, b, p):
    """
        Input: a,b,p
        Output: points | danh sách các điểm trên đương cong E
    """
    points = []
    num = 0
    for x in range(0, p):
        y2 = x ** 3 + a * x + b
        y2mod = y2 % p
        # Kiểm tra điều kiện 1 điểm có thuộc đường cong hay ko
        if int(sqrt(y2)) ** 2 == y2 or int(sqrt(y2mod)) ** 2 == y2mod:
            num += 1
            if int(sqrt(y2)) ** 2 == y2:
                points.append({
                    'x': x,
                    'y': int(sqrt(y2)) % p
                })
                # kiểm tra nếu y ^ 2 = 0 thì chỉ có 1 điểm duy nhất
                if int(sqrt(y2)) % p != 0:
                    points.append({
                        'x': x,
                        'y': (p - int(sqrt(y2))) % p
                    })
                    num += 1
            elif int(sqrt(y2mod)) ** 2 == y2mod:
                points.append({
                    'x': x,
                    'y': int(sqrt(y2mod)) % p
                })
                if int(sqrt(y2mod))  % p != 0:
                    points.append({
                        'x': x,
                        'y': (p - int(sqrt(y2mod))) % p
                    })
                    num += 1     
    return points

def inverse(a, m):
    """
        Input: a,m | tham số a và số mod m
        Output: Nghịch đảo chia lấy phần dư của a cho m
    """

    # Khai báo tham số ban đầu
    r0,r1 = a,m
    s0,s1 = 1,0

    # Vòng lặp tìm nghịch đảo chia lấy phần dư, vòng lặp kết thúc khi r(Kết qảu của phép chia dư) bằng 0
    while(True):
        q = r0 // r1
        r = r0 % r1
        if r == 0:
            return s
        s = s0 - q * s1
        r0 = r1
        r1 = r
        s0 = s1
        s1 = s

def compute_x3(x1, x2, lamb, p):
    """Hàm tính x3"""
    x3 = lamb ** 2 - x1 - x2   
    return x3 % p

def compute_y3(x3, x1, y1, lamb, p):
    """Hàm tính y3"""
    y3 = lamb * (x1 - x3) - y1
    return y3 % p

def compute_lambda(a,x1,y1,x2,y2,p):
    """Hàm tính lambda theo 3 case"""
    lamb = 0
    if (x1 == x2 and y1 == y2 and y1 == 0) or (x1 == x2 and y1 != y2):
        return 'INF'
    elif x1 != x2:
        lamb = (y2 - y1) * inverse(x2 - x1, p)
    elif x1 == x2 and y1 == y2:
        lamb = (3 * x1 ** 2 + a) * inverse(2 * y1, p)
    return lamb % p

def compute_group(a,x,y,p):
    """Hàm nhân 1 điểm trên E với 1 số thuộc Fp"""
    i = 1
    x_n,y_n = x,y
    print(f'{i}P:({x},{y})')
    # vòng lặp thực hiện phép cộng điểm , kết thúc khi rơi vào case 2
    while(True):
        i += 1
        lamb = compute_lambda(a,x,y,x_n,y_n,p)
        if lamb == 'INF':
            print(f'{i}P:(INF, INF)')
            break
        x3 = compute_x3(x, x_n, lamb, p)
        y3 = compute_y3(x3, x, y, lamb, p)
        print(f'{i}P:({x3},{y3})')
        x_n,y_n = x3,y3

def check_prime(p):
    """Hàm kiểm tra số nguyên tố"""
    if p > 1:
        arr = [i for i in range(2,p)]
        if all(p % i != 0 for i in arr):
            return True
    return False

a = 1
b = 6
p = 7919
if check_prime(p):
    try:
        print(f"y ^ 2 = x ^ 3 + {a} * x + {b} mod {p}")
        points = count_point(a, b, p)
        print(points)
        print(f'Number of points: {len(points) + 1}')
        print()
        for point in points:
            print(f"P:({point.get('x')},{point.get('y')}):")
            compute_group(a,point.get('x'),point.get('y'),p)
            print()
    except Exception as e: 
        print(e)
        print('Error with p = ' + str(p))
else:
    print(f"{p} is not a prime number!")
