import random
import sys
from game import constants
from game.action import Action
from game.point import Point

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        # ball position
        ball = cast['ball'] [0]
        ball_position = ball.get_position()
        
        #paddle position
        paddle = cast['paddle'] [0]
        paddle_position = paddle.get_position()

        # brick position
        bricks = cast['brick'] [0]
        brick_position = bricks.get_position()
        

        
        # if the ball hits the paddle, reverse its direction
        if ball_position.get_y() == paddle_position.get_y() - 1:
            paddle_min_x = paddle_position.get_x()
            paddle_max_x = paddle_min_x + 10
            if ball_position.get_x() >= paddle_min_x and ball_position.get_x() <= paddle_max_x:
                new_velocity = ball.get_velocity().reverse()
                ball.set_velocity(new_velocity)
        
        # if the ball hits a brick, reverse its direction
        
            
            # if ball_position.get_y() == brick_position.get_y() - 1:
            #     if ball_position.get_x() == brick_position.get_x() - 1:
            #         new_velocity = ball.get_velocity().reverse()
            #         ball.set_velocity(new_velocity)
       
        # if the ball hits the sides, have it bounce
        # if ball_position.get_x() == (constants.MAX_X - 1) or ball_position.get_x() == 1 or ball_position.get_y() == 1:
        #     new_y = ball.get_velocity().get_y()
        #     x = ball.get_velocity().reverse()
        #     new_x = x.get_x()
        #     ball.set_velocity(Point(x = new_x, y = new_y))
        
        # if the ball goes off screen on the bottom, then game over
        if ball_position.get_y() == constants.MAX_Y - 1:
            sys.exit()
            