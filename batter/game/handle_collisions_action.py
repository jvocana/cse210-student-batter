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
        
        for x in cast['brick']:   
            brick_x = x.get_position().get_x()
            brick_y = x.get_position().get_y()

            if ball_position.get_x() == brick_x and ball_position.get_y() == brick_y:
                x_point = ball.get_velocity().get_x()
                y = ball.get_velocity().get_y()
                new_velocity = Point(x_point, abs(y))
                ball.set_velocity(new_velocity)
                #remove the brick
                cast['brick'].remove(x)
                return ball.set_velocity(new_velocity)
            
            
       
        # if statements for collision with the walls       
        #if the ball hits the sides, have it bounce
        
        # if the ball hits right side
        if ball_position.get_x() == constants.MAX_X - 1:
            x = ball.get_velocity().get_x()
            y = ball.get_velocity().get_y()
            new_velocity = Point(-abs(x), y)
            ball.set_velocity(new_velocity)
        
        # if the ball hits the left side
        if ball_position.get_x() == 1:
            x = ball.get_velocity().get_x()
            y = ball.get_velocity().get_y()
            new_velocity = Point(abs(x), y)
            ball.set_velocity(new_velocity)

        # if the ball hits the top   
        if ball_position.get_y() == 1:
            x = ball.get_velocity().get_x()
            y = ball.get_velocity().get_y()
            new_velocity = Point(x, abs(y))
            ball.set_velocity(new_velocity)
            
            
        # if the ball goes off screen on the bottom, then game over
        if ball_position.get_y() == constants.MAX_Y - 1:
            sys.exit()
        
            