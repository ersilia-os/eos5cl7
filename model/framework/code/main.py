# imports
import os
import csv
import sys
import lazyqsar as lq

from chemprop import featurizers, nn
from chemprop.data import BatchMolGraph
from chemprop.nn import RegressionFFN
from chemprop.models import MPNN
import torch
from chemeleon_fingerprint import CheMeleonFingerprint

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.abspath(os.path.join(root, "..", "..", "checkpoints", "CheMeleon_LQ_model"))

def my_model(smiles_list):
    # Chemeleon embeddings
    chemeleon_fingerprint = CheMeleonFingerprint()
    X = chemeleon_fingerprint(smiles_list)
    # Predictions
    model =lq.LazyBinaryClassifier.load_model(model_path)
    y_pred = model.predict_proba(X)[:,1]
    return y_pred

# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

outputs = my_model(smiles_list)

#check input and output have the same lenght
input_len = len(smiles_list)
output_len = len(outputs)
assert input_len == output_len

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["ngonorrhoeae_inhibition_probability"])  # header
    for o in outputs:
        writer.writerow([o])
