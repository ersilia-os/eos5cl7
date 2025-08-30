# imports
import os
import csv
import sys
import lazyqsar

input_file = sys.argv[1]
output_file = sys.argv[2]

root = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.abspath(os.path.join(root, "..", "..", "checkpoints", "model"))

with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

def predict(smiles_list, model_path):
    model = lazyqsar.LazyBinaryClassifier.load_model(model_path)
    chemeleon = lazyqsar.descriptors.ChemeleonDescriptor()
    X = chemeleon.transform(smiles_list)
    y_hat = model.predict_proba(X=X)[:,1]
    return y_hat


outputs = predict(smiles_list, model_path)

input_len = len(smiles_list)
output_len = len(outputs)
assert input_len == output_len

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["ngonorrhoeae_inhibition_probability"])
    for o in outputs:
        writer.writerow([o])
