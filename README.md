# Growth Inhibitors of Neisseria gonorrhoeae

The authors curated a dataset of 282 compounds from ChEMBL, of which 160 (56.7%) were labeled as active N. gonorrhoeae inhibitor compounds. They used this dataset to build a naïve Bayesian model and used it to screen a commercial library. With this method,they identified and validated two hits. We have used the dataset to build a model using Ersilia’s set of AI modeling tools.

## Identifiers

* EOS model ID: `eos5cl7`
* Slug: `ngonorrhoeae-inh`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Classification`
* Output: `Probability`
* Output Type: `Float`
* Output Shape: `Single`
* Interpretation: Probability of activity for the inhibition of the Antimicrobial pathogen N. gonorrhoeae

## References

* [Publication](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8274436/)
* [Source Code](https://github.com/ersilia-os/lazy-qsar)
* Ersilia contributor: [Richiio](https://github.com/Richiio)

## Ersilia model URLs
* [GitHub](https://github.com/ersilia-os/eos5cl7)

## Citation

If you use this model, please cite the [original authors](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8274436/) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a GPL-3.0 license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!