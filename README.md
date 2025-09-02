# Growth Inhibitors of Neisseria gonorrhoeae

The authors curated a dataset of 282 compounds from ChEMBL, of which 160 (56.7%) were labeled as active N. gonorrhoeae inhibitor compounds. They used this dataset to build a naïve Bayesian model and used it to screen a commercial library. With this method, they identified and validated two hits. We have used the dataset to build a model using LazyQSAR with CheMeleon Embeddings as molecular descriptors, with AUROC of 0.86 (5-fold crossvalidation).

This model was incorporated on 2024-01-03.Last packaged on 2025-08-27.

## Information
### Identifiers
- **Ersilia Identifier:** `eos5cl7`
- **Slug:** `ngonorrhoeae-inhibition`

### Domain
- **Task:** `Annotation`
- **Subtask:** `Activity prediction`
- **Biomedical Area:** `Gonorrhea`
- **Target Organism:** `Neisseria gonorrhoeae`
- **Tags:** `Antimicrobial activity`, `ChEMBL`, `N.gonorrhoeae`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `1`
- **Output Consistency:** `Fixed`
- **Interpretation:** Probability of activity for the inhibition of the pathogen N. gonorrhoeae

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| ngonorrhoeae_inhibition_probability | float | high | Predicted probability of inhibiting the growth of Neisseria gonorrhoeae |


### Source and Deployment
- **Source:** `Local`
- **Source Type:** `Internal`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos5cl7](https://hub.docker.com/r/ersiliaos/eos5cl7)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos5cl7.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos5cl7.zip)

### Resource Consumption
- **Model Size (Mb):** `82`
- **Environment Size (Mb):** `7865`
- **Image Size (Mb):** `8111.46`

**Computational Performance (seconds):**
- 10 inputs: `32.39`
- 100 inputs: `24.23`
- 10000 inputs: `396.03`

### References
- **Source Code**: [https://github.com/ersilia-os/lazy-qsar](https://github.com/ersilia-os/lazy-qsar)
- **Publication**: [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8274436/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8274436/)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2020`
- **Ersilia Contributor:** [Richiio](https://github.com/Richiio)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [GPL-3.0-only](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos5cl7
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos5cl7
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
