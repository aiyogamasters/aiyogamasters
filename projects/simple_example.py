"""Simple example module."""

def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Namaste, {name}!"

if __name__ == "__main__":
    print(greet("World"))
