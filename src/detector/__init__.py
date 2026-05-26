"""
🛡️ AG-Wrapper - Módulo Detector
"""

from .zombie_detector import (
    LegacyShield,
    ZombiePattern,
    DetectionResult,
    Severity,
    scan_directory,
)
from .injection_detector import (
    PromptInjectDetector,
    InjectionFinding,
    InjectionCategory,
    InjectionPattern,
)

__all__ = [
    "LegacyShield",
    "ZombiePattern",
    "DetectionResult",
    "Severity",
    "scan_directory",
    "PromptInjectDetector",
    "InjectionFinding",
    "InjectionCategory",
    "InjectionPattern",
]
