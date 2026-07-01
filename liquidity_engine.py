class LiquidityEngine:
    """
    Detects liquidity sweeps (stop hunts).
    """

    def detect_sweep(self, candles):
        if len(candles) < 3:
            return False

        last = candles[-1]
        prev_high = max(c['high'] for c in candles[-10:-1])

        # sweep above high then rejection
        if last['high'] > prev_high and last['close'] < prev_high:
            return True

        return False
