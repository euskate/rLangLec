import numpy as np
import gym
import random
from collections import deque
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

# 1. 환경 설정
env = gym.make('CartPole-v1')
n_actions = env.action_space.n
n_states = env.observation_space.shape[0]

# 2. DQN 모델 정의
def create_model(input_shape, n_actions):
    model = Sequential()
    model.add(Dense(24, input_shape=(input_shape,), activation='relu'))
    model.add(Dense(24, activation='relu'))
    model.add(Dense(n_actions, activation='linear'))
    model.compile(optimizer=Adam(learning_rate=0.001), loss='mse')
    return model

# 3. DQN 알고리즘 구현
class DQNAgent:
    def __init__(self, state_size, action_size, gamma=0.99, epsilon=1.0, epsilon_min=0.01, epsilon_decay=0.995, batch_size=64, buffer_size=10000):
        self.state_size = state_size
        self.action_size = action_size
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_min = epsilon_min
        self.epsilon_decay = epsilon_decay
        self.batch_size = batch_size
        self.buffer_size = buffer_size
        self.memory = deque(maxlen=buffer_size)
        self.model = create_model(state_size, action_size)
        self.target_model = create_model(state_size, action_size)
        self.update_target_model()
    
    def update_target_model(self):
        self.target_model.set_weights(self.model.get_weights())

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))
    
    def act(self, state):
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_size)
        act_values = self.model.predict(np.expand_dims(state, axis=0))
        return np.argmax(act_values[0])
    
    def replay(self):
        if len(self.memory) < self.batch_size:
            return
        
        minibatch = random.sample(self.memory, self.batch_size)
        for state, action, reward, next_state, done in minibatch:
            target = reward
            if not done:
                target = reward + self.gamma * np.amax(self.target_model.predict(np.expand_dims(next_state, axis=0))[0])
            
            target_f = self.model.predict(np.expand_dims(state, axis=0))
            target_f[0][action] = target
            self.model.fit(np.expand_dims(state, axis=0), target_f, epochs=1, verbose=0)
        
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

# 4. 에이전트 학습 및 결과 평가
n_episodes = 1000
agent = DQNAgent(state_size=n_states, action_size=n_actions)

for e in range(n_episodes):
    state = env.reset()
    state = np.reshape(state, [1, n_states])
    done = False
    total_reward = 0
    
    while not done:
        action = agent.act(state)
        next_state, reward, done, _ = env.step(action)
        next_state = np.reshape(next_state, [1, n_states])
        agent.remember(state, action, reward, next_state, done)
        state = next_state
        total_reward += reward
        
        agent.replay()
    
    if (e + 1) % 100 == 0:
        agent.update_target_model()
        print(f"Episode {e + 1}/{n_episodes}, Total Reward: {total_reward:.2f}, Epsilon: {agent.
