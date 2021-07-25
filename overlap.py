testlist1 = [[572.994798731525, 589.533307081074], [980.955440528633, 991.175758850295], [2913.28090480674, 2945.26662743359], [3598.1017545957, 3623.03329631861], [3687.02956902969, 3710.49374436116], [3797.16035036894, 3805.92316962196], [3914.83167613624, 3927.97590501577], [3987.85209300433, 4008.29177474545], [4060.77892945614, 4065.74728563923], [4211.61018926417, 4224.8667783034]]
testlist2 = [[577.354418970819, 605.164482581487], [2929.4346032273, 2948.26159096649], [3602.40082220593, 3629.79447291512], [3690.02339096926, 3704.66762928106], [3798.82856452459, 3815.90794539923], [3888.10924960999, 3936.83711865265], [3977.12596208323, 4006.71873126086], [4059.70542286942, 4080.16591415182], [4209.37757224869, 4223.10447673127]]
testlist3 = [[584.527455464588, 600.820793904481], [2929.43466714205, 2946.97176447458], [3602.40082220593, 3608.70566207031], [3690.02339096926, 3696.41448949697], [3798.63768979395, 3806.12500543054], [3911.660729378, 3925.39368151594], [3989.38646928919, 3998.93030604674], [4059.70542286942, 4068.23548160959], [4209.37757224869, 4217.62243629387], [4251.16050485149, 4262.54633011343]]
testlist4 = [[779.430093629126, 807.433317026444], [2900.92224214284, 2945.26662743359], [3573.58177572401, 3703.65409815306], [3786.56475547992, 3815.53935314732], [3884.91077038168, 4075.00251613033], [4198.36283094628, 4224.8667783034]]
testlist5 = [[2899.75016432628, 2916.43978334125], [2929.06798469456, 2944.3235023538], [3602.40082220593, 3630.94766530348], [3690.02339096926, 3704.35092311865], [3798.2807689585, 3815.3722452611], [3888.10924960999, 3938.45502561098], [3977.07248807792, 3998.93030604674], [4056.666802252, 4070.79999151727], [4183.85455683246, 4200.34810449462], [4210.95194334281, 4224.37436706532]]

test_lists = [testlist1, testlist2, testlist3, testlist4, testlist5]
test_lists.sort(key=lambda x: x[0][0])
testlist1 = test_lists[0]
testlist2 = test_lists[1]
testlist3 = test_lists[2]
testlist4 = test_lists[3]
testlist5 = test_lists[4]

nums = []
for i in range(len(test_lists)):
    for j in range(len(test_lists[i])):
        nums.append(test_lists[i][j][0])
        nums.append(test_lists[i][j][1])

nums = sorted(list(set(nums)))

overlap = []
for i in range(len(nums)-1):
    overlap.append([nums[i], nums[i+1]])

overlap_count = [0 for i in overlap]

for i in range(len(test_lists)):
    for j in range(len(test_lists[i])):
        start = test_lists[i][j][0]
        end = test_lists[i][j][1]
        for k in range(len(overlap)):
            if start <= overlap[k][0] and overlap[k][1] <= end:
                overlap_count[k] += 1

result = []
result_count = []
for i in range(len(overlap_count)):
    if overlap_count[i] >= 3:
        result.append(overlap[i])
        result_count.append(overlap_count[i])

print(result)

stitch = []
for i in range(len(result)):
    if result[i][0] in stitch:
        stitch.remove(result[i][0])
        stitch.append(result[i][1])
    else:
        stitch.append(result[i][0])
        stitch.append(result[i][1])


final = []

for i in range(0, len(stitch), 2):
    final.append([stitch[i], stitch[i+1]])

print(final)



