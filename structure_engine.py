class StructureEngine:
    """
    Market structure detection:
    - Higher Highs / Higher Lows
    - Break of Structure (BOS)
    - Liquidity sweeps (simplified)
    """

    def detect_structure(self, candles):
        highs = [c['high'] for c in candles]
        lows = [c['low'] for c in candles]

        structure = {
            "trend": None,
            "bos": False,
            "sweep": False
        }

        if len(highs) < 5:
            return structure

        if highs[-1] > max(highs[-5:-1]):
            structure["trend"] = "BULLISH"
            structure["bos"] = True

        if lows[-1] < min(lows[-5:-1]):
            structure["trend"] = "BEARISH"
            structure["bos"] = True

        return structure
