import torch

class autocast(torch.autocast_mode.autocast):
    r"""
    See :class:`torch.autocast`.
    ``torch.cpu.amp.autocast(args...)`` is equivalent to ``torch.autocast("cpu", args...)``
    """
    def __init__(self, enabled=True, dtype=torch.float16):
        super().__init__("cpu", enabled=enabled, dtype=dtype)
