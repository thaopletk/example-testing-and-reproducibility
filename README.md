# Example: Testing and Reproducibility

This repository is an example of how to begin testing models and ensuring that their outputs are reproducible.
It contains a simple stochastic model that draws samples from a normal distribution, and some tests that check whether the model outputs are consistent with our expectations.

This repository provides two versions of the model, so that you can work in your preferred language.

## Python model

The model is defined in `model.py`, and test cases are defined in `test.py`.
You can run the test cases by running the following command:

```sh
python3 test.py
```

## R Model

The model is defined in `model.R`, and test cases are defined in `test.R`.
You can run the test cases by running the following command:

```sh
R -s -f test.R
```

## License

The code is distributed under the terms of the [BSD 3-Clause license](https://opensource.org/licenses/BSD-3-Clause) (see
`LICENSE`).

## Questions

- Can you run the test cases, as described above?

- Is the model reproducible?

- Are the test cases sensible?

- Are the test cases comprehensive?

## Exercises

- [ ] Define a reproducible environment in which the model can run.

- [ ] Update the model so that its outputs can be reproduced.

- [ ] Write test cases that check if the model outputs are reproducible.

- [ ] Use [pytest](https://docs.pytest.org/) (Python) or [testthat](https://testthat.r-lib.org/) (R) to run the test cases.

- [ ] Use [GitHub Actions](https://docs.github.com/en/actions) to run the test cases every time you push a new commit.
