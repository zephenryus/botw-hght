class Hght:
    height_scale_factor = 800 / 65335

    def __init__(self, height: float):
        self.height = height

    @staticmethod
    def to_float(height: int) -> float:
        return height * Hght.height_scale_factor

    @staticmethod
    def to_int(height: float) -> int:
        return round(height / Hght.height_scale_factor)
