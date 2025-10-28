# -*- coding: utf-8 -*-


"""
Python 3
19 / 05 / 2025
@author: z_tjona

"I find that I don't understand things unless I try to program them."
-Donald E. Knuth
"""


# ----------------------------- logging --------------------------
import logging
from sys import stdout
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s][%(levelname)s] %(message)s",
    stream=stdout,
    datefmt="%m-%d %H:%M:%S",
)
logging.info(__file__)
logging.info(datetime.now())

# ----------------------------- functions --------------------------
import keras
import os
import numpy as np


def load_model(model_path: str = "Blackbox/blackbox_S.keras") -> keras.Sequential:
    """Load a keras model from the specified path."""
    logging.debug(f"Loading model from {model_path}")
    print("Current working directory:", os.getcwd())
    return keras.models.load_model(model_path)  # type: ignore


def predict_point(model: keras.Sequential, x1: float, x2: float) -> float:
    """Predict the output for a single input."""
    assert isinstance(x1, (int, float)), "x1 must be a number"
    assert isinstance(x2, (int, float)), "x2 must be a number"
    return model.predict(np.array([[x1, x2]], dtype=np.float32)).round()[0][0]
    # return model.predict(np.array([[x1, x2]], dtype=np.float32)) # probs


def predict_batch(model: keras.Sequential, x1s: list, x2s: list) -> list:
    """Predict the output for a batch of inputs."""
    assert isinstance(x1s, list), "x1 must be a list"
    assert isinstance(x2s, list), "x2 must be a list"
    return (
        model.predict(np.array([x1s, x2s], dtype=np.float32).T)
        .round()
        .flatten()
        .tolist()
    )
    # return model.predict(np.array([x1s, x2s], dtype=np.float32).T).flatten().tolist() # probs
