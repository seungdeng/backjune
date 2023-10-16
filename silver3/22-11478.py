S = input()

result = set()

for i in range(1,len(S)+1):
    for j in range(len(S)-i+1):
        result.add(S[j:j+i])

print(len(result))
# # idx = 0
# # len = len(S)+1
# result = set()

# for i in range(len(S)):
#     if idx != len(S):
#         for k in range(1,len):
#             result.add(S[idx:])


# s = input()
# subset = set()
# for i in range(1, len(s)+1):
#     for j in range(len(s)-i+1):
#         subset.add(s[j:j+i])
# print(len(subset))