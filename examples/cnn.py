import argparse
import os
from pathlib import Path

import torch
from torch import nn

from bragghls.ir.nn import set_weights, compile_nn_module_to_mlir


class DoubleCNN(nn.Module):
    def __init__(self, scale):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(1, 16 * scale, 3)
        self.conv2_1 = torch.nn.Conv2d(16 * scale, 8 * scale, 1)
        self.conv2_2 = torch.nn.Conv2d(16 * scale, 8 * scale, 1)
        self.conv2_3 = torch.nn.Conv2d(16 * scale, 8 * scale, 1)
        self.conv3 = torch.nn.Conv2d(8 * scale, 16 * scale, 1)
        self.conv4 = torch.nn.Conv2d(16 * scale, 8 * scale, 3)

    def forward(self, x):
        y = self.conv1(x)
        z = self.conv2_1(y)
        w = self.conv2_2(y)
        u = self.conv2_3(y)
        uuu = z + w + u
        uu = self.conv3(uuu)
        return uu.sum()


class ConvPlusReLU(nn.Module):
    def __init__(self, in_channels, out_channels, bias=True):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(in_channels, out_channels, 3, bias=bias)
        self.conv2 = torch.nn.Conv2d(out_channels, in_channels, 3, bias=bias)
        self.relu = torch.nn.ReLU()

    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x).sum()
        return x


def make_single_small_cnn(
    in_channels=2, out_channels=8, img_size=11, simplify_weights=False, bias=True
):
    with torch.no_grad():
        mod = ConvPlusReLU(in_channels, out_channels, bias)
        mod.eval()
        if simplify_weights:
            mod.apply(set_weights)

    mlir_module = compile_nn_module_to_mlir(
        mod,
        [
            ([1, in_channels, img_size, img_size], torch.float32),
        ],
    )
    return str(mlir_module)


def make_double_small_cnn(scale=1, img_size=11, simplify_weights=False):
    with torch.no_grad():
        mod = DoubleCNN(scale)
        mod.eval()
        t = torch.randn((1, 1, img_size, img_size))
        y = mod(t)
        if simplify_weights:
            mod.apply(set_weights)

    mlir_module = compile_nn_module_to_mlir(
        mod,
        [
            ([1, 1, img_size, img_size], torch.float32),
        ],
    )
    return str(mlir_module)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="make stuff")
    parser.add_argument(
        "--out_dir",
        type=Path,
        default=Path(__file__).parent / "double_cnn_bragghls_artifacts",
    )
    parser.add_argument("--size", type=int, default=5)
    args = parser.parse_args()
    args.out_dir = args.out_dir.resolve()

    dot_str = make_double_small_cnn(img_size=args.size)
    os.makedirs(f"{args.out_dir}", exist_ok=True)
    open(f"{args.out_dir}/double_cnn.mlir", "w").write(dot_str)
