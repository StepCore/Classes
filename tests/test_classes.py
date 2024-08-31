import pytest

from oop.classes import Category, Product


@pytest.fixture()
def product_camera():
    return Product("camera", "for streaming", 15000, "good")


@pytest.fixture()
def category_video():
    return Category("video", "record", "camera")


@pytest.fixture()
def product_pc():
    return Product("pc", "for playing the game", 150000, "best")


@pytest.fixture()
def category_gadget():
    return Category("gadget", "digital", "pc")


def test_camera(product_camera):
    assert product_camera.name == "camera"
    assert product_camera.description == "for streaming"
    assert product_camera.price == 15000
    assert product_camera.quantity == "good"


def test_video(category_video):
    assert category_video.name == "video"
    assert category_video.description == "record"
    assert category_video.products == "camera"


def test_pc(product_pc):
    assert product_pc.name == "pc"
    assert product_pc.description == "for playing the game"
    assert product_pc.price == 150000
    assert product_pc.quantity == "best"


def test_gadget(category_gadget):
    assert category_gadget.name == "gadget"
    assert category_gadget.description == "digital"
    assert category_gadget.products == "pc"
