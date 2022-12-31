from __future__ import annotations
from matplotlib import pyplot as plt
from nptyping import NDArray
import numpy as np

from src.days.day22.models import MapObject


class Plot:
    def __init__(self) -> None:
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection="3d")

    def show(self):
        plt.show(block=True)

    def plot_cube(self, cube: NDArray):
        fill_edges(cube)
        remove_internal = np.vectorize(lambda x: x != " ")
        voxels = remove_internal(cube)
        colors = np.vectorize(
            lambda x: "white"
            if x == MapObject.Ground
            else "red"
            if x == MapObject.Wall
            else "yellow"
            if x == MapObject.Edge
            else "limegreen"
        )

        self.__setup_axis(cube.shape[0])
        self.ax.voxels(voxels, facecolors=colors(cube))

    def __setup_axis(self, side_length: int):
        self.ax.clear()
        self.ax.set_xlabel("X")
        self.ax.set_ylabel("Y")
        self.ax.set_zlabel("Z")

        self.ax.set_xlim([-1, side_length + 1])
        self.ax.set_ylim([-1, side_length + 1])
        self.ax.set_zlim([-1, side_length + 1])
        self.ax.invert_zaxis()


def fill_edges(cube: NDArray):
    side_length = cube.shape[0]
    for x in range(1, side_length - 2):
        cube[x, 1, 1] = MapObject.Edge
        cube[x, side_length - 2, 1] = MapObject.Edge
        cube[x, 1, side_length - 2] = MapObject.Edge
        cube[x, side_length - 2, side_length - 2] = MapObject.Edge
    for y in range(1, side_length - 2):
        cube[1, y, 1] = MapObject.Edge
        cube[1, y, side_length - 2] = MapObject.Edge
        cube[side_length - 2, y, 1] = MapObject.Edge
        cube[side_length - 2, y, side_length - 2] = MapObject.Edge
    for z in range(1, side_length - 2):
        cube[1, 1, z] = MapObject.Edge
        cube[1, side_length - 2, z] = MapObject.Edge
        cube[side_length - 2, 1, z] = MapObject.Edge
        cube[side_length - 2, side_length - 2, z] = MapObject.Edge
