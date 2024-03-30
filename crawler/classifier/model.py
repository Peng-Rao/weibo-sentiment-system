from typing import Tuple, Dict

import torch
from torch import nn
import gensim
from classifier.helper import collate_fn
from classifier.utils import processing
import os


# 定义网络结构
class LSTM(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers):
        super(LSTM, self).__init__()
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True, bidirectional=True)
        self.fc = nn.Linear(hidden_size * 2, 1)  # 双向, 输出维度要*2
        self.sigmoid = nn.Sigmoid()

    def forward(self, x, lengths):
        h0 = torch.zeros(self.num_layers * 2, x.size(0), self.hidden_size).to(self.device)  # 双向, 第一个维度要*2
        c0 = torch.zeros(self.num_layers * 2, x.size(0), self.hidden_size).to(self.device)

        packed_input = torch.nn.utils.rnn.pack_padded_sequence(input=x, lengths=lengths, batch_first=True)
        packed_out, (h_n, h_c) = self.lstm(packed_input, (h0, c0))

        lstm_out = torch.cat([h_n[-2], h_n[-1]], 1)  # 双向, 所以要将最后两维拼接, 得到的就是最后一个time step的输出
        out = self.fc(lstm_out)
        out = self.sigmoid(out)
        return out


class LstmClassifier:
    def __init__(self):
        # 输入维度
        embed_size = 100
        # 隐藏层维度
        hidden_size = 256
        # LSTM层数
        num_layers = 2
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        self.classifier: LSTM = LSTM(embed_size, hidden_size, num_layers)
        print(os.getcwd())
        self.classifier.load_state_dict(torch.load("classifier/models/02_lstm_model.pth", map_location=self.device))
        self.word2vec = gensim.models.Word2Vec.load("classifier/models/word2vec.model")

    def predict(self, text: str) -> Tuple[Dict[str, float], str, float]:
        """
        执行预测
        :param text: 用户输入的文本
        :return: 预测结果
        """
        strs = [text]
        data = []

        for s in strs:
            vectors = []
            for w in processing(s).split(" "):
                if w in self.word2vec.wv.key_to_index:
                    vectors.append(self.word2vec.wv[w])
            vectors = torch.Tensor(vectors).to(self.device)
            data.append(vectors)
        x, _, lengths = collate_fn(list(zip(data, [-1] * len(strs))))

        with torch.inference_mode():
            x = x.to(self.device)
            probabilities = self.classifier(x, lengths)
            probabilities = torch.round(probabilities).squeeze()
            sentiment = "positive" if probabilities.item() > 0.5 else "negative"
            confidence = probabilities.item()
        return {"positive": confidence, "negative": 1 - confidence}, sentiment, confidence


def get_classifier() -> LstmClassifier:
    return LstmClassifier()
