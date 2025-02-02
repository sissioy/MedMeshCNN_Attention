import torch
import torch.nn as nn


class Transformer(nn.Module):
    def __init__(
        self,
        # input
        num_layers=6,
        model_dim=512,
        num_heads=8,
        ffn_dim=2048,
        dropout=0.2,
    ):
        super(Transformer, self).__init__()
        self.encoder = Encoder(            
            num_layers,
            model_dim,
            num_heads,
            ffn_dim,
            dropout,)
        self.decoder = Decoder(            
            num_layers,
            model_dim,
            num_heads,
            ffn_dim,
            dropout,)
        self.linear = nn.Linear(model_dim,)
        self.softmax = nn.Softmax(dim=2)

    def forward(self,):
        context_attn_mask = padding_mask(tgt_seq, src_seq)
        output, enc_self_attn = self.encoder(src_seq, src_len)
        output, dec_self_attn, ctx_attn = self.decoder(
            tgt_seq, tgt_len, output, context_attn_mask
        )

        output = self.linear(output)
        output = self.softmax(output)

        return output, enc_self_attn, dec_self_attn, ctx_attn