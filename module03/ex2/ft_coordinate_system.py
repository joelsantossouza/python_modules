import math

if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    checkpoint = (0, 0, 0)

    point = (10, 20, 5)
    print(f"Position created: {point}")
    distance: float = math.sqrt(point[0]**2 + point[1]**2 + point[2]**2)
    print(f"Distance between {checkpoint} and {point}: {distance:.2f}\n")

    coordinates: str = "3,4,0"
    print(f"Parsing coordinates: \"{coordinates}\"")
    x, y, z = coordinates.split(",")
    try:
        x: int = int(x)
        y: int = int(y)
        z: int = int(z)
    except Exception as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: {e.args}")
    else:
        point = (x, y, z)
        print(f"Parsed position: {point}")
        distance: float = math.sqrt(point[0]**2 + point[1]**2 + point[2]**2)
        print(f"Distance between {checkpoint} and {point}: {distance:.1f}\n")

    coordinates: str = "abc,def,ghi"
    print(f"Parsing invalid coordinates: \"{coordinates}\"")
    x, y, z = coordinates.split(",")
    try:
        x: int = int(x)
        y: int = int(y)
        z: int = int(z)
    except Exception as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: {e.args}")
    else:
        point = (x, y, z)
        print(f"Parsed position: {point}")
        distance: float = math.sqrt(point[0]**2 + point[1]**2 + point[2]**2)
        print(f"Distance between {checkpoint} and {point}: {distance:.2f}\n")

    print("\nUnpacking demonstration:")
    x, y, z = point
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={point[0]}, Y={point[1]}, Z={point[2]}")
