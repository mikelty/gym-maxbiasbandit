from gym.envs.registration import register

register(
    id='maxbiasbandit-v0',
    entry_point='gym_foo.envs:FooEnv',
)