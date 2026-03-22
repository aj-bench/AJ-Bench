#!/usr/bin/env python3
"""
Global click coordinates configuration module.
Unified management of click coordinate configurations for all applications.
"""

import os
import json
from typing import Dict, Tuple

class ClickCoordinates:
    """Click coordinates configuration class."""
    
    def __init__(self):
        self.config_file = os.path.join(os.path.dirname(__file__), "click_coordinates.json")
        self._coordinates = None
    
    @property
    def coordinates(self) -> Dict[str, Tuple[int, int]]:
        """Get coordinate configuration."""
        if self._coordinates is None:
            self._coordinates = self._load_coordinates()
        return self._coordinates
    
    def _load_coordinates(self) -> Dict[str, Tuple[int, int]]:
        """Load coordinates from configuration file."""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    return {app: tuple(coord) for app, coord in data.items()}
            except Exception as e:
                print(f"Warning: Failed to load coordinate configuration file: {e}")
        
        return {
            "libreoffice_writer": (1845, 185),
            "libreoffice_calc": (1850, 220),
            "libreoffice_impress": (1395, 190)
        }
    
    def get_coordinate(self, app_type: str, screen_width: int = 1920, screen_height: int = 1080) -> Tuple[int, int]:
        """
        Get click coordinates for specified application.
        
        Args:
            app_type: Application type.
            screen_width: Screen width.
            screen_height: Screen height.
            
        Returns:
            (x, y) coordinate tuple.
        """
        base_coord = self.coordinates.get(app_type, (1780, 190))
        
        if screen_width != 1920 or screen_height != 1080:
            scale_x = screen_width / 1920
            scale_y = screen_height / 1080
            scaled_x = int(base_coord[0] * scale_x)
            scaled_y = int(base_coord[1] * scale_y)
            return (scaled_x, scaled_y)
        
        return base_coord
    
    def update_coordinate(self, app_type: str, x: int, y: int):
        """Update coordinates and save to file."""
        if self._coordinates is None:
            self._coordinates = self._load_coordinates()
        
        self._coordinates[app_type] = (x, y)
        
        try:
            data = {app: list(coord) for app, coord in self._coordinates.items()}
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"Updated {app_type} coordinates to: ({x}, {y})")
        except Exception as e:
            print(f"Failed to save coordinates: {e}")
    
    def list_coordinates(self):
        """List all coordinates."""
        print("Current coordinate configuration:")
        for app_type, coord in self.coordinates.items():
            print(f"  {app_type}: {coord}")
    
    def detect_app_type_from_config(self, task_config: Dict) -> str:
        """
        Detect application type from task configuration.
        
        Args:
            task_config: Task configuration dictionary.
            
        Returns:
            Application type string.
        """
        snapshot = task_config.get("snapshot", "").lower()
        if "writer" in snapshot:
            return "libreoffice_writer"
        elif "calc" in snapshot:
            return "libreoffice_calc"
        elif "impress" in snapshot:
            return "libreoffice_impress"
        
        related_apps = task_config.get("related_apps", [])
        for app in related_apps:
            app_lower = app.lower()
            if "writer" in app_lower:
                return "libreoffice_writer"
            elif "calc" in app_lower:
                return "libreoffice_calc"
            elif "impress" in app_lower:
                return "libreoffice_impress"
        
        return "libreoffice_writer"

click_coordinates = ClickCoordinates()

