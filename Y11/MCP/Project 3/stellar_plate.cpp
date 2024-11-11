#include <SFML/Graphics.hpp>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <iostream>

// Constants for grid size and window dimensions
const int gridSize = 301;
const int windowSize = 600;
const int cellSize = 2;  // Size of each particle

// 2D grid to store particle positions
std::vector<std::vector<bool>> grid(gridSize, std::vector<bool>(gridSize, false));

// Function to calculate distance from the center
float distanceFromCenter(int x, int y) {
    int centerX = gridSize / 2;
    int centerY = gridSize / 2;
    return std::sqrt((x - centerX) * (x - centerX) + (y - centerY) * (y - centerY));
}

// Introduce a new particle at the boundary with symmetry
sf::Vector2i introduceParticle() {
    int centerX = gridSize / 2;
    int centerY = gridSize / 2;

    // Generate a random angle for six-fold symmetry
    float angle = (rand() % 6) * (M_PI / 3);  // 6 possible directions (0, 60, 120, ... degrees)
    int radius = gridSize / 2 - 1;

    // Convert polar coordinates to Cartesian
    int x = centerX + static_cast<int>(radius * std::cos(angle));
    int y = centerY + static_cast<int>(radius * std::sin(angle));

    // Ensure the particle is within bounds
    x = std::max(0, std::min(gridSize - 1, x));
    y = std::max(0, std::min(gridSize - 1, y));

    return sf::Vector2i(x, y);
}

// Perform random walk biased towards arms of the snowflake
void biasedRandomWalk(sf::Vector2i &particle) {
    int centerX = gridSize / 2;
    int centerY = gridSize / 2;

    int direction = rand() % 6;  // Use 6 directions for biasing towards snowflake arms
    switch (direction) {
        case 0: particle.x = std::min(gridSize - 1, particle.x + 1); break; // Right
        case 1: particle.x = std::max(0, particle.x - 1); break;            // Left
        case 2: particle.y = std::min(gridSize - 1, particle.y + 1); break; // Down
        case 3: particle.y = std::max(0, particle.y - 1); break;            // Up
        case 4:  // Bias towards diagonal (arm direction)
            if (particle.x > centerX) particle.x--;
            if (particle.y > centerY) particle.y--;
            break;
        case 5:  // Another diagonal for symmetry
            if (particle.x < centerX) particle.x++;
            if (particle.y < centerY) particle.y++;
            break;
    }

    // Ensure the particle stays within bounds
    particle.x = std::max(0, std::min(gridSize - 1, particle.x));
    particle.y = std::max(0, std::min(gridSize - 1, particle.y));
}

// Check if a particle is adjacent to the cluster
bool adjacentToCluster(sf::Vector2i particle) {
    int x = particle.x;
    int y = particle.y;
    return (x > 0 && grid[x - 1][y]) || (x < gridSize - 1 && grid[x + 1][y]) ||
           (y > 0 && grid[x][y - 1]) || (y < gridSize - 1 && grid[x][y + 1]);
}

// Apply hexagonal symmetry to the grid
void applyHexagonalSymmetry(int x, int y) {
    int centerX = gridSize / 2;
    int centerY = gridSize / 2;

    // Calculate relative coordinates from center
    int relX = x - centerX;
    int relY = y - centerY;

    // Apply symmetry in six directions (60-degree rotations)
    for (int i = 0; i < 6; ++i) {
        float angle = i * (M_PI / 3);
        int symX = centerX + static_cast<int>(relX * std::cos(angle) - relY * std::sin(angle));
        int symY = centerY + static_cast<int>(relX * std::sin(angle) + relY * std::cos(angle));
        
        // Ensure symmetrical points are within bounds
        if (symX >= 0 && symX < gridSize && symY >= 0 && symY < gridSize) {
            grid[symX][symY] = true;
        }
    }
}

// Add a particle to the cluster with symmetry
void addParticleToCluster() {
    sf::Vector2i particle = introduceParticle();

    // Perform random walk until the particle sticks to the cluster
    while (true) {
        biasedRandomWalk(particle);
        if (adjacentToCluster(particle)) {
            grid[particle.x][particle.y] = true;
            applyHexagonalSymmetry(particle.x, particle.y);  // Apply hexagonal symmetry
            break;
        }
    }
}

// Main function to set up the window and start the simulation
int main() {
    // Initialize random seed
    std::srand(static_cast<unsigned>(std::time(0)));

    // Create the SFML window
    sf::RenderWindow window(sf::VideoMode(windowSize, windowSize), "Stellar Plate Snowflake DLA");
    window.setFramerateLimit(60);

    // Seed particle in the center of the grid
    grid[gridSize / 2][gridSize / 2] = true;

    // Calculate offsets to center the grid in the window
    int xOffset = (windowSize - gridSize * cellSize) / 2;
    int yOffset = (windowSize - gridSize * cellSize) / 2;

    // Main loop
    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed) {
                window.close();
            }
        }

        // Add multiple particles per frame to speed up simulation
        for (int i = 0; i < 500; ++i) {  // Increased particle count
            addParticleToCluster();
        }

        // Clear the window
        window.clear(sf::Color::Black);

        // Draw the grid
        sf::RectangleShape cell(sf::Vector2f(cellSize, cellSize));
        cell.setFillColor(sf::Color::White);  // Snowflake particles are white
        for (int x = 0; x < gridSize; x++) {
            for (int y = 0; y < gridSize; y++) {
                if (grid[x][y]) {
                    // Center the particle in the window
                    cell.setPosition(xOffset + x * cellSize, yOffset + y * cellSize);
                    window.draw(cell);
                }
            }
        }

        // Display the updated window
        window.display();
    }

    return 0;
}
