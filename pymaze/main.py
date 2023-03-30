from __future__ import absolute_import
from src.maze_manager import MazeManager
from src.maze import Maze


if __name__ == "__main__":
    for i in range(1000):

        # The easiest way to use the library is through the Manager class. It acts as the glue between
        # The visualization, solver, and maze classes. Mazes inside the manager have unique ids that we use
        # to specify particular mazes.
        manager = MazeManager()

        # We can add mazes to the manager two different ways.
        # The first way, we specify the maze dimensions. The maze that is created gets returned back to you.
        size = 12
        maze = manager.add_maze(size, size, i)

        # The second way is by creating a maze, and then adding it to the manager. Doing this will require you to add
        # from src.maze import Maze
        # to your imports. Because the ids need to be unique, the manager will ensure this happens. It may change the
        # id of the maze that was passed in, so we assign it to the return value to make sure we're using the updated maze.
        # maze2 = Maze(10, 10)
        # maze2 = manager.add_existing_maze(maze2)

        # Once we have a maze in the manager, we can tell the manager to solve it with a particular algorithm.
        #manager.solve_maze(maze.id, "BreadthFirst")
        #manager.solve_maze(maze.id, "BiDirectional")
        manager.solve_maze(maze.id, "DepthFirstBacktracker")

        # If we want to save the maze & maze solution images along with their animations, we need to let the manager know.
        file_name = f"maze_12_g/{size}_{i}"
        manager.set_filename(file_name)

        # To see the unsolved maze, call
        manager.show_maze(maze.id)

        # You can also set the size of the cell by passing show_maze's second argument. The default is 1.
        # manager.show_maze(maze.id, 2)

        # To show an animation of how the maze was generated, use the following line
        #manager.show_generation_animation(maze.id)

        # You can also see an animation of how the solver went about finding the end
        #manager.show_solution_animation(maze.id)
        file_name = f"maze_12_s/{size}_{i}"
        manager.set_filename(file_name)
        # Finally, you can show an image of the maze with the solution path overlaid. All of these display
        # functions will save the figure if MazeManager::set_filename has been set.
        manager.show_solution(maze.id)