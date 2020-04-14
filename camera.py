from __future__ import annotations
from typing import List


class Camera:
    desp: List[float, float]

    desp_obj: List[float, float]

    def __init__(self):
        self.desp = [0, 0]
        self.desp_obj = [0, 0]

    def update(self) -> None:
        """
        Actualiza el estado de la camara
        """
        self.desp[0] += (self.desp_obj[0] - self.desp[0]) * 0.01
        self.desp[1] += (self.desp_obj[1] - self.desp[1]) * 0.01

    def drag(self, x: float, y: float) -> None:
        """
        Establece una nueva posicion objetivo para la camara
        :param x:   Posicion Objetivo para el eje X
        :param y:   Posicion Objetivo para el eje Y
        """
        self.desp_obj[0] += x
        self.desp_obj[1] += y
