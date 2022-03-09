# Game constants
# Window dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Arcade Platformer"

# Scaling constants
MAP_SCALING = 1.0

# Player constants
GRAVITY = 1.0
PLAYER_START_X = 65
PLAYER_START_Y = 256

def setup(self) -> None:
    """Sets up the game for the current level"""

    # Get the current map based on the level
    map_name = f"platform_level_{self.level:02}.tmx"
    map_path = ASSETS_PATH / map_name

    # What are the names of the layers?
    wall_layer = "ground"
    coin_layer = "coins"
    goal_layer = "goal"
    background_layer = "background"
    ladders_layer = "ladders"

    # Load the current map
    game_map = arcade.tilemap.read_tmx(str(map_path))

    # Load the layers
    self.background = arcade.tilemap.process_layer(
        game_map, layer_name=background_layer, scaling=MAP_SCALING
    )
    self.goals = arcade.tilemap.process_layer(
        game_map, layer_name=goal_layer, scaling=MAP_SCALING
    )
    self.walls = arcade.tilemap.process_layer(
        game_map, layer_name=wall_layer, scaling=MAP_SCALING
    )
    self.ladders = arcade.tilemap.process_layer(
        game_map, layer_name=ladders_layer, scaling=MAP_SCALING
    )
    self.coins = arcade.tilemap.process_layer(
        game_map, layer_name=coin_layer, scaling=MAP_SCALING
    )

    # Set the background color
    background_color = arcade.color.FRESH_AIR
    if game_map.background_color:
        background_color = game_map.background_color
    arcade.set_background_color(background_color)

    # Create the player sprite if they're not already set up
    if not self.player:
        self.player = self.create_player_sprite()

    # Move the player sprite back to the beginning
    self.player.center_x = PLAYER_START_X
    self.player.center_y = PLAYER_START_Y
    self.player.change_x = 0
    self.player.change_y = 0

    # Load the physics engine for this map
    self.physics_engine = arcade.PhysicsEnginePlatformer(
        player_sprite=self.player,
        platforms=self.walls,
        gravity_constant=GRAVITY,
        ladders=self.ladders,
    )
