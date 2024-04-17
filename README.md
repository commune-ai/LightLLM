

## Setup

Clone the repo

```bash
git https://github.com/Big-Scale/LightLLM.git
cd lightllm
```

install dependencies

```bash
pip install -r requirements.txt
```

You are all set! 🎉

&nbsp;

## Use the model

To generate text predictions, you need to download the model weights. 
Run inference:

```bash
python generate.py --prompt "Hello, my name is"
```

This will run the 7B model and require ~26 GB of GPU memory (A100 GPU).

### Run LightLLM on consumer devices

On GPUs with `bfloat16` support, the `generate.py` script will automatically convert the weights and consume about ~14 GB.
For GPUs with less memory, or ones that don't support `bfloat16`, enable quantization (`--quantize llm.int8`):


It is expected that you have downloaded the pretrained weights as described above.
The finetuning requires at least one GPU with ~24 GB memory (RTX 3090). Follow the instructions in the script to efficiently fit your GPU memory.
Note: For some GPU models you might need to set `torch.backends.cuda.enable_flash_sdp(False)` (see comments at the top of the script).

More details about each finetuning method and how you can apply it to your own data can be found in our technical how-to guides.
