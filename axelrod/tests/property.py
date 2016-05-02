"""
A module for creating hypothesis based strategies for property based testing
"""
import axelrod
from hypothesis.strategies import composite, tuples, sampled_from, integers, floats, random_module


# For purposes of seeding need to use deterministic strategies
non_stochastic_strategies = [s for s in axelrod.strategies if not s().classifier['stochastic']]

@composite
def matches(draw, players=non_stochastic_strategies, min_turns=1,
            max_turns=200, min_noise=0, max_noise=1):
    strategies = draw(tuples(sampled_from(players), sampled_from(players)))
    players = [s() for s in strategies]
    turns = draw(integers(min_value=min_turns, max_value=max_turns))
    noise = draw(floats(min_value=min_noise, max_value=max_noise))
    match = axelrod.Match(players, turns=turns, noise=noise)
    return match


