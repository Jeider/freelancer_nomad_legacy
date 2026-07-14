items = [
    0.5,
    -0.002844238,
    1,
    -0.01111839,
    1.5,
    -0.02443459,
    2,
    -0.04240501,
    2.5,
    -0.06464177,
    3,
    -0.09075706,
    3.5,
    -0.120363,
    4,
    -0.1530717,
    4.5,
    -0.1884954,
    5,
    -0.2262462,
    5.5,
    -0.2659363,
    6,
    -0.3071777,
    6.5,
    -0.3495827,
    7,
    -0.3927634,
    7.5,
    -0.436332,
    8,
    -0.4799006,
    8.5,
    -0.5230812,
    9,
    -0.5654863,
    9.5,
    -0.6067277,
    10,
    -0.6464178,
    10.5,
    -0.6841685,
    11,
    -0.7195923,
    11.5,
    -0.7523009,
    12,
    -0.781907,
    12.5,
    -0.8080223,
    13,
    -0.830259,
    13.5,
    -0.8482294,
    14,
    -0.8615455,
    14.5,
    -0.8698198,
    15,
    -0.872664,
]

results = [
    0, 0,
]

i = 0
anims = []

for x in items:
    i += 1
    if i % 2 == 0:
        anims.append(x)

results += items
results.append(20)
results.append(-0.872664)

anims.reverse()
step = 0.5
time = 20

for an in anims:
    time += step
    results.append(time)
    results.append(an)


time += step
results.append(time)
results.append(0)


time += 5

results.append(time)
results.append(0)

for i in results:
    print(str(i).replace('.', ','))

# print(len(results) / 2)