num_rows = 5
num_cols = 4
row_inc = 24

idx = []

for i in range(num_rows * num_cols):
    idx.append(i//num_cols*row_inc + i%num_cols)

ls = [f"tag_{i}" for i in idx]
print("====== Solo ======")
print(f"tag_names: [{', '.join(ls)}]")
for el in idx: 
    print(f"""tag_{el}:
  id: {el}
  size: 0.03""")

print("====== Bundles ======")

bundle = {}
for i in range(3):
    ids = []
    for el in idx[i * 6:i * 6 + 6]:
        ids.append(el)
    print(ids)
    tmp = "".join([str(el) + ':\n\tsize: 0.03\n' for el in ids])
    bundle[f"bundle_{i}"] = f"""bundle_{i}:
  layout:
    ids: [{', '.join(map(str, ids))}]\n
    {tmp}
"""
print(f"bundle_names: {list(bundle.keys())}")
print(f"{list(bundle.values())}")
    #   bundle_names: ["bundle_0"]
    #   bundle_0:
    #     layout:
    #       ids: [1]
    #       1:
    #         size: 0.03
