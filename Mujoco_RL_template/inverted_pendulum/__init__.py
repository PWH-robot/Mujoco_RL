from gym.envs.registration import register

register(
    id='inverted_pendulum-v0',
    entry_point='inverted_pendulum.envs:Inverted_pendulum',
)