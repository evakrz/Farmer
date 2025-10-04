# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a save file for "The Farmer Was Replaced" game, containing automation scripts written in a Python-like language. The code automates farming tasks like harvesting grass, wood, carrots, pumpkins, and dinosaurs using a drone that moves around a grid-based farm.

## Game API Reference

The game provides a custom Python-like API defined in `__builtins__.py`. Key concepts:

- **Entities**: Things that can be planted (Grass, Tree, Bush, Carrot, Pumpkin, Dinosaur, etc.)
- **Items**: Resources obtained from harvesting (Hay, Wood, Carrot, Pumpkin, Bone, etc.)
- **Grounds**: Terrain types (Grassland, Soil)
- **Directions**: North, South, East, West for drone movement
- **Hats**: Different modes (Straw_Hat for farming, Dinosaur_Hat for dinosaur game)

Core game functions include: `harvest()`, `can_harvest()`, `plant()`, `move()`, `till()`, `get_pos_x()`, `get_pos_y()`, `get_world_size()`, `get_entity_type()`, `get_ground_type()`, `num_items()`, `change_hat()`, `clear()`, `measure()`

All actions have tick costs (performance metrics). Most actions take 200 ticks on success, 1 tick on failure.

## Code Architecture

The codebase uses a modular structure:

1. **main.py**: Main orchestration loop that coordinates all farming activities
   - Calls specialized farming functions from imported modules
   - Uses `get_cost()` to check unlock requirements before running tasks
   - Runs in infinite loop: Grass → Wood → Carrots → Pumpkins → Dinosaurs

2. **Resource-specific modules**: Each resource has its own automation function
   - **Grass.py**: `AutoGrass(max_amount)` - Harvests grass for hay
   - **Tree.py**: `AutoWood(max_amount)` - Plants trees/bushes in checkerboard pattern
   - **Carrots.py**: `AutoCarrots(max_amount)` - Manages carrot farming on soil
   - **Pumpkins.py**: `AutoPumpkin(max_value)` - Complex pumpkin growth/harvest logic
   - **Dinosaurs.py**: `AutoDinos(max_value)` - Dinosaur game navigation patterns

3. **Common patterns**:
   - Functions use `while num_items(Item) < max_amount` loops
   - Nested loops iterate through grid: outer loop moves East, inner loop moves North
   - Ground type checking with `get_ground_type()` to handle Grassland vs Soil
   - `till()` converts between Grassland and Soil
   - `can_harvest()` checks before `harvest()` to avoid wasting ticks

## Key Implementation Details

- **Grid traversal**: The drone wraps around edges (toroidal grid)
- **Checkerboard planting** (Tree.py): Trees on even coordinates, bushes on odd coordinates to optimize growth
- **Pumpkin mechanics**: Pumpkins grow together when adjacent; harvest yield is cubed based on cluster size
- **Dinosaur game**: Uses hat switching (`change_hat()`) to enter/exit dinosaur mode; complex serpentine movement patterns for even/odd grid sizes
- **Performance**: All functions return early when goals are met to minimize tick usage

## Development Notes

- The game language is Python-like but NOT actual Python (see `__builtins__.py` header comment)
- Type hints in `__builtins__.py` are for editor support only
- Resource thresholds in main.py determine progression through different farming phases
- Each Auto function is designed to be idempotent and safe to call repeatedly
