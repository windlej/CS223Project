class TitleView(arcade.View):
    """Displays a title screen and prompts the user to begin the game.
    Provides a way to show instructions and start the game.
    """

    def __init__(self) -> None:
        super().__init__()

        # Find the title image in the images folder
        title_image_path = ASSETS_PATH / "images" / "title_image.png"

        # Load our title image
        self.title_image = arcade.load_texture(title_image_path)

        # Set our display timer
        self.display_timer = 3.0

        # Are we showing the instructions?
        self.show_instructions = False
        
def on_update(self, delta_time: float) -> None:
    """Manages the timer to toggle the instructions

    Arguments:
        delta_time -- time passed since last update
    """

    # First, count down the time
    self.display_timer -= delta_time

    # If the timer has run out, we toggle the instructions
    if self.display_timer < 0:

        # Toggle whether to show the instructions
        self.show_instructions = not self.show_instructions

        # And reset the timer so the instructions flash slowly
        self.display_timer = 1.0
        
def on_draw(self) -> None:
    # Start the rendering loop
    arcade.start_render()

    # Draw a rectangle filled with our title image
    arcade.draw_texture_rectangle(
        center_x=SCREEN_WIDTH / 2,
        center_y=SCREEN_HEIGHT / 2,
        width=SCREEN_WIDTH,
        height=SCREEN_HEIGHT,
        texture=self.title_image,
    )

    # Should we show our instructions?
    if self.show_instructions:
        arcade.draw_text(
            "Enter to Start | I for Instructions",
            start_x=100,
            start_y=220,
            color=arcade.color.INDIGO,
            font_size=40,
        )
        
def on_key_press(self, key: int, modifiers: int) -> None:
    """Resume the game when the user presses ESC again

    Arguments:
        key -- Which key was pressed
        modifiers -- What modifiers were active
    """
    if key == arcade.key.RETURN:
        game_view = PlatformerView()
        game_view.setup()
        self.window.show_view(game_view)
    elif key == arcade.key.I:
        instructions_view = InstructionsView()
        self.window.show_view(instructions_view)
        
if __name__ == "__main__":
    window = arcade.Window(
        width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title=SCREEN_TITLE
    )
    title_view = TitleView()
    window.show_view(title_view)
    arcade.run()
