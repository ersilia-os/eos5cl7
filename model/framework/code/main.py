# imports
import os
import csv
import sys
from rdkit import Chem
from rdkit.Chem.Descriptors import MolWt
from rdkit.Chem import AllChem, DataStructs
import joblib
import numpy as np 
import pandas as pd 

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.abspath(os.path.join(root, "..", "..", "checkpoints", "model_morgan.joblib"))

# my model
def _smi_to_fps(smiles):
    mols = [Chem.MolFromSmiles(str(smi)) for smi in smiles]
    fp = [AllChem.GetMorganFingerprintAsBitVect(mol, 3, nBits=2048) for mol in mols] # gets the vector
    return fp

def _load_model(model_path):
    mdl = joblib.load(model_path)
    return mdl

def predict(smiles, model):
    X = _smi_to_fps(smiles)
    mdl = _load_model(model)
    y_pred = mdl.predict_proba(X)
    return y_pred[:,1]

# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

# run model
outputs = predict(smiles_list, model_path)

#check input and output have the same lenght
input_len = len(smiles_list)
output_len = len(outputs)
assert input_len == output_len

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["value"])  # header
    for o in outputs:
        writer.writerow([o])
