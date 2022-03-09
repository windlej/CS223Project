def on_draw(self) -> None:
    arcade.start_render()

    # Draw all the sprites
    self.background.draw()
    self.walls.draw()
    self.coins.draw()
    self.goals.draw()
    self.ladders.draw()
    self.player.draw()
