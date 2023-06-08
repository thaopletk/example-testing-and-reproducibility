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

- Can you run the test cases, as described above? Yes

- Is the model reproducible? @_@ 

- Are the test cases sensible? Hmmm

- Are the test cases comprehensive? Is this a trick question? Probably not comprehensive [what edge cases?]

## Exercises

- [x] Use [GitHub Actions](https://docs.github.com/en/actions) to run the test cases every time you push a new commit.

**Notes**: Set up requirements.txt; annoyingly, Python 3.10 does not load numpy properly, but version 3.9 works. See `python-app.yml` in the `.github\workflows` folder.

- [ ] Define a reproducible environment in which the model can run.

**Notes**: Since I already set up a requirements.txt file, I guess I'm going with Python virtualenv... -- Unless this question is asking something about containers/docker / ??? 

`python -m venv .venv`

`.venv\Scripts\activate.bat`

`pip install -r requirements.txt`

Is that a reproducible environment???? does the set up in the github actions consistute a reproducible environment?


- [ ] Update the model so that its outputs can be reproduced.

**Notes**: Is this about...random number generation and setting up a seed? 

- [ ] Write test cases that check if the model outputs are reproducible.

**Notes**: Then, getting the same series of random numbers?

- [ ] Use [pytest](https://docs.pytest.org/) (Python) or [testthat](https://testthat.r-lib.org/) (R) to run the test cases.


