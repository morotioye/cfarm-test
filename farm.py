import string
import random
import os
from git import Repo

n = int(input("how many sequences? (3 commits per sequence) : "))

rd = "/Users/wnr/bai/cfarm"
ru = "https://github.com/seeohh/cfarm.git"

if not os.path.exists(rd):
    r = Repo.clone_from(ru, rd)
else:
    r = Repo(rd)
o = r.remotes.origin

for _ in range(n):
    l = string.ascii_lowercase
    mc = """{}""".format(''.join(random.choice(l) for i in range(200)))
    fn = "random_method.py"

    with open(fn, "w") as f:
        f.write(mc)

    o.pull()
    r.git.add(fn)
    r.git.commit('-m', 'hi')
    o.push()
    o.fetch()
    os.remove(os.path.join(rd, fn))
    r.git.add(fn)
    r.git.commit('-m', 'bai')
    o.push()

print("done.")
