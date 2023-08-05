import numpy as np


def parity(bitstring):
    """Returns 1 if parity of `bitstring` is even, otherwise 0."""
    hamming_weight = sum(int(k) for k in list(bitstring))
    return (hamming_weight + 1) % 2


def label_probability(results: dict):
    """Converts a dict of bitstrings and their counts,
    to parities and their counts"""
    shots = sum(results.values())
    probabilities = {0: 0, 1: 0}
    for bitstring, counts in results.items():
        label = parity(bitstring)
        probabilities[label] += counts / shots
    return probabilities


def cross_entropy_loss(classification, expected):
    """Calculate accuracy of predictions using cross entropy loss.
    Args:
        classification (dict): Dict where keys are possible classes,
                               and values are the probability our
                               circuit chooses that class.
        expected (int): Correct classification of the data point.

    Returns:
        float: Cross entropy loss
    """
    p = classification.get(expected)  # Prob. of correct classification
    return -np.log(p + 1e-10)


class OptimizerLog:
    """
    Log to store optimizer's intermediate results
    """

    def __init__(self):
        self.evaluations = []
        self.parameters = []
        self.costs = []

    def update(self, evaluation, parameter, cost, _stepsize, _accept):
        """
        Save intermediate results. Optimizer passes five values,
        but we ignore the last two.
        """
        self.evaluations.append(evaluation)
        self.parameters.append(parameter)
        self.costs.append(cost)


class LinearClassifier:

    def __init__(self, dimension):
        self.weights = None
        self.bias = None

    def classify(self, x):
        """Classify a data point using the current weights"""
        estimate = np.inner(self.weights, x) + self.bias
        return np.sign(estimate)

    def set_weights(self, weights):
        """Set the weights of the classifier"""
        self.weights = weights[:-1]
        self.bias = weights[-1]


