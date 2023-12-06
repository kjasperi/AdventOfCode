# times = [7,  15,   30]
# distances = [9,  40,  200]

times = [55 ,    82,     64,     90]
distances = [246,   1441,   1012,   1111]

scores = 1
for idx, time in enumerate(times):
    record = distances[idx]
    # print(time, record)
    score = 0
    distance = 0
    for vel in range(time):
        dist = (time - vel) * vel
        # print(dist)
        if dist > record:
            score += 1

        
    scores *= score
print(scores)
    
    
