import pytest
import sys


@pytest.mark.skipif(sys.platform == "win32", reason="EmptyInitOnDevice on CPU not working for Windows.")
@pytest.mark.parametrize("model_size", ["7B", "13B", "30B", "65B"])
def test_config_identical(model_size, lit_llama):
    import torch.nn as nn
    import llama_model.adapter as llama_adapter
    from llama_model.adapter_v2 import adapter_v2_linear_with_bias_and_scale
    import llama_model.model as llama
    from llama_model.utils import EmptyInitOnDevice

    with EmptyInitOnDevice():
        llama_model = llama.LLaMA.from_name(model_size)
        adapter_model = llama_adapter.LLaMA.from_name(model_size)

        for module in adapter_model.modules():
            if isinstance(module, nn.Linear):
                adapter_v2_linear_with_bias_and_scale(module)

        print(adapter_model.transformer.h[2].attn.c_attn.adapter_bias)
        assert not hasattr(llama_model.transformer.h[2].attn.c_attn, 'adapter_bias')
        assert not hasattr(llama_model.transformer.h[2].attn.c_attn, 'adapter_scale')
        assert hasattr(adapter_model.transformer.h[2].attn.c_attn, 'adapter_bias')
        assert hasattr(adapter_model.transformer.h[2].attn.c_attn, 'adapter_scale')