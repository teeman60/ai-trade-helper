class Backtester:
    """
    Event-driven backtesting skeleton.
    Future upgrade: walk-forward + ML evaluation.
    """

    def run(self, strategy, historical_data):

        results = []

        for i in range(100, len(historical_data)):

            window = historical_data[:i]

            signal = strategy.evaluate(window)

            if signal:
                results.append(signal)

        return results
