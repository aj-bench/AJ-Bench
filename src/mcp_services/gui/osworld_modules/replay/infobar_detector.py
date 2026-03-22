#!/usr/bin/env python3
"""
General infobar detector.
Ported from the original mcpmark osworld_judge implementation.
Supports parsing accessibility trees in both XML and table formats,
and locating the close button of infobars based purely on layout features.
"""

import re
import xml.etree.ElementTree as ET
from typing import List, Dict, Tuple, Optional
import logging

logger = logging.getLogger(__name__)


class InfobarDetector:
    """Generic infobar detector supporting both XML and table formats."""

    def __init__(self, screen_width: int = 1920, screen_height: int = 1080, app_type: str = ""):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.app_type = app_type.lower()

        # Layout thresholds for infobar region
        self.INFOBAR_Y_MIN = 140
        self.INFOBAR_Y_MAX = 280
        self.INFOBAR_X_START_MAX = 500
        self.INFOBAR_MIN_WIDTH = 500
        self.INFOBAR_MIN_HEIGHT = 15
        self.INFOBAR_MAX_HEIGHT = 50

        # Close button X range depends on application type
        if "calc" in self.app_type:
            # Calculator: close button near far right.
            self.CLOSE_BUTTON_X_MIN = 1800
            self.CLOSE_BUTTON_X_MAX = 1860
        else:
            # Writer/Impress: close button more to the middle-right.
            self.CLOSE_BUTTON_X_MIN = 1370
            self.CLOSE_BUTTON_X_MAX = 1450

    def detect_tree_format(self, tree_str: str) -> str:
        """Detect whether accessibility tree is XML or table format."""
        tree_str_stripped = tree_str.strip()
        if tree_str_stripped.startswith("<"):
            return "xml"
        return "table"

    def parse_xml_tree(self, tree_str: str) -> List[Dict]:
        """Parse XML-format accessibility tree into a flat list of elements."""
        elements: List[Dict] = []
        try:
            root = ET.fromstring(tree_str)
            for elem in root.iter():
                screencoord = elem.get(
                    "{https://accessibility.ubuntu.example.org/ns/component}screencoord"
                )
                size = elem.get(
                    "{https://accessibility.ubuntu.example.org/ns/component}size"
                )

                if screencoord and size:
                    coord_match = re.match(r"\((\d+), (\d+)\)", screencoord)
                    size_match = re.match(r"\((\d+), (\d+)\)", size)

                    if coord_match and size_match:
                        x, y = int(coord_match.group(1)), int(coord_match.group(2))
                        w, h = int(size_match.group(1)), int(size_match.group(2))

                        tag = elem.tag.split("}")[-1] if "}" in elem.tag else elem.tag
                        name = elem.get("name", "")
                        text = elem.text.strip() if elem.text else ""

                        elements.append(
                            {
                                "tag": tag,
                                "name": name,
                                "text": text,
                                "x": x,
                                "y": y,
                                "w": w,
                                "h": h,
                                "right": x + w,
                                "bottom": y + h,
                                "center_x": x + w // 2,
                                "center_y": y + h // 2,
                            }
                        )
        except Exception as e:
            logger.error(f"Failed to parse XML-format a11y tree: {e}")
        return elements

    def parse_table_tree(self, tree_str: str) -> List[Dict]:
        """Parse TSV-table-format accessibility tree into a flat list of elements."""
        lines = tree_str.strip().split("\n")
        elements: List[Dict] = []

        for line_num, line in enumerate(lines[1:], 1):  # skip header
            fields = line.split("\t")
            if len(fields) >= 7:
                tag = fields[0]
                name = fields[1]
                text = fields[2]

                pos_match = re.search(r"\((\d+), (\d+)\)", fields[5])
                size_match = re.search(r"\((\d+), (\d+)\)", fields[6])

                if pos_match and size_match:
                    x, y = int(pos_match.group(1)), int(pos_match.group(2))
                    w, h = int(size_match.group(1)), int(size_match.group(2))

                    elements.append(
                        {
                            "line_num": line_num,
                            "tag": tag,
                            "name": name,
                            "text": text,
                            "x": x,
                            "y": y,
                            "w": w,
                            "h": h,
                            "right": x + w,
                            "bottom": y + h,
                            "center_x": x + w // 2,
                            "center_y": y + h // 2,
                        }
                    )

        return elements

    def parse_a11y_tree(self, tree_str: str) -> List[Dict]:
        """Auto-detect format and parse accessibility tree into elements."""
        format_type = self.detect_tree_format(tree_str)
        if format_type == "xml":
            logger.debug("Detected XML-format a11y tree")
            return self.parse_xml_tree(tree_str)
        logger.debug("Detected table-format a11y tree")
        return self.parse_table_tree(tree_str)

    def is_infobar_text_element(self, elem: Dict) -> bool:
        """Heuristically decide whether an element is the infobar text block."""
        if elem["tag"] != "text":
            return False
        if not (self.INFOBAR_Y_MIN <= elem["y"] <= self.INFOBAR_Y_MAX):
            return False
        if elem["w"] < self.INFOBAR_MIN_WIDTH:
            return False
        if not (self.INFOBAR_MIN_HEIGHT <= elem["h"] <= self.INFOBAR_MAX_HEIGHT):
            return False
        if elem["x"] > self.INFOBAR_X_START_MAX:
            return False
        return True

    def find_close_button_for_infobar(
        self, infobar_text_elem: Dict, all_elements: List[Dict]
    ) -> Optional[Dict]:
        """Locate the close button of the infobar using layout-only heuristics."""
        y_tolerance = 30
        for elem in all_elements:
            if elem["tag"] in ["tool-bar", "push-button"]:
                if self.CLOSE_BUTTON_X_MIN <= elem["x"] <= self.CLOSE_BUTTON_X_MAX:
                    if abs(elem["y"] - infobar_text_elem["y"]) <= y_tolerance:
                        if elem["w"] <= 30 and elem["h"] <= 30:
                            return elem
        return None

    def detect_infobars(self, a11y_tree_str: str) -> List[Dict]:
        """Detect all infobar regions based on layout-only features."""
        elements = self.parse_a11y_tree(a11y_tree_str)
        infobars: List[Dict] = []
        for elem in elements:
            if self.is_infobar_text_element(elem):
                infobars.append(elem)
        return infobars

    def has_infobars(self, a11y_tree_str: str) -> bool:
        """Return True if any infobars are detected."""
        return len(self.detect_infobars(a11y_tree_str)) > 0

    def get_topmost_infobar_close_coord(
        self, a11y_tree_str: str
    ) -> Optional[Tuple[int, int]]:
        """Return (x, y) of the close button for the topmost infobar, if any."""
        elements = self.parse_a11y_tree(a11y_tree_str)
        infobar_text_elems = [
            e for e in elements if self.is_infobar_text_element(e)
        ]

        if not infobar_text_elems:
            return None

        # Choose the highest (smallest y) infobar as the topmost.
        topmost = min(infobar_text_elems, key=lambda e: e["y"])
        close_elem = self.find_close_button_for_infobar(topmost, elements)
        if not close_elem:
            return None

        return close_elem["center_x"], close_elem["center_y"]

