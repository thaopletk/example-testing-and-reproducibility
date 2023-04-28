"""Test cases for the model defined in model.py."""

import numpy as np
from model import run_model


# Run the model.
model_output = run_model()

# Is the output mean close to the expected mean?
expected_mean = 10
model_mean = np.mean(model_output)
mean_abs_error = np.abs(model_mean - expected_mean)
if mean_abs_error > 0.2:
    raise ValueError(f'Sample mean has error {mean_abs_error}')

# Is the output standard deviation close to the expected standard deviation?
expected_sd = 1
model_sd = np.std(model_output)
sd_abs_error = np.abs(model_sd - expected_sd)
if sd_abs_error > 0.15:
    raise ValueError(f'Sample sd has error {sd_abs_error}')
