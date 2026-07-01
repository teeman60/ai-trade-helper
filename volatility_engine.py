import numpy as np

class VolatilityEngine:
    """
    Core engine for IV, RV, and regime classification.
    This is the MOST IMPORTANT module in the system.
    """

    def compute_realized_vol(self, returns):
        return np.std(returns) * np.sqrt(252)

    def iv_percentile(self, current_iv, historical_iv):
        historical_iv = np.array(historical_iv)
        return (np.sum(historical_iv < current_iv) / len(historical_iv)) * 100

    def iv_rv_ratio(self, iv, rv):
        return iv / rv if rv != 0 else 0

    def classify_regime(self, iv_pct):
        if iv_pct < 25:
            return "LOW_VOL"
        elif iv_pct < 70:
            return "NORMAL_VOL"
        else:
            return "HIGH_VOL"
