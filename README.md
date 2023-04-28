# Example: Testing and Reproducibility

This repository is an example of how to begin testing models and ensuring that their outputs are reproducible.
It contains a simple stochastic model that draws samples from a normal distribution, and some tests that check whether the model outputs are consistent with our expectations.

The model is defined in `model.py`, and test cases are defined in `test.py`.
You can run the test cases by running the following command:

```sh
python3 test.py
```

The code is distributed under the terms of the [BSD 3-Clause license](https://opensource.org/licenses/BSD-3-Clause) (see
`LICENSE`).
