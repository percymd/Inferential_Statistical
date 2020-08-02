
import random

def estimate_pi(n):
    number_point_circle = 0
    number_point_total = 0
    for _ in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = x**2 + y**2
        if distance <= 1:
            number_point_circle +=1
        number_point_total += 1

    return 4 * number_point_circle/number_point_total

if __name__ =='__main__':
    
    n = int(input(f'Numbers of trys: '))
    print(estimate_pi(n))