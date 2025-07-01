"""Defines a pokemon class."""

from typing import Any

import requests

MIN_DEX_NUMBER = 1
MAX_DEX_NUMBER = 151
MAX_TYPES = 2


class Pokemon:
    """Represents a pokemon."""

    def __init__(self, pokemon_id: str) -> None:
        """Instantiate a Pokemon object.

        Args:
            pokemon_id (str): Represents the pokemon name or id that will be created.

        """
        is_valid = Pokemon.id_validator(pokemon_id)
        if not is_valid:
            message = "Invalid pokemon id received."
            raise ValueError(message)
        poke_data: dict[str, Any] = Pokemon.get_pokemon_data(pokemon_id)
        self.name = poke_data["name"]
        self.id = poke_data["id"]
        self.type1 = poke_data["types"][0]
        self.type2 = poke_data["types"][1] if len(poke_data["types"]) > 1 else None
        self.height = poke_data["height"]
        self.weight = poke_data["weight"]
        self.sprite_url = poke_data["sprite"]
        self.cry_url = poke_data["cry"]
        self.flavor_text = poke_data["flavor_text"]
        self.genus = poke_data["genus"]
        self.areas = poke_data["areas"]
        self.learnset = poke_data["learnset"]

    @staticmethod
    def id_validator(pokemon_id: str) -> bool:
        """Validate gen 1 pokemon name or id entry.

        Args:
            pokemon_id (str): Is a pokemon name or id that will be validated.

        Returns:
            bool: Whether or not it is a valid pokemon.

        """
        poke_info = requests.get(
            f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}", timeout=5
        )
        try:
            poke_info.raise_for_status()
        except requests.HTTPError:
            return False
        return MIN_DEX_NUMBER <= int(poke_info.json()["id"]) <= MAX_DEX_NUMBER

    @staticmethod
    def get_pokemon_data(pokemon_id: str) -> dict[str, Any]:
        """Get all pokedex data from pokeAPI.

        Args:
            pokemon_id (str): Is a pokemon name or id to get the data for.

        Returns:
            dict[str, Any]: All the pokedex data in a dictionary.

        """
        # Requesting pokemon data
        poke_info = requests.get(
            f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}", timeout=5
        ).json()
        species_url = poke_info["species"]["url"]
        species_info = requests.get(species_url, timeout=5).json()

        location_url = poke_info["location_area_encounters"]
        location_info = requests.get(location_url, timeout=5).json()

        # Get area info
        areas = [
            location["location_area"]["name"]
            for location in location_info
            for version in location["version_details"]
            if version["version"]["name"] == "red"
        ]

        moves = [
            {
                "move": move["move"]["name"],
                "method": version["move_learn_method"]["name"],
                "level": version["level_learned_at"],
            }
            for move in poke_info["moves"]
            for version in move["version_group_details"]
            if version["version_group"]["name"] == "red-blue"
        ]
        # Get types info
        poke_types = []
        if poke_info["past_types"] == []:
            poke_types.append(poke_info["types"][0]["type"]["name"])
            if len(poke_info["types"]) == MAX_TYPES:
                poke_types.append(poke_info["types"][1]["type"]["name"])
        else:
            poke_types.append(poke_info["past_types"][0]["types"][0]["type"]["name"])
        # Build the dictionary
        return {
            "name": poke_info["name"][0].upper() + poke_info["name"][1:],
            "id": poke_info["id"],
            "types": poke_types,
            "height": int(poke_info["height"]) / 10,
            "weight": int(poke_info["weight"]) / 10,
            "sprite": poke_info["sprites"]["versions"]["generation-i"]["red-blue"][
                "front_transparent"
            ],
            "cry": poke_info["cries"]["legacy"],
            "flavor_text": " ".join(
                next(
                    item["flavor_text"]
                    for item in species_info["flavor_text_entries"]
                    if item["language"]["name"] == "en"
                    and item["version"]["name"] == "red"
                ).split()
            ),
            "genus": next(
                item["genus"]
                for item in species_info["genera"]
                if item["language"]["name"] == "en"
            ),
            "areas": areas,
            "learnset": moves,
        }
