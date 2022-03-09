def create_player_sprite(self) -> arcade.AnimatedWalkingSprite:
    """Creates the animated player sprite

    Returns:
        The properly set up player sprite
    """
    # Where are the player images stored?
    texture_path = ASSETS_PATH / "images" / "player"

    # Set up the appropriate textures
    walking_paths = [
        texture_path / f"alienGreen_walk{x}.png" for x in (1, 2)
    ]
    climbing_paths = [
        texture_path / f"alienGreen_climb{x}.png" for x in (1, 2)
    ]
    standing_path = texture_path / "alienGreen_stand.png"

    # Load them all now
    walking_right_textures = [
        arcade.load_texture(texture) for texture in walking_paths
    ]
    walking_left_textures = [
        arcade.load_texture(texture, mirrored=True)
        for texture in walking_paths
    ]

    walking_up_textures = [
        arcade.load_texture(texture) for texture in climbing_paths
    ]
    walking_down_textures = [
        arcade.load_texture(texture) for texture in climbing_paths
    ]

    standing_right_textures = [arcade.load_texture(standing_path)]

    standing_left_textures = [
        arcade.load_texture(standing_path, mirrored=True)
    ]

    # Create the sprite
    player = arcade.AnimatedWalkingSprite()

    # Add the proper textures
    player.stand_left_textures = standing_left_textures
    player.stand_right_textures = standing_right_textures
    player.walk_left_textures = walking_left_textures
    player.walk_right_textures = walking_right_textures
    player.walk_up_textures = walking_up_textures
    player.walk_down_textures = walking_down_textures

    # Set the player defaults
    player.center_x = PLAYER_START_X
    player.center_y = PLAYER_START_Y
    player.state = arcade.FACE_RIGHT

    # Set the initial texture
    player.texture = player.stand_right_textures[0]

    return player
