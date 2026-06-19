"""Pytest setup.

This file sitting at the project root makes pytest add the root to the import
path, so tests can write `import board` and `from solve.solver import solve`
without any extra packaging. It is intentionally empty otherwise.
"""
