#execution templates 
#bkz: https://docs.nvidia.com/deeplearning/tensorrt/quick-start-guide/index.html#conversion


/usr/src/tensorrt/bin/trtexec --onnx="$1" --saveEngine="$2" --explicitBatch --fp16 --workspace=3000