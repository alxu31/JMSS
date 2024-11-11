#include <SFML/Graphics.hpp>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <cmath>

// Constants for grid size and window dimensions
const int gridSize = 401;  // Larger grid size for more expansion
const int windowSize = 500; // Window dimensions remain the same
const int cellSize = windowSize / gridSize;

std::vector<std::vector<bool>> grid(gridSize, std::vector<bool>(gridSize, false)); // 2D grid

// Calculate distance from the center to a point
float distanceFromCenter(int x, int y) {
    int centerX = gridSize / 2;
    int centerY = gridSize / 2;
    return std::sqrt((x - centerX) * (x - centerX) + (y - centerY) * (y - centerY));
}

// Randomly introduce a new particle at the boundary
sf::Vector2i introduceParticle() {
    int side = rand() % 4;
    switch (side) {
        case 0: return sf::Vector2i(0, rand() % gridSize);        // Top
        case 1: return sf::Vector2i(gridSize - 1, rand() % gridSize);  // Bottom
        case 2: return sf::Vector2i(rand() % gridSize, 0);        // Left
        case 3: return sf::Vector2i(rand() % gridSize, gridSize - 1);  // Right
        default: return sf::Vector2i(0, 0);
    }
}

// Perform random walk on the particle
void randomWalk(sf::Vector2i &particle) {
    int direction = rand() % 4;
    switch (direction) {
        case 0: particle.x = std::min(gridSize - 1, particle.x + 1); break; // Right
        case 1: particle.x = std::max(0, particle.x - 1); break;            // Left
        case 2: particle.y = std::min(gridSize - 1, particle.y + 1); break; // Down
        case 3: particle.y = std::max(0, particle.y - 1); break;            // Up
    }
}

void biasedWalk(sf::Vector2i &particle, sf::Vector2i center) {
    // Random walk but with a bias toward or away from the center
    int direction = rand() % 100;
    if (direction < 40) {
        // 40% chance to move towards the center
        if (particle.x < center.x) particle.x++;
        else if (particle.x > center.x) particle.x--;
        if (particle.y < center.y) particle.y++;
        else if (particle.y > center.y) particle.y--;
    } else {
        // Normal random walk
        randomWalk(particle);
    }
}

// Check if a particle is adjacent to the cluster
bool adjacentToCluster(sf::Vector2i particle) {
    int x = particle.x;
    int y = particle.y;
    return (x > 0 && grid[x - 1][y]) || (x < gridSize - 1 && grid[x + 1][y]) ||
           (y > 0 && grid[x][y - 1]) || (y < gridSize - 1 && grid[x][y + 1]);
}

// Calculate color based on distance from the center
sf::Color getColorBasedOnDistance(int x, int y) {
    float maxDistance = std::sqrt(2) * (gridSize / 2); // Max distance is from center to a corner
    float distance = distanceFromCenter(x, y);
    float ratio = distance / maxDistance;

    sf::Uint8 red = static_cast<sf::Uint8>(255 * ratio);
    sf::Uint8 blue = static_cast<sf::Uint8>(255 * (1 - ratio));
    
    return sf::Color(red, 0, blue); // Gradient from blue (center) to red (edge)
}

// Add new particle to the cluster
void addParticleToCluster() {
    sf::Vector2i particle = introduceParticle();
    sf::Vector2i center(gridSize / 2, gridSize / 2);  // Center of the grid

    // Perform biased walk until the particle sticks to the cluster
    while (true) {
        biasedWalk(particle, center);  // Replaced randomWalk with biasedWalk
        if (adjacentToCluster(particle)) {
            grid[particle.x][particle.y] = true;
            break;
        }
    }
}


int main() {
    // Initialize random seed
    std::srand(static_cast<unsigned>(std::time(0)));

    // Set up the SFML window
    sf::RenderWindow window(sf::VideoMode(windowSize, windowSize), "DLA Simulation with Color Gradient");
    window.setFramerateLimit(60);

    // Set the center seed particle
    grid[gridSize / 2][gridSize / 2] = true;

    // Calculate the offset to center the grid in the window
    int xOffset = (windowSize - gridSize * cellSize) / 2;
    int yOffset = (windowSize - gridSize * cellSize) / 2;

    // Main simulation loop
    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed) {
                window.close();
            }
        }

        // Add multiple particles per frame to speed up simulation
        for (int i = 0; i < 10; ++i) {
            addParticleToCluster(); // Adding 10 particles per frame
        }

        // Clear the window
        window.clear(sf::Color::Black);

        // Draw the grid with color gradient based on distance from center
        sf::RectangleShape cell(sf::Vector2f(cellSize, cellSize));
        for (int x = 0; x < gridSize; x++) {
            for (int y = 0; y < gridSize; y++) {
                if (grid[x][y]) {
                    cell.setPosition(xOffset + x * cellSize, yOffset + y * cellSize); // Centered position
                    cell.setFillColor(getColorBasedOnDistance(x, y)); // Color changes as it expands
                    window.draw(cell);
                }
            }
        }

        // Display the updated window
        window.display();
    }

    return 0;
}
