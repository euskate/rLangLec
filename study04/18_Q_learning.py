import numpy as np
import gym
import random

# 1. 환경 설정
env = gym.make('Taxi-v3')  # OpenAI Gym의 Taxi-v3 환경
n_actions = env.action_space.n  # 가능한 행동의 수
n_states = env.observation_space.n  # 가능한 상태의 수

# 2. Q-러닝 알고리즘 구현
# Q 테이블 초기화
Q = np.zeros((n_states, n_actions))

# 학습 파라미터
learning_rate = 0.1
discount_factor = 0.99
epsilon = 1.0  # 탐색 비율
epsilon_min = 0.01
epsilon_decay = 0.995
n_episodes = 1000  # 에피소드 수

# 에피소드별 학습
for episode in range(n_episodes):
    state = env.reset()
    done = False
    total_reward = 0

    while not done:
        # Epsilon-greedy 정책
        if random.uniform(0, 1) < epsilon:
            action = env.action_space.sample()  # 탐색
        else:
            action = np.argmax(Q[state])  # 활용

        # 환경과 상호작용
        next_state, reward, done, _ = env.step(action)
        total_reward += reward

        # Q-값 업데이트
        best_next_action = np.argmax(Q[next_state])
        td_target = reward + discount_factor * Q[next_state, best_next_action]
        td_error = td_target - Q[state, action]
        Q[state, action] += learning_rate * td_error

        state = next_state

    # Epsilon 감소
    if epsilon > epsilon_min:
        epsilon *= epsilon_decay

    # 학습 진행 상황 출력
    if (episode + 1) % 100 == 0:
        print(f"Episode {episode + 1}/{n_episodes}, Total Reward: {total_reward:.2f}, Epsilon: {epsilon:.2f}")

# 3. 결과 평가
# 학습된 정책 평가
state = env.reset()
done = False
total_reward = 0

while not done:
    action = np.argmax(Q[state])
    next_state, reward, done, _ = env.step(action)
    total_reward += reward
    state = next_state

print(f"최종 총 보상: {total_reward:.2f}")

# 환경 종료
env.close()
