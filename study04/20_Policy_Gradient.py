import numpy as np
import gym
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras import backend as K

# 1. 환경 설정
env = gym.make('CartPole-v1')
n_actions = env.action_space.n
n_states = env.observation_space.shape[0]

# 2. 정책 신경망 모델 정의
class PolicyNetwork:
    def __init__(self, state_size, action_size, learning_rate=0.001):
        self.state_size = state_size
        self.action_size = action_size
        self.learning_rate = learning_rate
        self.model = self.create_model()
        self.optimizer = Adam(learning_rate=self.learning_rate)
    
    def create_model(self):
        model = Sequential()
        model.add(Dense(24, input_shape=(self.state_size,), activation='relu'))
        model.add(Dense(24, activation='relu'))
        model.add(Dense(self.action_size, activation='softmax'))
        model.compile(optimizer=self.optimizer, loss=self.ppo_loss)
        return model

    def ppo_loss(self, y_true, y_pred):
        y_true = K.clip(y_true, 1e-10, 1. - 1e-10)
        return -K.sum(y_true * K.log(y_pred), axis=-1)

    def predict(self, state):
        state = np.expand_dims(state, axis=0)
        return self.model.predict(state)[0]
    
    def train(self, states, actions, rewards):
        n = len(states)
        states = np.array(states)
        actions = np.array(actions)
        rewards = np.array(rewards)
        
        # Compute discounted rewards
        discounted_rewards = np.zeros_like(rewards)
        cumulative = 0
        for t in reversed(range(len(rewards))):
            cumulative = cumulative * 0.99 + rewards[t]
            discounted_rewards[t] = cumulative

        # Normalize rewards
        discounted_rewards = (discounted_rewards - np.mean(discounted_rewards)) / (np.std(discounted_rewards) + 1e-10)

        # Create target values
        actions_one_hot = np.eye(self.action_size)[actions]
        self.model.fit(states, actions_one_hot, sample_weight=discounted_rewards, verbose=0)

# 3. REINFORCE 알고리즘 구현
def reinforce(env, policy_network, n_episodes=1000):
    for episode in range(n_episodes):
        state = env.reset()
        state = np.reshape(state, [1, n_states])
        done = False
        total_reward = 0
        
        states, actions, rewards = [], [], []
        
        while not done:
            action_probs = policy_network.predict(state)
            action = np.random.choice(n_actions, p=action_probs)
            
            next_state, reward, done, _ = env.step(action)
            next_state = np.reshape(next_state, [1, n_states])
            
            states.append(state)
            actions.append(action)
            rewards.append(reward)
            
            state = next_state
            total_reward += reward
        
        policy_network.train(states, actions, rewards)
        
        print(f"Episode {episode + 1}/{n_episodes}, Total Reward: {total_reward:.2f}")

# 4. 에이전트 학습 및 결과 평가
policy_network = PolicyNetwork(state_size=n_states, action_size=n_actions)
reinforce(env, policy_network)

# 환경 종료
env.close()
