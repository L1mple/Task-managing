import pytest
from fastapi.testclient import TestClient

from app.api.main import create_api

app = create_api()


@pytest.fixture
def client():
    with TestClient(app) as c:  # noqa
        yield c


@pytest.mark.parametrize(
    "build_name, expected_output",
    [
        ("asdasd", {"detail": "No build found with passed name"}),
        (
            "forward_interest",
            {
                "tasks": [
                    "build_teal_leprechauns",
                    "enable_yellow_centaurs",
                    "bring_olive_centaurs",
                    "coloring_white_centaurs",
                    "create_teal_centaurs",
                    "design_lime_centaurs",
                    "train_purple_centaurs",
                    "upgrade_navy_centaurs",
                    "create_maroon_centaurs",
                    "bring_blue_centaurs",
                    "read_yellow_centaurs",
                    "create_olive_centaurs",
                    "coloring_aqua_centaurs",
                    "coloring_aqua_golems",
                    "coloring_navy_golems",
                    "map_black_leprechauns",
                    "upgrade_white_leprechauns",
                    "map_olive_leprechauns",
                    "enable_lime_leprechauns",
                    "create_aqua_humans",
                    "enable_olive_humans",
                    "build_maroon_humans",
                    "write_silver_humans",
                    "write_white_humans",
                    "create_purple_humans",
                    "train_white_humans",
                    "write_teal_humans",
                    "enable_silver_humans",
                    "bring_blue_ogres",
                    "design_white_ogres",
                    "train_green_ogres",
                    "upgrade_aqua_ogres",
                    "write_silver_ogres",
                    "enable_fuchsia_ogres",
                    "bring_green_ogres",
                    "build_yellow_ogres",
                    "create_maroon_ogres",
                    "design_green_ogres",
                    "upgrade_navy_ogres",
                    "write_blue_ogres",
                    "write_fuchsia_golems",
                ]
            },
        ),
        (
            "front_arm",
            {
                "tasks": [
                    "build_lime_golems",
                    "design_fuchsia_goblins",
                    "read_fuchsia_goblins",
                    "build_silver_goblins",
                    "build_teal_goblins",
                    "create_lime_goblins",
                    "create_silver_goblins",
                    "design_gray_goblins",
                    "design_olive_goblins",
                    "build_maroon_goblins",
                    "build_purple_goblins",
                    "coloring_white_goblins",
                    "upgrade_maroon_goblins",
                    "map_gray_goblins",
                    "coloring_black_goblins",
                    "write_teal_witches",
                    "design_maroon_witches",
                    "write_teal_golems",
                    "write_white_golems",
                    "coloring_silver_golems",
                    "enable_white_golems",
                    "train_maroon_golems",
                    "design_teal_golems",
                    "create_white_centaurs",
                    "design_teal_centaurs",
                    "read_lime_centaurs",
                    "create_blue_centaurs",
                    "map_fuchsia_centaurs",
                    "bring_lime_centaurs",
                    "coloring_gray_centaurs",
                    "create_silver_centaurs",
                    "upgrade_aqua_centaurs",
                    "design_yellow_centaurs",
                    "enable_fuchsia_humans",
                    "read_silver_humans",
                    "upgrade_lime_humans",
                    "bring_purple_humans",
                    "create_white_humans",
                    "upgrade_green_humans",
                    "design_blue_humans",
                    "bring_aqua_humans",
                    "map_aqua_humans",
                    "write_gray_humans",
                    "read_maroon_humans",
                    "build_purple_humans",
                    "design_lime_humans",
                    "write_yellow_humans",
                    "map_purple_humans",
                    "train_fuchsia_orcs",
                    "read_aqua_orcs",
                    "coloring_aqua_golems",
                    "create_fuchsia_golems",
                    "train_fuchsia_golems",
                    "design_maroon_golems",
                    "coloring_purple_golems",
                    "design_silver_golems",
                    "read_teal_golems",
                    "train_gray_golems",
                    "design_yellow_golems",
                    "map_maroon_golems",
                    "write_navy_golems",
                    "read_gray_golems",
                    "build_black_leprechauns",
                    "coloring_purple_leprechauns",
                    "design_teal_leprechauns",
                    "map_white_leprechauns",
                    "write_navy_leprechauns",
                    "coloring_fuchsia_leprechauns",
                    "read_white_leprechauns",
                    "train_white_leprechauns",
                    "bring_green_humans",
                    "create_green_humans",
                    "map_yellow_humans",
                    "write_teal_humans",
                    "upgrade_black_humans",
                    "enable_lime_humans",
                    "read_aqua_humans",
                    "upgrade_silver_humans",
                    "build_maroon_humans",
                    "coloring_white_humans",
                    "create_fuchsia_humans",
                    "write_maroon_humans",
                    "upgrade_gray_humans",
                ]
            },
        ),
        (
            "reach_wind",
            {
                "tasks": [
                    "build_black_golems",
                    "coloring_teal_golems",
                    "read_aqua_golems",
                    "design_purple_golems",
                    "map_gray_golems",
                    "read_teal_golems",
                    "bring_maroon_golems",
                    "bring_silver_orcs",
                    "coloring_silver_gorgons",
                    "upgrade_silver_gorgons",
                    "coloring_lime_gorgons",
                    "create_blue_gorgons",
                    "coloring_yellow_gorgons",
                    "create_teal_gorgons",
                    "design_black_gorgons",
                    "write_teal_gorgons",
                    "enable_purple_gorgons",
                    "map_silver_gorgons",
                    "upgrade_purple_gorgons",
                    "build_blue_gorgons",
                    "coloring_aqua_golems",
                    "coloring_fuchsia_humans",
                    "coloring_maroon_witches",
                    "upgrade_fuchsia_witches",
                    "build_gray_witches",
                    "build_white_witches",
                    "design_purple_witches",
                    "read_silver_witches",
                    "read_teal_witches",
                    "create_white_witches",
                    "build_aqua_witches",
                    "enable_aqua_witches",
                    "build_olive_witches",
                    "upgrade_lime_witches",
                    "write_maroon_witches",
                    "read_fuchsia_witches",
                    "coloring_green_witches",
                    "design_navy_fairies",
                    "read_green_fairies",
                    "train_olive_fairies",
                    "bring_lime_fairies",
                    "coloring_gray_fairies",
                    "bring_white_fairies",
                    "bring_purple_fairies",
                    "build_olive_fairies",
                    "coloring_silver_fairies",
                    "read_teal_fairies",
                    "train_green_fairies",
                    "build_fuchsia_fairies",
                    "create_white_fairies",
                    "read_gray_fairies",
                    "train_navy_fairies",
                    "write_olive_fairies",
                    "coloring_purple_fairies",
                    "coloring_yellow_leprechauns",
                    "bring_green_witches",
                    "design_teal_witches",
                    "upgrade_aqua_witches",
                    "create_purple_witches",
                    "coloring_olive_gnomes",
                    "bring_black_gnomes",
                    "build_silver_gnomes",
                    "coloring_blue_gnomes",
                    "coloring_silver_gnomes",
                    "map_maroon_gnomes",
                    "create_navy_gnomes",
                    "create_fuchsia_gnomes",
                    "enable_navy_gnomes",
                    "map_fuchsia_gnomes",
                    "write_aqua_gnomes",
                    "write_teal_gnomes",
                    "upgrade_yellow_gnomes",
                    "design_silver_gnomes",
                    "create_teal_gnomes",
                    "enable_green_gnomes",
                    "bring_white_gnomes",
                    "enable_maroon_gnomes",
                    "create_silver_gnomes",
                    "create_gray_goblins",
                    "enable_blue_goblins",
                    "enable_lime_goblins",
                    "enable_silver_goblins",
                    "map_maroon_goblins",
                    "read_blue_goblins",
                    "write_olive_goblins",
                    "train_olive_goblins",
                    "upgrade_maroon_goblins",
                    "write_fuchsia_goblins",
                    "enable_aqua_goblins",
                    "map_gray_leprechauns",
                    "map_purple_leprechauns",
                    "build_olive_gnomes",
                    "enable_lime_gnomes",
                    "train_olive_gnomes",
                    "coloring_maroon_gnomes",
                    "map_gray_gnomes",
                    "upgrade_maroon_gnomes",
                    "write_purple_gnomes",
                    "create_white_gnomes",
                    "map_yellow_gnomes",
                    "read_fuchsia_orcs",
                    "coloring_green_humans",
                    "write_lime_humans",
                    "coloring_teal_humans",
                    "bring_aqua_humans",
                    "build_gray_humans",
                    "coloring_silver_humans",
                    "create_olive_humans",
                    "upgrade_aqua_humans",
                    "bring_green_humans",
                    "create_green_humans",
                    "map_yellow_humans",
                    "write_teal_humans",
                    "upgrade_black_humans",
                    "enable_lime_humans",
                    "read_aqua_humans",
                    "upgrade_silver_humans",
                    "build_maroon_humans",
                    "coloring_white_humans",
                    "create_fuchsia_humans",
                    "write_maroon_humans",
                    "upgrade_gray_humans",
                    "read_gray_humans",
                    "read_yellow_gorgons",
                    "create_fuchsia_centaurs",
                    "design_green_centaurs",
                    "build_blue_centaurs",
                    "coloring_navy_centaurs",
                    "bring_blue_centaurs",
                    "read_yellow_centaurs",
                    "upgrade_navy_centaurs",
                    "create_olive_centaurs",
                    "enable_olive_centaurs",
                    "upgrade_teal_centaurs",
                    "write_maroon_centaurs",
                    "train_green_centaurs",
                    "build_silver_orcs",
                    "bring_fuchsia_orcs",
                    "design_navy_orcs",
                    "upgrade_silver_orcs",
                    "design_blue_orcs",
                    "create_green_orcs",
                    "create_purple_orcs",
                    "train_teal_orcs",
                    "enable_olive_orcs",
                    "coloring_black_orcs",
                    "map_olive_orcs",
                    "write_olive_orcs",
                    "train_navy_orcs",
                    "bring_green_orcs",
                    "create_silver_orcs",
                    "read_teal_orcs",
                    "build_teal_orcs",
                    "build_maroon_orcs",
                    "train_black_orcs",
                    "enable_silver_orcs",
                    "design_green_orcs",
                    "enable_maroon_orcs",
                    "train_lime_orcs",
                    "train_maroon_leprechauns",
                    "upgrade_olive_fairies",
                    "write_purple_cyclops",
                    "bring_purple_goblins",
                    "coloring_fuchsia_goblins",
                    "enable_maroon_goblins",
                    "upgrade_lime_goblins",
                    "write_green_goblins",
                    "coloring_olive_goblins",
                    "upgrade_olive_goblins",
                    "write_white_goblins",
                ]
            },
        ),
        (
            "voice_central",
            {
                "tasks": [
                    "build_white_leprechauns",
                    "coloring_yellow_leprechauns",
                    "enable_olive_leprechauns",
                    "write_purple_leprechauns",
                    "bring_yellow_leprechauns",
                    "build_gray_leprechauns",
                    "create_navy_leprechauns",
                    "design_yellow_leprechauns",
                    "build_olive_leprechauns",
                    "coloring_olive_leprechauns",
                    "read_gray_leprechauns",
                    "map_navy_leprechauns",
                    "bring_purple_leprechauns",
                    "create_gray_ogres",
                    "write_green_ogres",
                    "build_aqua_ogres",
                    "write_gray_ogres",
                    "coloring_purple_ogres",
                    "map_maroon_ogres",
                    "read_navy_ogres",
                    "create_olive_ogres",
                    "coloring_black_ogres",
                    "design_navy_ogres",
                    "bring_yellow_ogres",
                    "coloring_fuchsia_gorgons",
                    "train_white_gorgons",
                    "create_teal_gorgons",
                    "read_yellow_gorgons",
                    "train_lime_gorgons",
                    "upgrade_maroon_gorgons",
                    "write_navy_gorgons",
                    "build_lime_gorgons",
                    "enable_green_humans",
                    "enable_lime_humans",
                    "write_silver_humans",
                    "create_black_humans",
                    "build_navy_humans",
                    "map_teal_leprechauns",
                    "coloring_aqua_leprechauns",
                    "map_maroon_centaurs",
                    "train_blue_centaurs",
                    "coloring_black_centaurs",
                    "build_olive_centaurs",
                    "write_blue_centaurs",
                    "map_olive_centaurs",
                    "coloring_purple_centaurs",
                    "enable_blue_centaurs",
                    "map_teal_centaurs",
                    "build_silver_centaurs",
                    "create_aqua_centaurs",
                    "enable_silver_centaurs",
                    "read_silver_centaurs",
                    "coloring_teal_centaurs",
                    "coloring_white_goblins",
                    "design_blue_leprechauns",
                    "enable_silver_gnomes",
                    "coloring_fuchsia_gnomes",
                    "enable_teal_gnomes",
                    "design_white_gnomes",
                    "create_black_gnomes",
                    "read_maroon_gnomes",
                    "upgrade_maroon_gnomes",
                    "upgrade_gray_gnomes",
                    "upgrade_purple_gnomes",
                    "coloring_olive_gnomes",
                    "enable_navy_gnomes",
                    "map_fuchsia_gnomes",
                    "write_aqua_gnomes",
                    "write_teal_gnomes",
                    "upgrade_yellow_gnomes",
                    "design_green_gnomes",
                    "read_teal_orcs",
                    "build_teal_orcs",
                    "build_maroon_orcs",
                    "train_black_orcs",
                    "enable_silver_orcs",
                    "design_green_orcs",
                    "enable_gray_fairies",
                    "design_white_fairies",
                    "upgrade_aqua_fairies",
                    "read_fuchsia_fairies",
                    "enable_aqua_fairies",
                    "upgrade_yellow_witches",
                    "build_fuchsia_witches",
                    "read_purple_witches",
                    "train_silver_witches",
                    "coloring_teal_witches",
                    "build_blue_witches",
                    "create_yellow_witches",
                    "enable_purple_witches",
                    "write_black_witches",
                    "write_green_witches",
                    "enable_lime_witches",
                    "enable_navy_witches",
                    "write_blue_witches",
                    "write_white_witches",
                    "enable_black_witches",
                    "map_gray_gorgons",
                    "build_gray_gorgons",
                    "build_maroon_gorgons",
                    "coloring_white_gorgons",
                    "design_silver_gorgons",
                    "write_gray_gorgons",
                    "enable_gray_gorgons",
                    "read_fuchsia_gorgons",
                    "read_gray_ogres",
                    "train_aqua_humans",
                    "coloring_gray_leprechauns",
                    "create_black_leprechauns",
                    "map_lime_leprechauns",
                    "write_yellow_leprechauns",
                    "train_fuchsia_leprechauns",
                    "train_teal_centaurs",
                    "build_teal_goblins",
                    "design_black_goblins",
                    "read_green_goblins",
                    "train_blue_goblins",
                    "design_teal_goblins",
                    "read_gray_goblins",
                    "train_fuchsia_goblins",
                    "write_blue_goblins",
                ]
            },
        ),
        (
            "write_beautiful",
            {
                "tasks": [
                    "read_fuchsia_ogres",
                    "upgrade_green_ogres",
                    "write_yellow_ogres",
                    "coloring_lime_ogres",
                    "read_purple_ogres",
                    "train_aqua_ogres",
                    "coloring_olive_ogres",
                    "design_olive_ogres",
                    "create_silver_ogres",
                    "create_teal_ogres",
                    "upgrade_black_ogres",
                    "write_green_ogres",
                    "enable_silver_ogres",
                    "build_black_ogres",
                    "train_lime_ogres",
                    "write_teal_ogres",
                    "bring_gray_ogres",
                    "build_silver_orcs",
                    "bring_fuchsia_orcs",
                    "design_navy_orcs",
                    "upgrade_silver_orcs",
                    "design_blue_orcs",
                    "create_green_orcs",
                    "create_purple_orcs",
                    "train_teal_orcs",
                    "enable_olive_orcs",
                    "coloring_black_orcs",
                    "map_olive_orcs",
                    "write_olive_orcs",
                    "train_navy_orcs",
                    "bring_green_orcs",
                    "bring_maroon_leprechauns",
                    "map_aqua_leprechauns",
                    "read_white_leprechauns",
                    "read_fuchsia_leprechauns",
                    "bring_silver_leprechauns",
                    "enable_navy_witches",
                    "enable_white_witches",
                    "read_green_witches",
                    "map_green_witches",
                    "bring_silver_witches",
                    "design_blue_cyclops",
                    "write_aqua_cyclops",
                    "enable_teal_cyclops",
                    "bring_teal_cyclops",
                    "build_aqua_orcs",
                    "bring_blue_orcs",
                    "create_navy_orcs",
                    "coloring_lime_orcs",
                    "enable_purple_orcs",
                    "read_olive_orcs",
                    "design_fuchsia_orcs",
                    "create_blue_orcs",
                    "write_fuchsia_orcs",
                    "enable_fuchsia_orcs",
                    "coloring_fuchsia_orcs",
                    "bring_purple_fairies",
                    "build_olive_fairies",
                    "coloring_silver_fairies",
                    "read_teal_fairies",
                    "train_green_fairies",
                    "build_fuchsia_fairies",
                    "bring_teal_fairies",
                    "build_white_fairies",
                    "map_green_fairies",
                    "upgrade_white_fairies",
                    "coloring_white_fairies",
                    "create_black_fairies",
                    "map_gray_fairies",
                    "upgrade_blue_fairies",
                    "coloring_green_fairies",
                    "bring_white_gorgons",
                    "coloring_aqua_gorgons",
                    "design_fuchsia_gorgons",
                    "read_silver_gorgons",
                    "coloring_maroon_gorgons",
                    "bring_black_humans",
                    "coloring_purple_humans",
                    "enable_lime_humans",
                    "enable_maroon_humans",
                    "enable_purple_humans",
                    "coloring_maroon_humans",
                    "train_yellow_humans",
                    "coloring_navy_humans",
                    "build_green_gnomes",
                    "design_teal_gnomes",
                    "read_navy_gnomes",
                    "design_blue_gnomes",
                    "enable_black_gnomes",
                    "map_aqua_gnomes",
                    "upgrade_teal_gnomes",
                    "design_fuchsia_gnomes",
                    "bring_white_gnomes",
                    "enable_maroon_gnomes",
                    "enable_navy_gnomes",
                    "coloring_aqua_gnomes",
                    "read_white_gnomes",
                    "coloring_teal_gnomes",
                    "bring_lime_golems",
                    "train_blue_golems",
                    "train_fuchsia_golems",
                    "upgrade_purple_golems",
                    "build_gray_golems",
                    "coloring_lime_golems",
                    "write_fuchsia_golems",
                    "create_white_golems",
                    "bring_black_golems",
                    "design_gray_golems",
                    "coloring_purple_golems",
                    "design_silver_golems",
                    "read_teal_golems",
                    "train_gray_golems",
                    "train_maroon_golems",
                    "design_yellow_golems",
                    "upgrade_green_golems",
                    "upgrade_lime_golems",
                    "design_fuchsia_golems",
                    "coloring_teal_golems",
                    "read_aqua_golems",
                    "design_purple_golems",
                    "write_white_golems",
                    "coloring_white_golems",
                    "create_aqua_centaurs",
                    "bring_green_centaurs",
                    "create_navy_centaurs",
                    "map_yellow_centaurs",
                    "read_maroon_centaurs",
                    "train_yellow_centaurs",
                    "create_black_centaurs",
                    "coloring_olive_centaurs",
                    "create_green_centaurs",
                    "train_gray_centaurs",
                    "coloring_yellow_centaurs",
                    "create_navy_witches",
                    "read_aqua_centaurs",
                    "read_yellow_centaurs",
                    "upgrade_teal_centaurs",
                    "create_gray_centaurs",
                    "upgrade_maroon_centaurs",
                    "read_navy_centaurs",
                    "design_purple_centaurs",
                    "coloring_gray_humans",
                    "train_aqua_humans",
                    "train_fuchsia_humans",
                    "upgrade_yellow_humans",
                    "bring_gray_humans",
                    "enable_fuchsia_humans",
                    "read_silver_humans",
                    "upgrade_lime_humans",
                    "bring_purple_humans",
                    "design_navy_humans",
                    "coloring_white_humans",
                    "map_fuchsia_humans",
                    "map_green_humans",
                    "train_olive_humans",
                    "enable_black_humans",
                    "upgrade_yellow_witches",
                    "build_fuchsia_witches",
                    "read_purple_witches",
                    "train_silver_witches",
                    "coloring_teal_witches",
                    "build_blue_witches",
                    "create_yellow_witches",
                    "enable_purple_witches",
                    "write_black_witches",
                    "write_green_witches",
                    "enable_lime_witches",
                    "write_blue_witches",
                    "write_white_witches",
                    "enable_black_witches",
                    "enable_white_goblins",
                    "build_black_goblins",
                    "build_olive_goblins",
                    "design_white_goblins",
                    "train_purple_goblins",
                    "upgrade_olive_goblins",
                    "coloring_lime_goblins",
                    "design_purple_goblins",
                    "map_olive_goblins",
                    "create_white_goblins",
                    "train_teal_goblins",
                    "write_silver_goblins",
                    "create_olive_goblins",
                    "upgrade_navy_goblins",
                    "write_navy_goblins",
                    "create_teal_goblins",
                    "create_purple_goblins",
                    "map_blue_goblins",
                    "build_maroon_goblins",
                    "build_purple_goblins",
                    "coloring_white_goblins",
                    "upgrade_maroon_goblins",
                    "map_gray_goblins",
                    "read_lime_goblins",
                    "read_navy_goblins",
                    "enable_teal_goblins",
                    "map_black_goblins",
                    "read_gray_leprechauns",
                    "coloring_olive_gnomes",
                    "build_blue_gnomes",
                    "coloring_yellow_gnomes",
                    "design_black_gnomes",
                    "design_olive_gnomes",
                    "upgrade_purple_gnomes",
                    "coloring_white_gnomes",
                    "bring_fuchsia_gnomes",
                    "create_purple_gnomes",
                    "train_green_gnomes",
                    "enable_purple_gnomes",
                    "read_lime_gnomes",
                    "coloring_fuchsia_fairies",
                    "design_purple_fairies",
                    "bring_gray_fairies",
                    "coloring_lime_fairies",
                    "create_lime_fairies",
                    "design_lime_fairies",
                    "upgrade_fuchsia_fairies",
                    "design_aqua_fairies",
                    "train_white_fairies",
                    "build_black_leprechauns",
                    "coloring_purple_leprechauns",
                    "design_teal_leprechauns",
                    "map_white_leprechauns",
                    "write_navy_leprechauns",
                    "coloring_fuchsia_leprechauns",
                    "train_white_leprechauns",
                    "build_maroon_humans",
                    "create_fuchsia_humans",
                    "write_maroon_humans",
                    "write_purple_leprechauns",
                ]
            },
        ),
    ],
)
def test_get_build_tasks(
    client: TestClient,
    build_name: str,
    expected_output: dict,
) -> None:
    response = client.post(
        url="/build/get_tasks",
        json={"build": build_name},
    )
    assert response.json() == expected_output
