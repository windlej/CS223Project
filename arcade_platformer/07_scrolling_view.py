# Player constants
GRAVITY = 1.0
PLAYER_START_X = 65
PLAYER_START_Y = 256
PLAYER_MOVE_SPEED = 10
PLAYER_JUMP_SPEED = 20

# Viewport margins
# How close do we have to be to scroll the viewport?
LEFT_VIEWPORT_MARGIN = 50
RIGHT_VIEWPORT_MARGIN = 300
TOP_VIEWPORT_MARGIN = 150
BOTTOM_VIEWPORT_MARGIN = 150

# Move the player sprite back to the beginning
self.player.center_x = PLAYER_START_X
self.player.center_y = PLAYER_START_Y
self.player.change_x = 0
self.player.change_y = 0

# Reset the viewport
self.view_left = 0
self.view_bottom = 0

# Set the background color
background_color = arcade.color.FRESH_AIR
if game_map.background_color:
    background_color = game_map.background_color
arcade.set_background_color(background_color)

# Find the edge of the map to control viewport scrolling
self.map_width = (
    game_map.map_size.width - 1
) * game_map.tile_size.width

def scroll_viewport(self) -> None:
    """Scrolls the viewport when the player gets close to the edges"""
    # Scroll left
    # Find the current left boundary
    left_boundary = self.view_left + LEFT_VIEWPORT_MARGIN

    # Are we to the left of this boundary? Then we should scroll left.
    if self.player.left < left_boundary:
        self.view_left -= left_boundary - self.player.left
        # But don't scroll past the left edge of the map
        if self.view_left < 0:
            self.view_left = 0

    # Scroll right
    # Find the current right boundary
    right_boundary = self.view_left + SCREEN_WIDTH - RIGHT_VIEWPORT_MARGIN

    # Are we to the right of this boundary? Then we should scroll right.
    if self.player.right > right_boundary:
        self.view_left += self.player.right - right_boundary
        # Don't scroll past the right edge of the map
        if self.view_left > self.map_width - SCREEN_WIDTH:
            self.view_left = self.map_width - SCREEN_WIDTH

    # Scroll up
    top_boundary = self.view_bottom + SCREEN_HEIGHT - TOP_VIEWPORT_MARGIN
    if self.player.top > top_boundary:
        self.view_bottom += self.player.top - top_boundary

    # Scroll down
    bottom_boundary = self.view_bottom + BOTTOM_VIEWPORT_MARGIN
    if self.player.bottom < bottom_boundary:
        self.view_bottom -= bottom_boundary - self.player.bottom

    # Only scroll to integers. Otherwise we end up with pixels that
    # don't line up on the screen.
    self.view_bottom = int(self.view_bottom)
    self.view_left = int(self.view_left)

    # Do the scrolling
    arcade.set_viewport(
        left=self.view_left,
        right=SCREEN_WIDTH + self.view_left,
        bottom=self.view_bottom,
        top=SCREEN_HEIGHT + self.view_bottom,
    )
    
# Scroll right
# Find the current right boundary
right_boundary = self.view_left + SCREEN_WIDTH - RIGHT_VIEWPORT_MARGIN

# Are we right of this boundary? Then we should scroll right.
if self.player.right > right_boundary:
    self.view_left += self.player.right - right_boundary
    # Don't scroll past the right edge of the map
    if self.view_left > self.map_width - SCREEN_WIDTH:
        self.view_left = self.map_width - SCREEN_WIDTH
        
if goals_hit:
    # Play the victory sound
    self.victory_sound.play()

    # Set up the next level
    self.level += 1
    self.setup()

# Set the viewport, scrolling if necessary
self.scroll_viewport()
