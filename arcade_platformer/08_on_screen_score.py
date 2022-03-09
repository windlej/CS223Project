def on_draw(self) -> None:
    arcade.start_render()

    # Draw all the sprites
    self.background.draw()
    self.walls.draw()
    self.coins.draw()
    self.goals.draw()
    self.ladders.draw()
    self.player.draw()

    # Draw the score in the lower left
    score_text = f"Score: {self.score}"

    # First a black background for a shadow effect
    arcade.draw_text(
        score_text,
        start_x=10 + self.view_left,
        start_y=10 + self.view_bottom,
        color=arcade.csscolor.BLACK,
        font_size=40,
    )
    # Now in white, slightly shifted
    arcade.draw_text(
        score_text,
        start_x=15 + self.view_left,
        start_y=15 + self.view_bottom,
        color=arcade.csscolor.WHITE,
        font_size=40,
    )
