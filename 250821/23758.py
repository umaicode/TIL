import heapq

pq = []
lst = [("BHC", 2), ("NeNe", 1), ("KFC", 3), ("BBQ", 1), ("Moms", 2), ("Mc", 4)]

for brand, length in lst:
    heapq.heappush(pq, (length, brand, length))

while len(pq):
    if len(pq) == 1:
        result = heapq.heappop(pq)
        print(f"{result[1]} {result[2]}")
        break

    idx_1, brand_1, len_1 = heapq.heappop(pq)
    idx_2, brand_2, len_2 = heapq.heappop(pq)

    temp_brand = [brand_1, brand_2]
    temp_brand = sorted(temp_brand)

    temp = (idx_1 + idx_2, temp_brand[0], len_1 + len_2)
    heapq.heappush(pq, temp)
    temp_brand.clear()
