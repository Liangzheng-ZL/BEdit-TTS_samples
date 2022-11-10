#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright 2019 Shigeki Karita
#  Apache 2.0  (http://www.apache.org/licenses/LICENSE-2.0)

"""Positionwise feed forward layer definition."""

import torch
############## zl modified: add gelu #################
from espnet.nets.pytorch_backend.transformer.gelu import GELU
######################################################


class PositionwiseFeedForward(torch.nn.Module):
    """Positionwise feed forward layer.

    :param int idim: input dimenstion
    :param int hidden_units: number of hidden units
    :param float dropout_rate: dropout rate

    """
    ################## zl modified: add gelu #################
    #def __init__(self, idim, hidden_units, dropout_rate):
    def __init__(self, idim, hidden_units, dropout_rate, activation=None):
    ##########################################################
        """Construct an PositionwiseFeedForward object."""
        super(PositionwiseFeedForward, self).__init__()
        self.w_1 = torch.nn.Linear(idim, hidden_units)
        self.w_2 = torch.nn.Linear(hidden_units, idim)
        self.dropout = torch.nn.Dropout(dropout_rate)
        ############## zl modified: add gelu ##############
        if activation=="gelu":
            self.activation = GELU()
        else:
            self.activation = torch.nn.ReLU()
        ###################################################

    def forward(self, x):
        """Forward funciton."""
        return self.w_2(self.dropout(self.activation(self.w_1(x))))
