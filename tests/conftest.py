"""pytest 全局配置。

在所有测试模块导入之前设置环境变量，确保 huggingface 相关库
在初始化时就以离线模式运行（模型已缓存的情况）。
"""

from __future__ import annotations

import os
from pathlib import Path

# 在 pytest 收集任何测试之前检查 BGE-M3 模型是否已本地缓存
# 若已缓存则启用离线模式，避免网络不可达时加载挂起
_cache_base = Path.home() / ".cache" / "huggingface" / "hub" / "models--BAAI--bge-m3"
if (_cache_base / "snapshots").is_dir():
    os.environ["HF_HUB_OFFLINE"] = "1"
