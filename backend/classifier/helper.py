from typing import Tuple, List

import torch
from torch.nn.utils.rnn import pad_sequence


def collate_fn(data):
    """
    :param data: 第0维：data，第1维：label
    :return: 序列化的data、记录实际长度的序列、以及label列表
    """
    data.sort(key=lambda i: len(i[0]), reverse=True)  # pack_padded_sequence要求要按照序列的长度倒序排列
    data_length = [len(sq[0]) for sq in data]
    x = [i[0] for i in data]
    y = [i[1] for i in data]
    data = pad_sequence(x, batch_first=True, padding_value=0)  # 用RNN处理变长序列的必要操作
    return data, torch.tensor(y, dtype=torch.float32), data_length
