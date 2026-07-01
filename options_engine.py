class OptionsEngine:
    """
    Ranks options contracts using:
    - IV regime
    - delta alignment
    - liquidity
    - spreads
    """

    def rank(self, chain, signal, iv_pct):

        results = []

        for c in chain:

            if c['open_interest'] < 200:
                continue

            if c['spread_pct'] > 0.08:
                continue

            # IV-aware delta selection
            if iv_pct < 25:
                valid_delta = (0.5, 0.7)
            elif iv_pct > 70:
                valid_delta = (0.65, 0.85)
            else:
                valid_delta = (0.6, 0.75)

            if valid_delta[0] <= abs(c['delta']) <= valid_delta[1]:
                results.append(c)

        return sorted(results, key=lambda x: x['volume'], reverse=True)[:3]
