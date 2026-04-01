"""Package sorting rules for Smarter Technology's robotic factory."""

from __future__ import annotations


BULKY_VOLUME_THRESHOLD = 1_000_000
BULKY_DIMENSION_THRESHOLD = 150
HEAVY_MASS_THRESHOLD = 20


def sort(width: float, height: float, length: float, mass: float) -> str:
    """Return the destination stack for a package.

    A package is:
    - bulky when its volume is at least 1,000,000 cm^3, or any dimension is
      at least 150 cm
    - heavy when its mass is at least 20 kg

    Returns one of:
    - "STANDARD"
    - "SPECIAL"
    - "REJECTED"
    """

    _validate_non_negative(width=width, height=height, length=length, mass=mass)

    volume = width * height * length
    is_bulky = (
        volume >= BULKY_VOLUME_THRESHOLD
        or width >= BULKY_DIMENSION_THRESHOLD
        or height >= BULKY_DIMENSION_THRESHOLD
        or length >= BULKY_DIMENSION_THRESHOLD
    )
    is_heavy = mass >= HEAVY_MASS_THRESHOLD

    if is_bulky and is_heavy:
        return "REJECTED"
    if is_bulky or is_heavy:
        return "SPECIAL"
    return "STANDARD"


def _validate_non_negative(**measurements: float) -> None:
    """Reject impossible package measurements early."""

    invalid = [name for name, value in measurements.items() if value < 0]
    if invalid:
        names = ", ".join(sorted(invalid))
        raise ValueError(f"Measurements must be non-negative: {names}")
