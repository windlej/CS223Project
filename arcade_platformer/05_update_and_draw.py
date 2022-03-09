def on_draw(self) -> None:
    arcade.start_render()

    # Draw all the sprites
    self.background.draw()
    self.walls.draw()
    self.coins.draw()
    self.goals.draw()
    self.ladders.draw()
    self.player.draw()
    
def on_update(self, delta_time: float) -> None:
    """Updates the position of all game objects

    Arguments:
        delta_time {float} -- How much time since the last call
    """

    # Update the player animation
    self.player.update_animation(delta_time)

    # Update player movement based on the physics engine
    self.physics_engine.update()

    # Restrict user movement so they can't walk off screen
    if self.player.left < 0:
        self.player.left = 0

    # Check if we've picked up a coin
    coins_hit = arcade.check_for_collision_with_list(
        sprite=self.player, sprite_list=self.coins
    )

    for coin in coins_hit:
        # Add the coin score to our score
        self.score += int(coin.properties["point_value"])

        # Play the coin sound
        arcade.play_sound(self.coin_sound)

        # Remove the coin
        coin.remove_from_sprite_lists()

    # Now check if we're at the ending goal
    goals_hit = arcade.check_for_collision_with_list(
        sprite=self.player, sprite_list=self.goals
    )

    if goals_hit:
        # Play the victory sound
        self.victory_sound.play()

        # Set up the next level
        self.level += 1
        self.setup()
