import torch
import torch.optim as optim
from common.models.cnn import CNN
from common.utils.data_utils.py import preprocess_image, load_data

def train_model(data_path):
    model = CNN()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    criterion = nn.MSELoss()

    data = load_data(data_path)
    for epoch in range(10):  # Run for 10 epochs
        for state, action, reward, next_state in data:
            state = torch.tensor(state).float()
            action = torch.tensor(action).float()
            reward = torch.tensor(reward).float()
            next_state = torch.tensor(next_state).float()

            target = reward + 0.95 * torch.max(model(next_state))
            target_f = model(state)
            target_f[0][action] = target

            optimizer.zero_grad()
            loss = criterion(target_f, action)
            loss.backward()
            optimizer.step()
