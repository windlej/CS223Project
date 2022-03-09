class PlatformerView(arcade.View):
    def __init__(self) -> None:
        super().__init__()

if __name__ == "__main__":
    window = arcade.Window(
        width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title=SCREEN_TITLE
    )
    platform_view = PlatformerView()
    platform_view.setup()
    window.show_view(platform_view)
    arcade.run()
