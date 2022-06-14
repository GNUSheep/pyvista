import numpy as np
from numpy.random import default_rng
from pytest import fixture

import pyvista
from pyvista import examples

pyvista.OFF_SCREEN = True


@fixture(scope='session')
def set_mpl():
    """Avoid matplotlib windows popping up."""
    try:
        import matplotlib
    except Exception:
        pass
    else:
        matplotlib.use('agg', force=True)


@fixture()
def cube():
    return pyvista.Cube()


@fixture()
def airplane():
    return examples.load_airplane()


@fixture()
def rectilinear():
    return examples.load_rectilinear()


@fixture()
def sphere():
    return examples.load_sphere()


@fixture()
def uniform():
    return examples.load_uniform()


@fixture()
def ant():
    return examples.load_ant()


@fixture()
def globe():
    return examples.load_globe()


@fixture()
def hexbeam():
    return examples.load_hexbeam()


@fixture()
def struct_grid():
    x, y, z = np.meshgrid(
        np.arange(-10, 10, 2, dtype=np.float32),
        np.arange(-10, 10, 2, dtype=np.float32),
        np.arange(-10, 10, 2, dtype=np.float32),
    )
    return pyvista.StructuredGrid(x, y, z)


@fixture()
def plane():
    return pyvista.Plane()


@fixture()
def spline():
    return examples.load_spline()


@fixture()
def tri_cylinder():
    """Triangulated cylinder"""
    return pyvista.Cylinder().triangulate()


@fixture()
def datasets():
    return [
        examples.load_uniform(),  # UniformGrid
        examples.load_rectilinear(),  # RectilinearGrid
        examples.load_hexbeam(),  # UnstructuredGrid
        examples.load_airplane(),  # PolyData
        examples.load_structured(),  # StructuredGrid
    ]


@fixture()
def pointset():
    rng = default_rng(0)
    points = rng.random((10, 3))
    return pyvista.PointSet(points)


@fixture()
def image():
    # create a basic texture by plotting a sphere
    pl = pyvista.Plotter(window_size=(200, 200), lighting=None, off_screen=True)
    pl.add_mesh(pyvista.Sphere(), color='k')
    pl.background_color = 'w'
    pl.camera_position = 'xy'
    pl.camera.zoom(0.5)
    return pyvista.Texture(pl.screenshot()).to_image()


def pytest_addoption(parser):
    parser.addoption("--reset_image_cache", action='store_true', default=False)
    parser.addoption("--ignore_image_cache", action='store_true', default=False)
    parser.addoption("--fail_extra_image_cache", action='store_true', default=False)
