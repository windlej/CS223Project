# Player constants
GRAVITY = 1.0
PLAYER_START_X = 65
PLAYER_START_Y = 256
PLAYER_MOVE_SPEED = 10
PLAYER_JUMP_SPEED = 20

def on_key_press(self, key: int, modifiers: int) -> None:
    """Arguments:
    key -- Which key was pressed
    modifiers -- Which modifiers were down at the time
    """

    # Check for player left or right movement
    if key in [arcade.key.LEFT, arcade.key.A]:
        self.player.change_x = -PLAYER_MOVE_SPEED
    elif key in [arcade.key.RIGHT, arcade.key.D]:
        self.player.change_x = PLAYER_MOVE_SPEED

    # Check if player can climb up or down
    elif key in [arcade.key.UP, arcade.key.W]:
        if self.physics_engine.is_on_ladder():
            self.player.change_y = PLAYER_MOVE_SPEED
    elif key in [arcade.key.DOWN, arcade.key.S]:
        if self.physics_engine.is_on_ladder():
            self.player.change_y = -PLAYER_MOVE_SPEED

    # Check if player can jump
    elif key == arcade.key.SPACE:
        if self.physics_engine.can_jump():
            self.player.change_y = PLAYER_JUMP_SPEED
            # Play the jump sound
            arcade.play_sound(self.jump_sound)
          
def on_key_release(self, key: int, modifiers: int) -> None:
    """Arguments:
    key -- The key which was released
    modifiers -- Which modifiers were down at the time
    """

    # Check for player left or right movement
    if key in [
        arcade.key.LEFT,
        arcade.key.A,
        arcade.key.RIGHT,
        arcade.key.D,
    ]:
        self.player.change_x = 0

    # Check if player can climb up or down
    elif key in [
        arcade.key.UP,
        arcade.key.W,
        arcade.key.DOWN,
        arcade.key.S,
    ]:
        if self.physics_engine.is_on_ladder():
            self.player.change_y = 0
