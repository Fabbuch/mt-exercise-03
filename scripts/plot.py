#! /bin/env/python

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from sys import argv
import re

model_ppl = {}
# arguments should be paths to train logs
for logfile in argv[1:]:
    # check that logfile exists
    assert Path(logfile).exists()
    with open(logfile, "r") as f:
        ppls = list()
        for i, line in enumerate(f):
            # extract model name from log
            if i==1:
                match = re.search("cfg.name \: (.+)\n", line)
                model_name = match.group(1)
            # find evaluation result line
            if re.search("Evaluation result \(greedy\)", line) != None:
                # get perplexity value
                match = re.search("ppl:\s+(\d+\.\d+),", line)
                ppl_str = match.group(1)
                ppl = float(ppl_str)
                ppls.append(ppl)
        model_ppl[model_name] = ppls

df = pd.DataFrame(model_ppl)

# prints data as table
print(df.to_string())

# plot validation perplexity for each model
plt.figure(figsize=(10, 7))
plt.plot(df, label=df.columns)

plt.ylabel('Validation Perpexity')
plt.legend()

plt.show()