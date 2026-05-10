from src import exp
from src import gui

def main() -> None:
    """
    Runs the program.

    Args:
        None

    Returns:
        None
    """
    the_gui = gui.Gui()
    the_experiment = exp.Exp(the_gui)
    the_gui.root.mainloop()

if __name__ == "__main__":
    main()