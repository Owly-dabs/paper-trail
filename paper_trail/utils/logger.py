import logging

def setup_logging(log_file: str = None, level: int = logging.INFO):
    """
    Sets up consistent logging across your project.
    
    Parameters:
    - log_file: Optional path to a log file.
    - level: Logging level (default INFO).
    """
    handlers = [logging.StreamHandler()]
    if log_file:
        handlers.append(logging.FileHandler(log_file))

    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=handlers,
    )

    logging.info("Logging initialized.")