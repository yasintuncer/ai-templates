import torch
from   torch import random
import onnx
#import the pytorch model you want to convert

model = #load model

device = 'cuda' # select device


model.eval().to(device)
model.load_state_dict(torch.load(#model weights ,torch.device(device)))
inputshape = #input shape
input = torch.rand(inputshape, dtype= torch.float)
input = input.uniform_(0,1)
input = input.to(device)

torch.onnx.export(model,input,"output.onnx", export_params=True, opset_version=11,training=False, verbose=True)

model = onnx.load("output.onnx")
onnx.checker.check_model(model)
print(onnx.helper.printable_graph(model.graph))
