import torch
import torch.nn as nn
from torch.utils.data import Dataset
import test

class sin_fun(nn.Module):
    def __init__(self):
        super().__init__()
        self.relu = nn.ReLU()

    def forward(self, input):
        return self.relu(input) / input * torch.abs(torch.sin(input))


class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        self.l1 = nn.Linear(input_size, hidden_size)
        self.fun_act = sin_fun()
        self.l2 = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        out = self.l1(x)
        out = self.fun_act(out)
        out = self.l2(out)  # NOT USE SOFTMAX SINCE WE USE nn.CrossEntropyLoss
        return out


class Article_nn(nn.Module):
    def __init__(self, input_size):
        super(Article_nn, self).__init__()
        self.l1 = nn.Linear(input_size*2, 64)
        self.relu = nn.ReLU()
        self.l2 = nn.Linear(64, 1000)
        self.l3 = nn.Linear(1000, 1)


    def forward(self, x):
        out = self.relu(self.l1(x))
        out = self.relu(self.l2(out))
        out = self.l3(out)
        return out

class Article_nn2(nn.Module):
    def __init__(self, input_size):
        super(Article_nn, self).__init__()
        self.l1 = nn.Linear(input_size*2, 64)
        self.relu = nn.ReLU()
        self.leaky = nn.LeakyReLU()
        self.l2 = nn.Linear(64, 128)
        self.l3 = nn.Linear(128, 128)
        self.l4 = nn.Linear(128, 64)
        self.l5 = nn.Linear(64, 1)


    def forward(self, x):
        out = self.leaky(self.l1(x))
        out = self.leaky(self.l2(out))
        out = self.leaky(self.l3(out))
        out = self.leaky(self.l4(out))
        out = self.l5(out)
        return out


class NumbersDataset(Dataset):
    def __init__(self, samples, labels):
        self.samples = torch.from_numpy(samples).to(torch.float32)
        self.labels = torch.from_numpy(labels).to(torch.float32)

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        return self.samples[idx], self.labels[idx]

model = Article_nn(1)
x = torch.randn(64,2)
# print(x)

# test.make_dot(model(x), params=dict(list(model.named_parameters()))).render("rnn_torchviz", format="png")