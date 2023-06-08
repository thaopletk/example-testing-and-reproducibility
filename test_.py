"""Test cases for the model defined in model.py."""

import numpy as np
from model import run_model


def test_RNG():

    model_output_run = [10.05252847, 10.40854786,  9.80850703,  7.65836897, 12.22114217, 10.53031372, 11.55932282, 11.48300132,  9.14015438 ,11.64174397,  9.06265779, 10.59165298,11.11442702, 11.26099369,  9.40552957, 10.920113,    9.63041275,  9.86967634,
    10.5669279,  10.01739331,  9.52105681,  8.86441591,  8.84980998, 10.97879084,
    9.26492939 , 9.83993048, 10.34928244 ,10.29897026,  7.53308062, 10.7104941 ,
    9.90779641, 10.05042854 , 9.77454186 , 8.47080862 ,10.87022882 ,10.83090937,
    9.1092407 , 11.15255989 , 9.30930476 ,11.18554311, 10.6271051 ,  9.87376694,
    9.67512736,  9.65213965 , 8.94232567 ,10.84104334 , 9.81147448 , 8.97179512,
    8.28794234 , 8.04678099]

    # Run the model.
    model_output = run_model(seed = 666)

    # is the model output the same?
    assert np.allclose(model_output ,model_output_run)

def test_mean():
    # Run the model.
    model_output = run_model()

    # Is the output mean close to the expected mean?
    expected_mean = 10
    model_mean = np.mean(model_output)
    mean_abs_error = np.abs(model_mean - expected_mean)
    assert mean_abs_error <= 0.2
    
def test_sd():
    # Run the model.
    model_output = run_model()

    # # Is the output standard deviation close to the expected standard deviation?
    expected_sd = 1
    model_sd = np.std(model_output)
    sd_abs_error = np.abs(model_sd - expected_sd)
    assert sd_abs_error <= 0.15