import math

P = [1750, 2625, 3500, 10000]
n = [8500, 5000, 6000, 500]
C = [8500000, 6000000, 13800000, 1750000]
k = 4

total_revenue = 0
total_cost = 0

for i in range(k):
    revenue = P[i] * n[i]
    cost = C[i]
    pf = revenue - cost
    n_min = math.ceil(C[i] / P[i])

    total_revenue += revenue
    total_cost += cost

    print(f"โซนที่ {i+1}:ถ้าราคาตั๋ว {P[i]} บาท และต้นทุน {cost} บาท จะต้องขายมากกว่า {n_min} ใบ จึงจะมีกำไร")
    print(f"ขาย {n[i]} ใบ รายได้: {revenue} บาท, ต้นทุน: {cost} บาท, กำไร: {pf} บาท\n")

total_pf = total_revenue - total_cost
print("สรุปรวมทั้งหมด:")
print(f"รายได้รวม: {total_revenue} บาท")
print(f"ต้นทุนรวม: {total_cost} บาท")
print(f"กำไรสุทธิ: {total_pf} บาท")
