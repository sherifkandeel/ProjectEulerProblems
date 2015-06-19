target = 200
coinSizes = [1, 2, 5, 10, 20, 50, 100, 200]
ways ={}
ways[0]=1

for i in range (0,len(coinSizes)):
    for j in range(coinSizes[i],target+1):
        ways[j] += ways[j - coinSizes[i]]

print ways
# for (int i = 0; i < coinSizes.Length; i++) {
#     for (int j = coinSizes[i]; j <= target; j++) {
#         ways[j] += ways[j - coinSizes[i]];
#     }
# }